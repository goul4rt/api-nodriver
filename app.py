from flask import Flask, request, jsonify
import nodriver as uc
import asyncio

app = Flask(__name__)

# Global variable to store the driver instance
driver = None

# Function to start the driver (only once)
async def start_driver():
    global driver
    if driver is None:
        driver = await uc.start(headless=False)

# Async scraper function
async def scraper(url):
    global driver
    # Ensure that the driver is started
    await start_driver()

    # Visit the target website
    page = await driver.get(url)
    # Wait for 1 second to allow JavaScript to load
    await asyncio.sleep(5)

    # Get the full-page HTML    
    html_content = await page.get_content()

    # Return the content without closing the driver
    return html_content

# Helper function to run async functions in a thread
def run_async(func, *args):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    return loop.run_until_complete(func(*args))

@app.route('/scrape', methods=['GET'])
def scrape():
    url = request.args.get('url')  # Get URL from query parameters
    if not url:
        return jsonify({"error": "URL is required"}), 400

    try:
        # Run async scraper function in a thread
        html_content = run_async(scraper, url)
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    return jsonify({"url": url, "html": html_content})

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=3333)
