# Stock Data Downloader

This repository contains scripts for downloading stock price data from various sources, particularly for financial technology (fintech) companies in Vietnam.

## Project Overview

The scripts in this repository help automate the retrieval of historical stock price data from sources such as VCBS and Vietstock. The stock symbols are categorized and stored in the `stock_name.py` file.

## Files and Functionality

- **`stock_download.py`**:  
  - Fetches stock price history from VCBS.  
  - Saves data as JSON files.  
  - Iterates through stock symbols listed in `stock_name.py`.

- **`vietstock.py`**:  
  - Opens Vietstock links for specific fintech stocks in a web browser.  
  - Automates downloading of trading result reports.

- **`stock_name.py`**:  
  - Contains categorized lists of stock symbols (e.g., fintech, real estate, healthcare).  
  - Used by other scripts to determine which stocks to process.

## Requirements

- Python 3.x
- `requests` library (for API calls in `stock_download.py`)

## Installation

1. Clone this repository:
   ```sh
   git clone https://github.com/your-repo-name.git
   cd your-repo-name
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
   *(If using only `stock_download.py`, ensure `requests` is installed.)*

## Usage

### Download Stock Data from VCBS
```sh
python stock_download.py
```
- This will save stock data as JSON files in the specified directory.

### Open Vietstock Trading Results
```sh
python vietstock.py
```
- This script will open stock trading data in a web browser.

## Notes

- The directory for storing JSON data is hardcoded in `stock_download.py`. Modify the `os.chdir` line to match your preferred path.
- Ensure you have internet access when running these scripts.

## License

This project is open-source. Feel free to modify and adapt it to your needs.

---

