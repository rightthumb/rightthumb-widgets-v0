import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
	pass
	_.switches.register( 'URLs', '-url', 'url here or leave blank to | pipe', isData='name' )
	_.switches.register( 'Depth', '-d,-depth', '3 defaults to unlimited' )
	_.switches.register( 'MaxThreads', '-t,-threads,-max,-maxThreads', '0 to disable threading. defaults to 10' )
	_.switches.register( 'Omit', '-o,-omit', '-o .zip .pdf' )
_._default_settings_()

_.appInfo[focus()] = {
	'file': 'thisApp.py',
	'description': 'Changes the world',
	'categories': [
						'DEFAULT',
				],
	'examples': [
						_.hp('p thisApp -file file.txt'),
						_.linePrint(label='simple',p=0),
						'',
	],
	'columns': [
	],
	'aliases': [],
	'relatedapps': [],
	'prerequisite': [],
	'notes': [],
}

_.appInfo[focus()] = _.appInfoContinuity(__.thisApp( __file__ ),_.appInfo[focus()])
_.appData[focus()] = _.appDataContinuity()
def appRegDics(): return { 'appInfo': _.appInfo[focus()], 'appData': _.appData[focus()] }

def triggers():
	_._default_triggers_()
	_.switches.trigger( 'Files',   _.isFileAdvanced, vs=False )     # Advanced File Registration    (Fn Alias Resolves To: def myFileLocations)
	_.switches.trigger( 'DB', _.aliasesFi )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'Folders', _.myFolderLocations )
	__.SwitchesModifier.Trigger['Folders'] = _.myFolder
	_.switches.trigger( 'OutputFolder', _.aliasesFo )
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw )
########################################################################################
#n)--> start


import threading
import queue
import time
import traceback


class ThreadManager:
    def __init__(self, threads=10, timeout=None, onDone=None):
        self.max_threads = threads
        self.global_timeout = timeout
        self.onAllDone = onDone

        self._lock = threading.Lock()
        self._job_queue = queue.Queue()
        self._scheduled = []
        self._stop_flag = False

        # Runtime stats
        self.active_count = 0
        self.total_started = 0
        self.total_completed = 0
        self.total_killed = 0
        self.total_timeout = 0
        self.job_log = []

        self._manager_thread = threading.Thread(target=self._manager_loop, daemon=True)
        self._manager_thread.start()

    def queue(self, fn, argsKwargs=None, timeout=None, onStart=None, onDone=None, onKill=None, onTimeout=None, label=None):
        job = {
            "fn": fn,
            "args": argsKwargs if isinstance(argsKwargs, tuple) else (),
            "kwargs": argsKwargs if isinstance(argsKwargs, dict) else {},
            "timeout": timeout,
            "onStart": onStart,
            "onDone": onDone,
            "onKill": onKill,
            "onTimeout": onTimeout,
            "label": label or f"job-{self.total_started + 1}"
        }
        self._scheduled.append(job)
        self._job_queue.put(job)

    def _manager_loop(self):
        while not self._stop_flag:
            if self.active_count < self.max_threads:
                try:
                    job = self._job_queue.get(timeout=0.1)
                except queue.Empty:
                    if self._scheduled == [] and self.active_count == 0 and self.onAllDone:
                        self.onAllDone()
                    continue
                threading.Thread(target=self._run_job, args=(job,), daemon=True).start()
            else:
                time.sleep(0.01)

    def _run_job(self, job):
        label = job["label"]
        start_time = time.time()

        with self._lock:
            self.active_count += 1
            self.total_started += 1

        fn = job["fn"]
        args = job["args"]
        kwargs = job["kwargs"]
        timeout = job["timeout"] if job["timeout"] is not None else self.global_timeout

        start_cb = job["onStart"]
        done_cb = job["onDone"]
        kill_cb = job["onKill"]
        timeout_cb = job["onTimeout"]

        result = None
        error = None
        killed = False
        timed_out = False

        if start_cb:
            try:
                start_cb()
            except Exception:
                traceback.print_exc()

        def target_fn():
            nonlocal result, error
            try:
                result = fn(*args, **kwargs)
            except Exception as e:
                error = e

        t = threading.Thread(target=target_fn)
        t.start()
        t.join(timeout)

        status = "completed"

        if t.is_alive():
            timed_out = True
            killed = True
            status = "timeout"
            with self._lock:
                self.total_timeout += 1
            if timeout_cb:
                try:
                    timeout_cb()
                except Exception:
                    traceback.print_exc()
        elif error:
            killed = True
            status = "killed"
            with self._lock:
                self.total_killed += 1
            if kill_cb:
                try:
                    kill_cb()
                except Exception:
                    traceback.print_exc()
        else:
            with self._lock:
                self.total_completed += 1
            if done_cb:
                try:
                    done_cb(result)
                except Exception:
                    traceback.print_exc()

        duration = time.time() - start_time
        log_entry = {
            "label": label,
            "status": status,
            "result": str(result) if result is not None else None,
            "error": str(error) if error else None,
            "duration": round(duration, 3)
        }

        with self._lock:
            self.active_count -= 1
            self.job_log.append(log_entry)

        if self._scheduled:
            self._scheduled.pop(0)

        if self._scheduled == [] and self.active_count == 0 and self.onAllDone:
            self.onAllDone()

    def stats(self):
        with self._lock:
            return {
                "active": self.active_count,
                "total_started": self.total_started,
                "total_completed": self.total_completed,
                "total_killed": self.total_killed,
                "total_timeout": self.total_timeout,
                "log": list(self.job_log)
            }

    def stop(self):
        self._stop_flag = True


