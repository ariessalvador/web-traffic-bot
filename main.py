import random
import time
import traceback
from itertools import cycle
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Replace with your target website URL
TARGET_URL = "http://example.com"

# Replace with the path to your ChromeDriver executable
CHROMEDRIVER_PATH = "/path/to/chromedriver"

# List of user agents for random selection
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
]

def load_proxies(file_path):
    try:
        with open(file_path, 'r') as f:
            proxies = [line.strip() for line in f if line.strip()]
        print(f"Loaded {len(proxies)} proxies from {file_path}")
        return proxies
    except Exception as e:
        print(f"Error reading proxy file {file_path}: {e}")
        return []

def visit_website_with_selenium(proxy, url):
    try:
        options = webdriver.ChromeOptions()
        options.add_argument(f"user-agent={random.choice(USER_AGENTS)}")


        if proxy:
            options.add_argument(f'--proxy-server=http://{proxy}')
        
        options.add_argument('--headless')  
        options.add_argument('--no-sandbox')  
        options.add_argument('--disable-dev-shm-usage')  
        options.add_argument('--disable-gpu')  
        options.add_argument('--window-size=1920,1080')  


        driver = webdriver.Chrome(service=Service(CHROMEDRIVER_PATH), options=options)


        driver.get(url)
        print(f"Successfully opened {url} using proxy {proxy} (Headless Mode)")


        for _ in range(random.randint(2, 5)):
            action = random.choice(['down', 'up'])
            if action == 'down':
                driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
            else:
                driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_UP)
            print(f"Scrolled {action} on {url}")
            time.sleep(random.randint(2, 5))  


        stay_duration = random.randint(5, 60)
        print(f"Staying on page for {stay_duration} seconds...")
        time.sleep(stay_duration)

        driver.quit()

    except Exception as e:
        print(f"Error visiting {url} with proxy {proxy}: {e}")
        traceback.print_exc()

def main():
    proxy_file = "liveProxy.txt"  
    proxies = load_proxies(proxy_file)
    
    if not proxies:
        print("No proxies loaded. Exiting program.")
        return
    
 
    proxy_pool = cycle(proxies)
    for _ in range(500):  # Number of visits
        proxy = next(proxy_pool)
        visit_website_with_selenium(proxy, TARGET_URL)

if __name__ == "__main__":
    main()
