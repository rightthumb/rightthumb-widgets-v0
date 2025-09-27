import threading
import time

class MinThread:
	def __init__(self, fn, *args, **kwargs):
		self.fn = fn
		self.args = args
		self.kwargs = kwargs
		self.thread = None
		self.running = False
		self.expire_time = None  # Expiration time if needed
		self.lock = threading.Lock()  # Ensures thread-safe operations

		# Event handlers stored in a dictionary
		self.on = {
			"onExpire": None,
			"onComplete": None,
			"onStop": None,
			"onKill": None,
			"onAnyStop": None
		}

		# Start the monitoring thread
		self.monitor_thread = threading.Thread(target=self._monitor, daemon=True)
		self.monitor_running = True
		self.monitor_thread.start()

	def start(self):
		"""Start the worker thread."""
		with self.lock:
			if not self.running:
				self.running = True
				self.thread = threading.Thread(target=self._run)
				self.thread.start()

	def _run(self):
		"""Internal method to execute the function."""
		try:
			self.fn(*self.args, **self.kwargs)
			self._trigger_event("onComplete")
		except Exception as e:
			print(f"Thread error: {e}")
		finally:
			with self.lock:
				self.running = False
				self._trigger_event("onAnyStop")

	def _monitor(self):
		"""Monitors thread completion and expiration."""
		while self.monitor_running:
			with self.lock:
				if not self.running:  # If main thread is not running, stop monitoring
					self.monitor_running = False
					break

				if self.expire_time and time.time() >= self.expire_time:
					self.kill()
					self._trigger_event("onExpire")

			time.sleep(0.1)  # Prevent CPU overuse

	def set_expiration(self, seconds):
		"""Set expiration time in seconds."""
		with self.lock:
			self.expire_time = time.time() + seconds

	def kill(self):
		"""Force kill the thread."""
		with self.lock:
			if self.running:
				self.running = False
				self.thread = None
				self._trigger_event("onKill")
				self._trigger_event("onAnyStop")

	def stop(self):
		"""Gracefully stop the thread."""
		with self.lock:
			if self.running:
				self.running = False
				self._trigger_event("onStop")
				self._trigger_event("onAnyStop")

	def _trigger_event(self, event_name):
		"""Trigger an event if it exists in `self.on`."""
		if event_name in self.on and callable(self.on[event_name]):
			self.on[event_name]()



# import time

# def my_function():
#     print("Thread started")
#     time.sleep(5)
#     print("Thread finished")

# aThread = MinThread(my_function)
# aThread.on["onComplete"] = lambda: print("Thread completed")
# aThread.on["onExpire"] = lambda: print("Thread expired")
# aThread.on["onKill"] = lambda: print("Thread killed")
# aThread.on["onAnyStop"] = lambda: print("Thread stopped (any reason)")

# aThread.start()

# # Example: Set expiration to 3 seconds (will auto-kill if not completed)
# aThread.set_expiration(3)