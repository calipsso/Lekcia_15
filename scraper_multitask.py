import threading
import urllib.request
import time

def download_site(url):
    with urllib.request.urlopen(url) as response:
        print(f"Stiahnutie {url}: {len(response.read())} bytov")

sites = ["http://www.google.com", "http://www.wienerberger.sk", "http://www.wienerberger.com", "http://www.yahoo.com"]

threads = []

start_time = time.time()

duration = time.time() - start_time
#print(f"Stiahnnute {len(sites)} stranok za {duration} sekund")

for url in sites:
    thread=threading.Thread(target=download_site, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

duration = time.time() - start_time
print(f"Stiahnnute {len(sites)} stranok za {duration} sekund")
