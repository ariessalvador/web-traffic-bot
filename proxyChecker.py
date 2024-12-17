import requests

# File paths
proxy_file_path = "proxyTest.txt"
live_proxy_file_path = "liveProxy.txt"

# Load proxies from the file
def load_proxies(file_path):
    try:
        with open(file_path, "r") as file:
            proxies = [line.strip() for line in file if line.strip()]
        return proxies
    except FileNotFoundError:
        print(f"File {file_path} not found. Please check the path.")
        return []

# Save live proxies to a file
def save_live_proxy(proxy, file_path):
    try:
        with open(file_path, "a") as file:
            file.write(f"{proxy}\n")
    except Exception as e:
        print(f"Failed to save proxy {proxy} to file: {e}")

test_url = 'http://google.com'

# Function to check proxy status
def check_proxy(proxy):
    try:
        proxy_dict = {
            'http': proxy,
            'https': proxy
        }
        response = requests.get(test_url, proxies=proxy_dict, timeout=5)
        
        if response.status_code == 200:
            print(f"Proxy {proxy} is live!")
            save_live_proxy(proxy, live_proxy_file_path)
        else:
            print(f"Proxy {proxy} responded with status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Proxy {proxy} is not working: {e}")

# Main execution
def main():
    # Clear the liveProxy.txt file at the start
    open(live_proxy_file_path, "w").close()
    
    proxies_list = load_proxies(proxy_file_path)
    if proxies_list:
        for proxy in proxies_list:
            check_proxy(proxy)
    else:
        print("No proxies loaded. Exiting.")

if __name__ == "__main__":
    main()
