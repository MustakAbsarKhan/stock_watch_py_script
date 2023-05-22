import requests
import webbrowser
from bs4 import BeautifulSoup

def scrape_dse_data(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            last_trading_price = soup.find('th', string='Last Trading Price').find_next_sibling('td').text
            closing_price = soup.find('th', string='Closing Price').find_next_sibling('td').text
            last_update = soup.find('th', string='Last Update').find_next_sibling('td').text
            days_range = soup.find('th', string="Day's Range").find_next_sibling('td').text
            change = soup.find('th', string='Change*').find_next_sibling('td').text
            days_value = soup.find('th', string="Day's Value (mn)  ").find_next_sibling('td').text
            weeks_range = soup.find('th', string="52 Weeks' Moving Range").find_next_sibling('td').text
            opening_price = soup.find('th', string='Opening Price').find_next_sibling('td').text
            days_volume = soup.find('th', string="Day's Volume (Nos.)").find_next_sibling('td').text
            adjusted_opening_price = soup.find('th', string='Adjusted Opening Price').find_next_sibling('td').text
            days_trade = soup.find('th', string="Day's Trade (Nos.)").find_next_sibling('td').text
            yesterday_closing_price = soup.find('th', string="Yesterday's Closing Price").find_next_sibling('td').text
            market_cap = soup.find('th', string='Market Capitalization (mn)').find_next_sibling('td').text
            
            # Return the extracted data
            return {
                'Last Trading Price': last_trading_price,
                'Closing Price': closing_price,
                'Last Update': last_update,
                "Day's Range": days_range,
                "Change": change,
                "Day's Value (mn)": days_value,
                "52 Weeks' Moving Range": weeks_range,
                'Opening Price': opening_price,
                "Day's Volume (Nos.)": days_volume,
                "Adjusted Opening Price:": adjusted_opening_price,
                "Day's Trade (Nos.)": days_trade,
                "Yesterday's Closing Price": yesterday_closing_price,
                "Market Capitalization (mn):": market_cap
            }
        else:
            print(f"Failed to fetch data from DSE URL: {url}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from DSE URL: {url}")
        print(str(e))
    return None

def scrape_cse_data(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find all <tr> tags within the first table
            table1 = soup.find('table', width="100%", cellspacing="0", cellpadding="0", border="0")
            rows1 = table1.find_all('tr')

            # Extract the desired data from each <td> element within the rows
            data1 = {}
            for row in rows1:
                tds = row.find_all('td')
                if len(tds) == 2:
                    key = tds[0].text.strip()
                    value = tds[1].text.strip()
                    data1[key] = value

            # Find the second table within the HTML
            table2 = soup.find_all('table', width="100%", cellspacing="0", cellpadding="0", border="0")[1]
            rows2 = table2.find_all('tr')

            # Extract the desired data from each <td> element within the rows
            data2 = {}
            for row in rows2:
                tds = row.find_all('td')
                if len(tds) == 2:
                    key = tds[0].text.strip()
                    if key == 'Total Trade':
                        key = 'Total Trade (Nos.)'  # Update the key to match the HTML
                    value = tds[1].text.strip()
                    data2[key] = value
                          

            # Return the extracted data
            return {**data1, **data2}
        else:
            print(f"Failed to fetch data from CSE URL: {url}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from CSE URL: {url}")
        print(str(e))
    return None

def strip_order_numbers(stock_names):
    stripped_names = []
    for name in stock_names:
        stripped_name = name.split('. ', 1)[-1]
        stripped_names.append(stripped_name)
    return stripped_names

# Example usage
stock_names = []

def fetch_values_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            for stock in file:
                stock_names.append(stock.strip())
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    return stock_names


restart = True  # Flag to control program restart

while restart:
    file_path = "stock_names.txt"
    stock_names = fetch_values_from_file(file_path)
    stripped_names = strip_order_numbers(stock_names)
    print(stripped_names)

    for stock in stripped_names:
        default_settings = input("Do you wish to go with the default settings? (y/n): ")
        if default_settings.lower() == 'y':
            show_dse = True
            show_cse = True
        else:
            show_dse = False
            show_cse = False
            preference = input("Do you wish to see data of DSE, CSE, or both? (d/c/b): ")
            if preference.lower() == 'd':
                show_dse = True
            elif preference.lower() == 'c':
                show_cse = True
            elif preference.lower() == 'b':
                show_dse = True
                show_cse = True
        
        if show_dse:
            dse_url = f'https://www.dsebd.org/displayCompany.php?name={stock}'
            stocknow_url = f'https://stocknow.com.bd/search?symbol={stock}'
            dse_data = scrape_dse_data(dse_url)
            print(f"\nData for {stock.upper()} from DSE:")
            if dse_data:
                for key, value in dse_data.items():
                    print(f"{key}: {value}")
            user_pref = input("\n Do you want to Know about shareholding '%' changes? Type y/n (Yes or No) ")
            if user_pref.lower() == "y":
                webbrowser.open(stocknow_url)
    
        if show_cse:
            cse_url = f'https://www.cse.com.bd/company/companydetails/{stock}'
            cse_data = scrape_cse_data(cse_url)
            print(f"\nData for {stock.upper()} from CSE:")
            if cse_data:
                for key, value in cse_data.items():
                    if key != "" and value != "":
                        print(f"{key}: {value}")
        
        input("\nPress ENTER to move to the next answer!!\n")

    choice = input("\n Do you want to Restart the program? (y/n): ")
    if choice.lower() != 'y':
        restart = False