# # start thread manager example
# if __name__ == "__main__":
#     import random

#     def work(i, delay=None):
#         if delay is None:
#             delay = random.uniform(0.5, 2)
#         print(f"→ Work {i}")
#         time.sleep(delay)
#         return f"Done {i}"

#     def on_all_done():
#         print("✅ All jobs complete!")
#         print(tm.stats())

#     tm = ThreadManager(threads=3, onDone=on_all_done)

#     for i in range(7):
#         tm.queue(
#             fn=work,
#             argsKwargs=(i,),
#             label=f"Task-{i}",
#             timeout=1.5,
#             onDone=lambda result: print("✔", result),
#             onTimeout=lambda: print("⏰ Timeout"),
#             onKill=lambda: print("❌ Failed")
#         )

#     while threading.active_count() > 1:
#         time.sleep(0.1)

# # end thread manager example





import os
import threading
import time
import requests
import sys
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup




# start version 1

class SiteSpider:
    def __init__(self, output_folder, omit=None, threaded=True, max_threads=10, max_depth=0):
        self.output_folder = output_folder
        self.omit = omit or []
        self.threaded = threaded
        self.max_threads = max_threads
        self.max_depth = max_depth

        self.visited = set()
        self.lock = threading.Lock()
        self.paths = []
        self.url_map = {}
        self.force_exit = False
        self.thread_manager = ThreadManager(
            threads=max_threads,
            onDone=self._on_all_done
        )
        self.active_threads_event = threading.Event()

    def sanitize_path(self, path, query='', fragment=''):
        if path.endswith('/'):
            path += 'index.html'
        elif not os.path.splitext(path)[1]:
            path += '/index.html'

        extra = ''
        if query:
            extra += '_Q-' + query.replace('=', '_').replace('&', '_')
        if fragment:
            extra += '_F-' + fragment.replace('#', '-')

        filename = path.lstrip('/')
        if extra:
            filename = filename.replace('index.html', f'index{extra}.html')

        return filename

    def save_file(self, url, content):
        parsed = urlparse(url)
        domain_folder = parsed.netloc.replace(':', '_')
        path = self.sanitize_path(parsed.path, parsed.query, parsed.fragment)
        local_path = os.path.join(self.output_folder, domain_folder, path)

        os.makedirs(os.path.dirname(local_path), exist_ok=True)
        with open(local_path, 'wb') as f:
            f.write(content)

        with self.lock:
            relative_path = os.path.relpath(local_path, os.path.join(self.output_folder, domain_folder))
            self.url_map[url] = relative_path
            self.paths.append(relative_path)

        return local_path

    def download_assets(self, soup, base_url):
        downloaded_urls = set()
        tag_attrs = {
            'script': 'src',
            'link': 'href',
            'img': 'src',
            'iframe': 'src',
            'source': 'src',
            'a': 'href'
        }
        for tag, attr in tag_attrs.items():
            for el in soup.find_all(tag):
                src = el.get(attr)
                if src:
                    full_url = urljoin(base_url, src)
                    parsed_src = urlparse(full_url)
                    if parsed_src.netloc == urlparse(base_url).netloc:
                        if full_url not in self.url_map:
                            try:
                                r = requests.get(full_url, timeout=10)
                                self.save_file(full_url, r.content)
                            except Exception as e:
                                print(f"[!] Failed asset: {full_url} → {e}")
                        downloaded_urls.add(full_url)
        return downloaded_urls

    def rewrite_html(self, html_content, base_url):
        soup = BeautifulSoup(html_content, 'html.parser')
        tag_attrs = {
            'script': 'src',
            'link': 'href',
            'img': 'src',
            'iframe': 'src',
            'source': 'src',
            'a': 'href'
        }

        for tag, attr in tag_attrs.items():
            for el in soup.find_all(tag):
                src = el.get(attr)
                if src:
                    full_url = urljoin(base_url, src)
                    with self.lock:
                        local_path = self.url_map.get(full_url)
                    if local_path:
                        current_dir = os.path.dirname(self.url_map.get(base_url, ''))
                        el[attr] = os.path.relpath(local_path, start=current_dir)

        return str(soup)

    def crawl(self, url, depth=0):
        with self.lock:
            if url in self.visited or any(skip in url for skip in self.omit):
                return
            if self.max_depth > 0 and depth > self.max_depth:
                return
            self.visited.add(url)

        print(f"[🌐] Thread started → {url}")
        try:
            response = requests.get(url, timeout=15)
            content_type = response.headers.get('Content-Type', '')

            if 'text/html' not in content_type:
                self.save_file(url, response.content)
                return

            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            downloaded_urls = self.download_assets(soup, url)

            parsed = urlparse(url)
            domain_folder = parsed.netloc.replace(':', '_')
            path = self.sanitize_path(parsed.path, parsed.query, parsed.fragment)
            local_path = os.path.join(self.output_folder, domain_folder, path)
            os.makedirs(os.path.dirname(local_path), exist_ok=True)

            with self.lock:
                relative_path = os.path.relpath(local_path, os.path.join(self.output_folder, domain_folder))
                self.url_map[url] = relative_path
                self.paths.append(relative_path)

            with open(local_path, 'w', encoding='utf-8') as f:
                f.write(self.rewrite_html(html, url))

            print(f"[✓] Saved: {url} → {local_path}")

            for link in downloaded_urls:
                if any(link.lower().endswith(ext) for ext in ['.css', '.js', '.jpg', '.jpeg', '.png', '.gif', '.svg', '.ico', '.woff', '.woff2', '.ttf', '.eot']):
                    continue
                self.thread_manager.queue(self.crawl, argsKwargs=(link, depth + 1), label=link)

        except Exception as e:
            print(f"[✘] Error: {url} — {e}")
        finally:
            print(f"[🏁] Thread ended ← {url}")

    def _on_all_done(self):
        print(f"\n[✔] Spider complete.\n")

    def start(self, root_url):
        def ctrl_c_exit():
            print("🕹️  Press Ctrl+C to stop the spider immediately.")
            try:
                while True:
                    time.sleep(1)
            except KeyboardInterrupt:
                print("\n[⛔] Ctrl+C detected! Force exiting spider...")
                os._exit(0)

        threading.Thread(target=ctrl_c_exit, daemon=True).start()

        self.thread_manager.queue(self.crawl, argsKwargs=(root_url, 0), label="initial")

        while True:
            if not self.thread_manager._scheduled and self.thread_manager.active_count == 0:
                break
            time.sleep(0.25)

        parsed = urlparse(root_url)
        domain_folder = os.path.join(self.output_folder, parsed.netloc.replace(':', '_'))
        init_path = os.path.join(domain_folder, 'spider.init')

        with self.lock:
            init_relative = self.url_map.get(root_url)

        if init_relative:
            with open(init_path, 'w') as f:
                f.write(init_relative)
            print(f"[🕸️] spider.init written: {init_path}")
        else:
            print(f"[!] Could not write spider.init – missing map for {root_url}")

