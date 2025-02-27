# 🌐 Async Web Scraping Service

This is an asynchronous web scraping service built with Flask and nodriver. Perfect for getting HTML content from JavaScript-heavy websites! 🚀

## ✨ Features

- REST endpoint for web page scraping
- Asynchronous browser handling using nodriver
- Browser instance reuse for better performance 
- Returns full page HTML after JavaScript execution
- Handles JavaScript-rendered content 💪

## 📋 Requirements

- Python 3.7+
- Flask
- nodriver
- beautifulsoup4
- apscheduler
- quart

## 🛠️ Installation

1. Clone this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python app.py
   ```

## 🚀 Usage

Send a GET request to the `/scrape` endpoint with a `url` parameter

### Example

Here's a simple Python example using the requests library:

```python
import requests

# Scraping service URL (running locally)
service_url = "http://localhost:3333/scrape"

# URL we want to scrape (e.g., Google)
target_url = "https://www.google.com"

# Making the request to the service
response = requests.get(service_url, params={"url": target_url})

# Checking if the request was successful
if response.status_code == 200:
    # Getting the response data
    data = response.json()
    
    # The complete HTML will be in data["html"]
    html_content = data["html"]
    print("HTML successfully retrieved!")
    print("First 200 characters of HTML:", html_content[:200])
else:
    print("Error:", response.json().get("error"))
```

To use this example:

1. Make sure the service (`app.py`) is running
2. Install the requests library if you haven't already (`pip install requests`)
3. Run the code above

The service will:
- Start a headless browser
- Visit the provided URL
- Wait 5 seconds for JavaScript to execute
- Return the complete HTML of the page after JavaScript execution

This is particularly useful for websites that rely on JavaScript to render their content, as the service waits for JavaScript execution before returning the HTML.