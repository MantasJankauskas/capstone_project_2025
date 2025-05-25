import time
import threading

class Loader:
    def __init__(self, desc="Loading...", end="Done!", timeout=0.1):
        self.desc = desc
        self.end = end
        self.timeout = timeout
        self._running = False
        self._thread = None

    def start(self):
        self._running = True
        self._thread = threading.Thread(target=self._animate)
        self._thread.start()

    def _animate(self):
        chars = "|/-\\"
        idx = 0
        while self._running:
            print(f"\r{self.desc} {chars[idx % len(chars)]}", end="", flush=True)
            idx += 1
            time.sleep(self.timeout)
        print(f"\r{self.end}{' ' * 10}")

    def stop(self):
        self._running = False
        if self._thread is not None:
            self._thread.join()