# end version 1
# end version 1


# start beta untested 
# start beta untested 
# start beta untested 
'''
import os
import threading
import time
import requests
import sys
import re
import json
from collections import defaultdict
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup


def relevant(page_text):
    results = {}
    address_regex = re.compile(r'''
        (?P<number>\d{1,6})\s+
        (?P<street>[A-Za-z0-9\s.'\-]+?)\s+
        (?P<type>St(?:reet)?|Ave(?:nue)?|Rd|Road|Blvd|Lane|Ln|Dr|Ct|Pl|Terrace|Way|Circle|Crescent|Highway|Pkwy|Parkway)\b\.?,?\s*
        (?:Apt|Unit|Suite|Ste|#)?\s*(?P<apt>\w{0,10})?,?\s*
        (?P<city>[A-Za-z\s.'\-]+),?\s+
        (?P<state>[A-Z]{2})\s+
        (?P<zip>\d{5}(?:-\d{4})?)
    ''', re.IGNORECASE | re.VERBOSE)

    email_regex = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', re.IGNORECASE)
    phone_regex = re.compile(r'(?:(?:\+?1\s*(?:[.-]\s*)?)?(?:\(?\d{3}\)?|\d{3})\s*(?:[.-]\s*)?)?\d{3}\s*(?:[.-]\s*)?\d{4}', re.VERBOSE)
    url_regex = re.compile(r'https?://[^\s"\'<>]+', re.IGNORECASE)
    zip_regex = re.compile(r'\b\d{5}(?:-\d{4})?\b')

    results['address'] = [m.group(0) for m in address_regex.finditer(page_text)]
    results['email'] = email_regex.findall(page_text)
    results['phone'] = phone_regex.findall(page_text)
    results['url'] = url_regex.findall(page_text)
    results['zip_code'] = zip_regex.findall(page_text)

    return results


class SiteSpider:
    def __init__(self, output_folder, omit=None, threaded=True, max_threads=10, max_depth=0, only=None):
        self.output_folder = output_folder
        self.omit = omit or []
        self.threaded = threaded
        self.max_threads = max_threads
        self.max_depth = max_depth
        self.only = only or []
        self.relevant_data = defaultdict(list)
        self.stop_flags = {'stop': False}

        self.visited = set()
        self.lock = threading.Lock()
        self.paths = []
        self.url_map = {}
        self.force_exit = False
        self.thread_manager = ThreadManager(
            threads=max_threads,
            onDone=self._on_all_done
        )
        self.active_threads_event = threading.Event()

    def sanitize_path(self, path, query='', fragment=''):
        if path.endswith('/'):
            path += 'index.html'
        elif not os.path.splitext(path)[1]:
            path += '/index.html'
        extra = ''
        if query:
            extra += '_Q-' + query.replace('=', '_').replace('&', '_')
        if fragment:
            extra += '_F-' + fragment.replace('#', '-')
        filename = path.lstrip('/')
        if extra:
            filename = filename.replace('index.html', f'index{extra}.html')
        return filename

    def save_file(self, url, content):
        parsed = urlparse(url)
        domain_folder = parsed.netloc.replace(':', '_')
        path = self.sanitize_path(parsed.path, parsed.query, parsed.fragment)
        local_path = os.path.join(self.output_folder, domain_folder, path)
        os.makedirs(os.path.dirname(local_path), exist_ok=True)
        with open(local_path, 'wb') as f:
            f.write(content)
        with self.lock:
            relative_path = os.path.relpath(local_path, os.path.join(self.output_folder, domain_folder))
            self.url_map[url] = relative_path
            self.paths.append(relative_path)
        return local_path

    def download_assets(self, soup, base_url):
        downloaded_urls = set()
        tag_attrs = {
            'script': 'src',
            'link': 'href',
            'img': 'src',
            'iframe': 'src',
            'source': 'src',
            'a': 'href'
        }
        for tag, attr in tag_attrs.items():
            for el in soup.find_all(tag):
                src = el.get(attr)
                if src:
                    full_url = urljoin(base_url, src)
                    parsed_src = urlparse(full_url)
                    if parsed_src.netloc == urlparse(base_url).netloc:
                        if full_url not in self.url_map:
                            try:
                                r = requests.get(full_url, timeout=10)
                                self.save_file(full_url, r.content)
                            except Exception as e:
                                print(f"[!] Failed asset: {full_url} → {e}")
                        downloaded_urls.add(full_url)
        return downloaded_urls

    def rewrite_html(self, html_content, base_url):
        soup = BeautifulSoup(html_content, 'html.parser')
        tag_attrs = {
            'script': 'src',
            'link': 'href',
            'img': 'src',
            'iframe': 'src',
            'source': 'src',
            'a': 'href'
        }
        for tag, attr in tag_attrs.items():
            for el in soup.find_all(tag):
                src = el.get(attr)
                if src:
                    full_url = urljoin(base_url, src)
                    with self.lock:
                        local_path = self.url_map.get(full_url)
                    if local_path:
                        current_dir = os.path.dirname(self.url_map.get(base_url, ''))
                        el[attr] = os.path.relpath(local_path, start=current_dir)
        return str(soup)

    def extract_text_and_check_relevance(self, soup, base_url):
        text = soup.get_text(separator=' ')
        text = re.sub(r'[\r\n]+', ' ', text)
        text = re.sub(r'\s+', ' ', text).strip()
        lower_text = text.lower()
        found = False
        for item in self.only:
            if isinstance(item, dict):
                for label, pattern in item.items():
                    matches = re.findall(pattern, text, flags=re.IGNORECASE)
                    if matches:
                        self.relevant_data[label].extend(matches)
                        found = True
            elif isinstance(item, str):
                if item.startswith('[') and item.endswith(']'):
                    key = item[1:-1].lower()
                    results = relevant(text)
                    if key in results and results[key]:
                        self.relevant_data[key].extend(results[key])
                        found = True
                elif item.lower() in lower_text:
                    found = True
        if found:
            filename = os.path.join(self.output_folder, "relevant.json")
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.relevant_data, f, indent=2)
        if self.only == [0]:
            required = ['address', 'email', 'phone', 'url', 'zip_code']
            if all(self.relevant_data[k] for k in required):
                self.stop_flags['stop'] = True
        return found

    def crawl(self, url, depth=0):
        with self.lock:
            if url in self.visited or any(skip in url for skip in self.omit):
                return
            if self.max_depth > 0 and depth > self.max_depth:
                return
            self.visited.add(url)

        if self.stop_flags['stop']:
            return

        print(f"[🌐] Thread started → {url}")
        try:
            response = requests.get(url, timeout=15)
            content_type = response.headers.get('Content-Type', '')
            if 'text/html' not in content_type:
                self.save_file(url, response.content)
                return
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')

            if self.only:
                should_save = self.extract_text_and_check_relevance(soup, url)
                if not should_save and all(not isinstance(x, str) or not x.startswith('[') for x in self.only):
                    return

            downloaded_urls = self.download_assets(soup, url)
            parsed = urlparse(url)
            domain_folder = parsed.netloc.replace(':', '_')
            path = self.sanitize_path(parsed.path, parsed.query, parsed.fragment)
            local_path = os.path.join(self.output_folder, domain_folder, path)
            os.makedirs(os.path.dirname(local_path), exist_ok=True)
            with self.lock:
                relative_path = os.path.relpath(local_path, os.path.join(self.output_folder, domain_folder))
                self.url_map[url] = relative_path
                self.paths.append(relative_path)
            with open(local_path, 'w', encoding='utf-8') as f:
                f.write(self.rewrite_html(html, url))
            print(f"[✓] Saved: {url} → {local_path}")

            for link in downloaded_urls:
                if any(link.lower().endswith(ext) for ext in ['.css', '.js', '.jpg', '.jpeg', '.png', '.gif', '.svg', '.ico', '.woff', '.woff2', '.ttf', '.eot']):
                    continue
                self.thread_manager.queue(self.crawl, argsKwargs=(link, depth + 1), label=link)
        except Exception as e:
            print(f"[✘] Error: {url} — {e}")
        finally:
            print(f"[🏁] Thread ended ← {url}")

    def _on_all_done(self):
        print(f"\n[✔] Spider complete.\n")

    def start(self, root_url):
        def ctrl_c_exit():
            print("🕹️  Press Ctrl+C to stop the spider immediately.")
            try:
                while True:
                    time.sleep(1)
            except KeyboardInterrupt:
                print("\n[⛔] Ctrl+C detected! Force exiting spider...")
                os._exit(0)
        threading.Thread(target=ctrl_c_exit, daemon=True).start()
        self.thread_manager.queue(self.crawl, argsKwargs=(root_url, 0), label="initial")
        while True:
            if not self.thread_manager._scheduled and self.thread_manager.active_count == 0:
                break
            time.sleep(0.25)
        parsed = urlparse(root_url)
        domain_folder = os.path.join(self.output_folder, parsed.netloc.replace(':', '_'))
        init_path = os.path.join(domain_folder, 'spider.init')
        with self.lock:
            init_relative = self.url_map.get(root_url)
        if init_relative:
            with open(init_path, 'w') as f:
                f.write(init_relative)
            print(f"[🕸️] spider.init written: {init_path}")
        else:
            print(f"[!] Could not write spider.init – missing map for {root_url}")

'''
# end  beta untested 
# end  beta untested 
# end  beta untested 


import sys



def run_spider(url):
	try:
		print(f"[•] Starting spider for: {url}")

		if _.switches.isActive('Depth'):
			max_depth = int(_.switches.values('Depth')[0])
		else:
			max_depth = 0

		threaded = True
		if _.switches.isActive('MaxThreads'):
			max_threads = int(_.switches.values('MaxThreads')[0])
			if not max_threads:
				threaded = False
		else:
			max_threads = 10

		if _.switches.isActive('Omit'):
			omit = _.switches.values('Omit')
		else:
			omit = None

		spider = SiteSpider(output_folder="__Spider__", omit=omit, threaded=threaded, max_threads=max_threads, max_depth=max_depth)
		spider.start(url)

	except Exception as e:
		print(f"[✘] run_spider failed: {url} → {e}")



def action():
	print("Press Ctrl+[ to stop")
	threads = []

	for url in _.isData():
		t = threading.Thread(target=run_spider, args=(url,))
		t.start()
		threads.append(t)

	for t in threads:
		t.join()

	print("\n[✓] All spiders completed.")



########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__)