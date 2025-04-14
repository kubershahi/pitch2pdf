# Pitch2PDF

A Python tool to convert Pitch.com presentations to PDF files.

## Features

- Converts Pitch.com presentations to PDF
- Handles multiple slides
- Preserves slide quality
- Command-line interface

## Requirements

- Python 3.8+
- Google Chrome installed
- ChromeDriver version **matching your Chrome version**

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/pitch2pdf.git
cd pitch2pdf
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Install ChromeDriver:

#### Step 1: Check Chrome Version
- Open Chrome browser
- Visit: `chrome://settings/help`
- Note down your Chrome version number

#### Step 2: Download ChromeDriver
- Visit [Chrome for Testing](https://googlechromelabs.github.io/chrome-for-testing/)
- Find the version matching your Chrome browser
- Download the appropriate `chromedriver` for your operating system
- Extract the downloaded file
- Save the `chromedriver` binary in your project directory

## Usage

```bash
python pitch2pdf.py \
    --pitch_url "https://pitch.com/your-presentation-url" \
    --chrome_driver "/path/to/chromedriver"
```

### Arguments
- `--pitch_url`: URL of the Pitch.com presentation (required)
- `--chrome_driver`: Path to ChromeDriver (optional, defaults to "./chromedriver")

## License

MIT License