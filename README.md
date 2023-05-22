
# Stock Watch Python Script

![Python Version](https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A Python script for scraping stock data from Dhaka Stock Exchange (DSE) and Chittagong Stock Exchange (CSE) websites.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Download Stock Watch Executable](#download-stock-watch-executable)
- [License](#license)

## Introduction
Stock Watch Python Script is a tool that allows you to scrape stock data from the Dhaka Stock Exchange (DSE) and Chittagong Stock Exchange (CSE) websites. It fetches data such as last trading price, closing price, day's range, volume, and more for a list of stocks provided in a file[`stock_names.txt`] where you can add or deduct company `Trading Code`. The script utilizes web scraping techniques using the `requests` and `BeautifulSoup` libraries.

## Features
- Scrapes stock data from DSE and CSE websites
- Provides information such as last trading price, closing price, day's range, volume, and more
- Allows customization of data preferences
- Opens stocknow.com.bd for shareholding '%' changes (DSE only)

## Prerequisites
- Python 3.7, 3.8, or 3.9 installed

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/MustakAbsarKhan/stock_watch_py_script.git
   ```
2. Navigate to the project directory:
   ```bash
   cd stock_watch_py_script
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Prepare a file `stock_names.txt` that contains a list of stock names, each on a new line.
2. Run the script:
   ```bash
   python main.py
   ```
3. Follow the prompts:
   - If you wish to go with the default settings, type `y` and press Enter.
   - If you want to customize data preferences, type `n` and follow the instructions.
   - When prompted, you can choose to see data from DSE, CSE, or both.
   - If you choose to see data from DSE, the script will open stocknow.com.bd for shareholding '%' changes.
   - Press Enter to move to the next stock in the list.
4. The script will display the extracted stock data for each stock in the console.

## Download Stock Watch Executable
An executable file `stock_watch.exe` is available for Windows users. You can download it from the following link:

[Download stock_watch.exe](https://raw.githubusercontent.com/MustakAbsarKhan/stock_watch_py_script/main/dist/stock_watch.exe)

Please note that the executable file is specifically built for Windows operating systems.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
```

You can copy and paste the above content into your GitHub repository's README file. Remember to update the link to the stock_watch.exe file if it changes in the future.

Feel free to customize the README further based on your preferences and specific project details.

Let me know if you need any further assistance!