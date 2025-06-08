import os
import time
import requests
from bs4 import BeautifulSoup
from tkinter import Tk, filedialog
from selenium import webdriver
from selenium.webdriver.support.ui import Select


def get_save_directory():
    """Open a GUI dialog asking the user where to save files."""
    root = Tk()
    root.withdraw()
    directory = filedialog.askdirectory(title="Select directory to save images")
    root.destroy()
    return directory


def download_image(url, save_dir, idx):
    """Download a single image to the save directory."""
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        ext = os.path.splitext(url)[1]
        if not ext:
            ext = '.jpg'
        file_path = os.path.join(save_dir, f"image_{idx}{ext}")
        with open(file_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024):
                file.write(chunk)


def main():
    # Request user input
    base_url = input("Enter website URL: ")
    start_num = int(input("Enter starting issue number: "))
    end_num = int(input("Enter ending issue number: "))

    save_dir = get_save_directory()
    if not save_dir:
        print("No directory selected. Exiting.")
        return

    # Fetch the issue links from the main page
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Example filtering: adjust selectors to match the target website
    links = [a['href'] for a in soup.find_all('a', href=True) if 'Issue' in a.text]

    if not links:
        print("No issue links found.")
        return

    # Adjust indices for 1-based user input
    selected_links = links[start_num - 1:min(end_num, len(links))]

    # Use Selenium to open each link so that the site can load all pages
    driver = webdriver.Firefox()

    try:
        for link in selected_links:
            print(f"Processing {link}")
            driver.get(link)

            # Select the option to view all pages
            select = Select(driver.find_element('id', 'selectReadType'))
            select.select_by_value('1')

            # Wait for the page to load all images
            time.sleep(10)

            # Parse the updated page and download all images
            page_soup = BeautifulSoup(driver.page_source, 'html.parser')
            images = [img['src'] for img in page_soup.find_all('img') if img.get('src')]

            for idx, img_url in enumerate(images):
                download_image(img_url, save_dir, idx)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
