import urllib.request
import time
from concurrent.futures import ThreadPoolExecutor
def download_site(url):
    print(f"Stahujem... " + url)
    with urllib.request.urlopen(url) as response:
        return f"Stiahnuté {url}: {len(response.read())} bytov"
sites = ["http://www.google.com", "http://www.wienerberger.sk", "http://www.wienerberger.com", "http://www.yahoo.com"]
threads = []
start_time = time.time()
with ThreadPoolExecutor(max_workers=3) as executor:
    futures = []
    for site in sites:
        futures.append(executor.submit(download_site, site))
    for future in futures:
        result = future.result()
        print(result)
duration = time.time() - start_time
print(f"Stiahnuté {len(sites)} stránok za {duration} sekúnd")