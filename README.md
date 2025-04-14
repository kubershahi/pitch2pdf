# Pitch2PDF

A Python tool to convert Pitch.com presentations to PDF files.

## Features

- Converts Pitch.com presentations to PDF
- Handles multiple slides
- Preserves slide quality
- Command-line interface

## Requirements

- Python 3.8+
- Chrome browser
- ChromeDriver

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
- macOS: `brew install chromedriver`
- Ubuntu/Debian: `sudo apt-get install chromedriver`
- Windows: Download from https://chromedriver.chromium.org/downloads

## Usage

```bash
python pitch2pdf.py --pitch_url "https://pitch.com/your-presentation-url" --chrome_driver "/path/to/chromedriver"
```

Arguments:
- `--pitch_url`: URL of the Pitch.com presentation (required)
- `--chrome_driver`: Path to ChromeDriver (optional, defaults to "./chromedriver")

## License

MIT License