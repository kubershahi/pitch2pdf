# Pitch Presentation to PDF
This project uses [Selenium](https://www.selenium.dev/) and [ChromeDriver](https://googlechromelabs.github.io/chrome-for-testing/) to automatically crawl through a public [Pitch.com](https://pitch.com) presentation, capture each slide, and save them all as a single PDF.
---

## 📸 Features

- Automatically navigates through all slides using arrow keys
- Waits for slide content to fully load before capturing
- Takes high-resolution screenshots
- Combines all slide images into a single PDF
---

## 📦 Requirements

- Python 3.8+
- Google Chrome installed
- ChromeDriver version **matching your Chrome version**

Install Python dependencies:

```bash
pip install -r requirements.txt
```
---

## 🚀 How to Use

### Step 1: Check Your Chrome Version

Open Chrome and visit: chrome://settings/help
---

### Step 2: Download Matching ChromeDriver

1. Go to: [https://googlechromelabs.github.io/chrome-for-testing/](https://googlechromelabs.github.io/chrome-for-testing/)
2. Locate your exact Chrome version
3. Download the correct `chromedriver` binary for your OS
4. Extract it and save the path to the binary
---

### Step 3: Run the script

Run the script using:

```bash
python pitch2pdf.py \
    --pitch_url https://pitch.com/v/spa2_-coordinates-transformations-and-perception-nkmrmy \
    --chrome_driver ./chromedriver
```