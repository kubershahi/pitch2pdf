import os
import re
import argparse
from hashlib import md5

from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def capture_all_slides(pitch_url, chromedriver_path, max_slides=50):
    # Create output folder for screenshots
    output_folder = "slide_images"
    os.makedirs(output_folder, exist_ok=True)

    # Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--window-size=1920,1080")

    # Launch driver
    service = Service(executable_path=chromedriver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # time.sleep(10)
    driver.get(pitch_url)  # Let the page render

    output_pdf = re.sub(r'[\\/*?:"<>|]', "", driver.title.strip()) + ".pdf"

    actions = ActionChains(driver)

    image_paths = []

    wait = WebDriverWait(driver, timeout=5)
    actions = ActionChains(driver)
    prev_hash = ""

    for i in range(max_slides):
        print(f"Capturing slide {i + 1}")

        # Wait for slide container to load
        slide_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[class*='canvas-precision-wrapper']")))
        current_html = slide_element.get_attribute("innerHTML")
        current_hash = md5(current_html.encode("utf-8")).hexdigest()

        if current_hash == prev_hash:
            print("Slide content unchanged. Possibly reached the last slide.")
            break

        slide_path = os.path.join(output_folder, f"slide_{i + 1:03d}.png")
        driver.save_screenshot(slide_path)
        image_paths.append(slide_path)

        prev_hash = current_hash

        # Press → to go to next slide
        actions.send_keys(Keys.ARROW_RIGHT).perform()

        # Wait until slide changes
        try:
            wait.until(lambda d: md5(d.find_element(By.CSS_SELECTOR, "div[class*='canvas-precision-wrapper']").get_attribute("innerHTML").encode("utf-8")).hexdigest() != prev_hash)
        except Exception as e:
            print(e)
            print("Timeout waiting for next slide to load.")
            break

    driver.quit()

    # Convert screenshots to PDF
    images = [Image.open(p).convert("RGB") for p in image_paths]
    if images:
        images[0].save(output_pdf, save_all=True, append_images=images[1:])
        print(f"[✓] PDF saved as: {output_pdf}")
    else:
        print("No images captured. PDF not generated.")
    
    # Remove all images
    for image in image_paths:
        os.remove(image)
    # Remove directory
    os.rmdir(output_folder)


if __name__ == "__main__":
    # === CONFIG ===
    parser = argparse.ArgumentParser(description="Convert Pitch presentations to PDF")
    parser.add_argument("--pitch_url", type=str, required=True, help="URL of the Pitch presentation")
    parser.add_argument("--chrome_driver", type=str, default="./chromedriver", help="Path to ChromeDriver")
    args = parser.parse_args()

    pitch_url = args.pitch_url
    chromedriver_path = args.chrome_driver
    max_slide_count = 80  # Adjust based on your slide count
    capture_all_slides(pitch_url, chromedriver_path, max_slide_count)
