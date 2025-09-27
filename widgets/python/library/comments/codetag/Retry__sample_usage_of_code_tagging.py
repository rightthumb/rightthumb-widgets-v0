#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#<app RetryKit v=1.0.0 id=retry-kit lang=python process=file.(python).contents.block.index-version scope=down />
# Minimal, dependency-free retry utility with jittered exponential backoff and a decorator.

from __future__ import annotations
import time, random, math
from dataclasses import dataclass
from typing import Callable, Iterable, Optional, Type, TypeVar, Any, Tuple

T = TypeVar("T")

#<sec Types v=1 id=types scope=down />
@dataclass(frozen=True)
class RetryResult:
	"""Outcome summary for a retryable operation."""
	attempts: int
	elapsed: float
	last_exception: Optional[BaseException] = None
#</sec Types>


#<fn sleep_backoff v=1 id=util-sleep process=file.(python).contents.(unit) scope=down />
def sleep_backoff(base: float, factor: float, attempt: int, jitter: float, cap: float) -> float:
	"""
	Compute the next sleep (seconds) using exponential backoff with optional jitter.

	Args:
		base: Starting delay (e.g., 0.1).
		factor: Exponential multiplier per attempt (e.g., 2.0).
		attempt: Zero-based attempt index.
		jitter: Jitter fraction in [0,1]; 0.1 ⇒ ±10% randomization.
		cap: Maximum sleep cap.
	Returns:
		The bounded sleep duration in seconds.
	"""
	#<sec BackoffFormula v=1 id=backoff meta={ desc: 'exp backoff with jitter', risk: low } scope=down />
	raw = base * (factor ** attempt)
	if jitter:
		span = raw * jitter
		raw = random.uniform(max(0.0, raw - span), raw + span)
	return min(raw, cap)
	#</sec BackoffFormula>


#<fn retryable v=1 id=retryable-decorator process=file.(python).contents.(unit) scope=down />
def retryable(
	exceptions: Iterable[Type[BaseException]] | Type[BaseException] = Exception,
	tries: int = 5,
	base: float = 0.1,
	factor: float = 2.0,
	jitter: float = 0.1,
	cap: float = 5.0,
	timeout: Optional[float] = None,
	predicate: Optional[Callable[[Exception], bool]] = None,
) -> Callable[[Callable[..., T]], Callable[..., T]]:
	"""
	Decorator factory to retry a function on failure.

	Args:
		exceptions: Exception type(s) to catch and retry.
		tries: Max attempt count (≥1).
		base: Initial backoff delay (seconds).
		factor: Exponential multiplier per attempt.
		jitter: Fractional jitter [0,1] applied to delay.
		cap: Max per-sleep delay (seconds).
		timeout: Optional wall-clock timeout across all attempts.
		predicate: Optional filter; retry only if predicate(exc) is True.
	Returns:
		A decorator that wraps the function with retry logic.
	"""
	#<under lines=3 meta={ desc: keep defaults sane }>
	if tries < 1:
		raise ValueError("tries must be ≥ 1")
	if jitter < 0 or jitter > 1:
		raise ValueError("jitter must be within [0,1]")

	if not isinstance(exceptions, tuple):
		exceptions = (exceptions,)

	def decorator(fn: Callable[..., T]) -> Callable[..., T]:
		#<sec DecoratedCall v=1 id=decorated-call scope=down />
		def wrapper(*args: Any, **kwargs: Any) -> T:
			start = time.monotonic()
			attempt = 0
			while True:
				try:
					return fn(*args, **kwargs)
				except exceptions as exc:  # only retry whitelisted exceptions
					if predicate and not predicate(exc):
						raise
					attempt += 1
					elapsed = time.monotonic() - start
					# Give up if attempts or time budget exceeded
					if attempt >= tries or (timeout is not None and elapsed >= timeout):
						raise
					time.sleep(sleep_backoff(base, factor, attempt - 1, jitter, cap))
		#</sec DecoratedCall>
		return wrapper
	return decorator


