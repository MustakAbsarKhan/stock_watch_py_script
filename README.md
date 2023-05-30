# Stock Watch Python Script

<br>
<p align="center">
  
  <a href="https://github.com/MustakAbsarKhan/nvidia_driver_updator/issues">
    <img src="https://img.shields.io/github/issues/MustakAbsarKhan/nvidia_driver_updator"/> 
  </a>
  <a href="https://github.com/MustakAbsarKhan/nvidia_driver_updator/network/members">
    <img src="https://img.shields.io/github/forks/MustakAbsarKhan/nvidia_driver_updator"/> 
  </a>  
  <a href="https://github.com/MustakAbsarKhan/nvidia_driver_updator/stargazers">
    <img src="https://img.shields.io/github/stars/MustakAbsarKhan/nvidia_driver_updator"/> 
  </a>
    <a href="https://github.com/MustakAbsarKhan/nvidia_driver_updator/LICENSE">
    <img src="https://img.shields.io/github/license/MustakAbsarKhan/nvidia_driver_updator"/> 
  </a>
</p>
<br>
<p align="center">
A Python script for scraping stock data from Dhaka Stock Exchange (DSE) and Chittagong Stock Exchange (CSE) websites.
</p>

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Introduction
Stock Watch Python Script is a tool that allows you to scrape stock data from the Dhaka Stock Exchange (DSE) and Chittagong Stock Exchange (CSE) websites. It fetches data such as the last trading price, closing price, day's range, volume, and more for a list of stocks provided in the `stock_names.txt` file. The script utilizes web scraping techniques using the `requests`, `BeautifulSoup`, and `tqdm` libraries.

## Features
- Scrapes stock data from DSE and CSE websites
- Provides information such as the last trading price, closing price, day's range, volume, and more
- Allows customization of data preferences
- Opens `stocknow.com.bd` for shareholding '%' changes (DSE only)

## Prerequisites
- Python 3.7, 3.8, or 3.9 installed
- Required Python packages: `requests`, `beautifulsoup4`, and `tqdm`. Install them using the following command:
  ```bash
  pip install requests beautifulsoup4 tqdm
  ```

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/MustakAbsarKhan/stock_watch_py_script.git
   ```
2. Navigate to the project directory:
   ```bash
   cd stock_watch_py_script
   ```

## Usage
1. Prepare the `stock_names.txt` file:
   - Create a file named `stock_names.txt` in the project directory.
   - Add the trading codes of the stocks you want to fetch data for, with each code on a new line.
   - Save the file.

2. Run the script:
   ```bash
   python main.py
   ```

3. Follow the prompts:
   - If you wish to go with the default settings and see data from both DSE and CSE, type `y` and press Enter.
   - If you want to customize data preferences, type `n` and follow the instructions.
   - When prompted, you can choose to see data from DSE, CSE, or both.
   - If you choose to see data from DSE, the script will open stocknow.com.bd for shareholding '%' changes.
   - Press Enter to move to the next stock in the list.

4. The script will display the extracted stock data for each stock in the console.

5. If you prefer using the executable file (`stock_watch.exe`) you can find it as `stock_watch.zip` inside exe_file folder in the [Repository](https://github.com/MustakAbsarKhan/stock_watch_py_script). You can simply double-click on it to launch the program. The executable file eliminates the need for installing dependencies and running the script from the command line.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
