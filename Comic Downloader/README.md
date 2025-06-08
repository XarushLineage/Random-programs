# Comic Downloader

This script downloads comic page images from a website.

## Usage
1. Run `python comic_downloader.py`.
2. Enter the base website URL containing the list of issues.
3. Provide the starting and ending issue numbers (1‑based).
4. Choose the folder where images should be saved.

The script uses Selenium to open each issue, selects the **All pages** option, waits 10 seconds for images to load and then downloads each image. Relative links are automatically converted to full URLs.

Dependencies: `requests`, `beautifulsoup4`, `selenium`, `tkinter` (usually included with Python) and a Selenium WebDriver (e.g. Firefox geckodriver).
