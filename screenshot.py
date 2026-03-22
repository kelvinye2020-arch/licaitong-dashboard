import asyncio
from playwright.async_api import async_playwright

async def capture_screenshots():
    urls = [
        ("https://kelvinye2020-arch.github.io/fund-briefing/", "fund-briefing.png"),
        ("https://kelvinye2020-arch.github.io/market-dashboard/", "market-dashboard.png"),
        ("https://bank-marketing-report-f92sjti9dl.edgeone.dev/bank_marketing_report.html", "bank-marketing.png"),
    ]
    
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        
        for url, filename in urls:
            print(f"Capturing {url}...")
            page = await browser.new_page()
            await page.set_viewport_size({"width": 1200, "height": 800})
            await page.goto(url, wait_until="networkidle", timeout=60000)
            await page.screenshot(path=f"thumbnails/{filename}", full_page=False)
            await page.close()
            print(f"Saved thumbnails/{filename}")
        
        await browser.close()
        print("Done!")

if __name__ == "__main__":
    asyncio.run(capture_screenshots())
