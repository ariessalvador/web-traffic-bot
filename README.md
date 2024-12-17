# Web Traffic Bot and Proxy Checker

This project consists of two main scripts:

1. **Proxy Checker** (`proxyChecker.py`): Verifies the functionality of proxies.
2. **Web Traffic Bot** (`main.py`): Automates website visits using live proxies and random user agents with Selenium.

The project is designed to check proxies, filter out live ones, and generate web traffic using the validated proxies.

---

## Project Structure

```
web-traffic-bot/
|-- main.py             # Web traffic bot script
|-- proxyChecker.py     # Proxy checker script
|-- liveProxy.txt       # File to store live proxies
|-- proxyTest.txt       # Input file containing proxy list for testing
|-- requirements.txt    # List of required Python libraries
|-- README.md           # Project documentation
```

---

## Features

1. **Proxy Checker**:
   - Loads proxies from `proxyTest.txt`.
   - Tests each proxy by attempting to connect to `http://google.com`.
   - Saves working proxies into `liveProxy.txt`.

2. **Web Traffic Bot**:
   - Reads live proxies from `liveProxy.txt`.
   - Automates browser interactions to visit a target website.
   - Simulates human behavior using:
     - Randomized scrolling (page up/down).
     - Randomized visit duration (5-60 seconds).
     - Random User-Agent selection.
   - Supports running in headless mode (no browser UI).

3. **Customizable Options**:
   - **Target URL**: Set the target website to receive traffic.
   - **ChromeDriver Path**: Specify the path to your ChromeDriver executable.
   - **User Agents**: List of random User-Agent strings for browser simulation.
   - **Proxy File**: Provide input proxy lists for validation.

---

## Prerequisites

Before running the project, ensure you have the following installed:

- **Python 3.x**
- **Google Chrome** (latest version)
- **ChromeDriver** (compatible with your Chrome version)

Install dependencies using pip:
```bash
pip install -r requirements.txt
```

This will install:
- Selenium
- Requests

Download [ChromeDriver](https://googlechromelabs.github.io/chrome-for-testing/) and ensure it matches your installed Chrome version.

---

## How to Use

### 1. Prepare Proxy List
Place your proxy list (one proxy per line, `IP:Port` format) into `proxyTest.txt`.
Example:
```
123.45.67.89:8080
111.222.333.444:3128
```
### 2. Install Requirements
Install all dependencies:

```bash
pip install -r requirements.txt
```

### 3. Check Proxies
Run the `proxyChecker.py` script to validate proxies:
```bash
python proxyChecker.py
```
This will generate a `liveProxy.txt` file containing only the working proxies.

### 4. Run Web Traffic Bot
Update the following settings in `main.py`:
- **`TARGET_URL`**: Replace with the URL of the website you want to visit.
- **`CHROMEDRIVER_PATH`**: Path to the ChromeDriver executable.

Run the bot:
```bash
python main.py
```
The script will:
- Use live proxies from `liveProxy.txt`.
- Simulate multiple visits to the target website.

---

## Notes

1. **Headless Mode**: The browser runs in headless mode, so it won't be visible during execution.
2. **Traffic Simulation**: The bot simulates real user behavior by scrolling and staying on pages for random durations.
3. **Proxy List**: Ensure you use high-quality proxies for better results.

---

## Example Workflow

1. Prepare a proxy list (`proxyTest.txt`).
2. Install dependencies using (`requirements.txt`).
3. Run `proxyChecker.py` to filter live proxies.
4. Update the target website and ChromeDriver path in `main.py`.
5. Run `main.py` to generate automated traffic.

---

## Disclaimer
This project is for educational purposes only. Use it responsibly and ensure compliance with applicable laws and website terms of service. Misuse of this tool may lead to IP bans or legal consequences.

---


## License
This project is licensed under the MIT License. See `LICENSE` for more details.