#<sec RetryClass v=1 id=retry-class scope=down />
class Retry:
	"""
	Imperative retry helper with detailed results and a call-style interface.

	Common uses:
	- Retry transient network calls (HTTP 5xx, timeouts).
	- Wrap DB operations that fail sporadically under load.
	"""

	#<fn __init__ v=1 id=retry-init process=file.(python).contents.(unit) scope=down />
	def __init__(
		self,
		exceptions: Iterable[Type[BaseException]] | Type[BaseException] = Exception,
		tries: int = 5,
		base: float = 0.1,
		factor: float = 2.0,
		jitter: float = 0.1,
		cap: float = 5.0,
		timeout: Optional[float] = None,
		predicate: Optional[Callable[[Exception], bool]] = None,
		record_last_exception: bool = True,
	) -> None:
		if not isinstance(exceptions, tuple):
			exceptions = (exceptions,)
		self.exceptions = exceptions
		self.tries = max(1, int(tries))
		self.base = float(base)
		self.factor = float(factor)
		self.jitter = max(0.0, min(1.0, float(jitter)))
		self.cap = float(cap)
		self.timeout = timeout if timeout is None else float(timeout)
		self.predicate = predicate
		self.record_last_exception = bool(record_last_exception)

	#<fn __call__ v=1 id=retry-call process=file.(python).contents.(unit) scope=down />
	def __call__(self, fn: Callable[..., T], *args: Any, **kwargs: Any) -> Tuple[T | None, RetryResult]:
		"""
		Call `fn` with retries. Returns (value, RetryResult); `value` is None if final attempt failed.

		The function's exception is re-raised only if `record_last_exception` is False.
		Otherwise, we suppress on final failure and report it in RetryResult.
		"""
		#<sec CallLoop v=1 id=call-loop meta={ desc:'core retry loop with time budget' } scope=down />
		start = time.monotonic()
		attempts = 0
		last_exc: Optional[BaseException] = None

		while True:
			try:
				value = fn(*args, **kwargs)
				elapsed = time.monotonic() - start
				return value, RetryResult(attempts=attempts + 1, elapsed=elapsed, last_exception=None)

			except self.exceptions as exc:
				if self.predicate and not self.predicate(exc):
					# Predicate veto: do not retry this exception
					raise
				attempts += 1
				last_exc = exc
				elapsed = time.monotonic() - start

				#<under lines=3 meta={ desc:'termination checks' }>
				if attempts >= self.tries:
					break
				if self.timeout is not None and elapsed >= self.timeout:
					break
				#</under>

				delay = sleep_backoff(self.base, self.factor, attempts - 1, self.jitter, self.cap)
				time.sleep(delay)

		# Final failure path
		elapsed = time.monotonic() - start
		if not self.record_last_exception and last_exc is not None:
			raise last_exc
		return None, RetryResult(attempts=attempts, elapsed=elapsed, last_exception=last_exc)
		#</sec CallLoop>

	#<fn decorator v=1 id=retry-decorator method=true process=file.(python).contents.(unit) scope=down />
	def decorator(self) -> Callable[[Callable[..., T]], Callable[..., T]]:
		"""
		Create a decorator bound to this Retry instance.
		"""
		def _wrap(fn: Callable[..., T]) -> Callable[..., T]:
			def _inner(*args: Any, **kwargs: Any) -> T:
				val, result = self(fn, *args, **kwargs)
				if result.last_exception is not None:
					# Re-raise to let callers handle; change behavior by toggling record_last_exception
					raise result.last_exception
				return val  # type: ignore[return-value]
			return _inner
		return _wrap
#</sec RetryClass>


#<sec Example v=1 id=example meta={ desc:'basic usage demo' } scope=down />
if __name__ == "__main__":
	# Freeze any literal you never want mutated by tooling:
	#<sec FrozenLiteral v=1 id=frozen meta={ desc:'do not edit literal' } freeze:true scope=down />
	STABLE_MESSAGE = "This string is intentionally stable."
	#</sec FrozenLiteral>

	@retryable(exceptions=ValueError, tries=3, base=0.05, factor=2.0, jitter=0.2, cap=0.2)
	def flaky_once(counter={"n": 0}):
		counter["n"] += 1
		if counter["n"] < 2:
			raise ValueError("transient!")
		return "ok"

	print("decorator result:", flaky_once())

	r = Retry(exceptions=(ValueError,), tries=3, base=0.05, factor=2.0, jitter=0.2, cap=0.2)
	value, meta = r(lambda: "ok")  # succeeds first try
	print("class call result:", value, meta)
#</sec Example>