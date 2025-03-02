from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import pandas as pd
import time
from datetime import datetime, timedelta

# List of all 100 U.S. Senators (first name, last name, state)
senators = [
    {"first_name": "Angela", "last_name": "Alsobrooks", "state": "Maryland"},
    {"first_name": "Tammy", "last_name": "Baldwin", "state": "Wisconsin"},
    {"first_name": "Jim", "last_name": "Banks", "state": "Indiana"},
    {"first_name": "John", "last_name": "Barrasso", "state": "Wyoming"},
    {"first_name": "Michael", "last_name": "Bennet", "state": "Colorado"},
    {"first_name": "Marsha", "last_name": "Blackburn", "state": "Tennessee"},
#    {"first_name": "Richard", "last_name": "Blumenthal", "state": "Connecticut"},
    {"first_name": "Lisa", "last_name": "Blunt Rochester", "state": "Delaware"},
    {"first_name": "Cory", "last_name": "Booker", "state": "New Jersey"},
    {"first_name": "John", "last_name": "Boozman", "state": "Arkansas"},
    {"first_name": "Katie", "last_name": "Britt", "state": "Alabama"},
    {"first_name": "Ted", "last_name": "Budd", "state": "North Carolina"},
    {"first_name": "Maria", "last_name": "Cantwell", "state": "Washington"},
    {"first_name": "Shelley", "last_name": "Capito", "state": "West Virginia"},
    {"first_name": "William", "last_name": "Cassidy", "state": "Louisiana"},
    {"first_name": "Susan", "last_name": "Collins", "state": "Maine"},
    {"first_name": "Christopher", "last_name": "Coons", "state": "Delaware"},
    {"first_name": "John", "last_name": "Cornyn", "state": "Texas"},
    {"first_name": "Catherine", "last_name": "Cortez Masto", "state": "Nevada"},
    {"first_name": "Tom", "last_name": "Cotton", "state": "Arkansas"},
    {"first_name": "Kevin", "last_name": "Cramer", "state": "North Dakota"},
    {"first_name": "Mike", "last_name": "Crapo", "state": "Idaho"},
    {"first_name": "Rafael", "last_name": "Cruz", "state": "Texas"},
    {"first_name": "John", "last_name": "Curtis", "state": "Utah"},
    {"first_name": "Steve", "last_name": "Daines", "state": "Montana"},
    {"first_name": "Tammy", "last_name": "Duckworth", "state": "Illinois"},
    {"first_name": "Richard", "last_name": "Durbin", "state": "Illinois"},
    {"first_name": "Joni", "last_name": "Ernst", "state": "Iowa"},
    {"first_name": "John", "last_name": "Fetterman", "state": "Pennsylvania"},
    {"first_name": "Deb", "last_name": "Fischer", "state": "Nebraska"},
    {"first_name": "Ruben", "last_name": "Gallego", "state": "Arizona"},
    {"first_name": "Kirsten", "last_name": "Gillibrand", "state": "New York"},
    {"first_name": "Lindsey", "last_name": "Graham", "state": "South Carolina"},
    {"first_name": "Chuck", "last_name": "Grassley", "state": "Iowa"},
    {"first_name": "William", "last_name": "Hagerty", "state": "Tennessee"},
    {"first_name": "Maggie", "last_name": "Hassan", "state": "New Hampshire"},
    {"first_name": "Josh", "last_name": "Hawley", "state": "Missouri"},
    {"first_name": "Martin", "last_name": "Heinrich", "state": "New Mexico"},
    {"first_name": "John", "last_name": "Hickenlooper", "state": "Colorado"},
    {"first_name": "Mazie", "last_name": "Hirono", "state": "Hawaii"},
    {"first_name": "John", "last_name": "Hoeven", "state": "North Dakota"},
    {"first_name": "Jon", "last_name": "Husted", "state": "Ohio"},
    {"first_name": "Cindy", "last_name": "Hyde-Smith", "state": "Mississippi"},
    {"first_name": "Ron", "last_name": "Johnson", "state": "Wisconsin"},
    {"first_name": "James", "last_name": "Justice", "state": "West Virginia"},
    {"first_name": "Tim", "last_name": "Kaine", "state": "Virginia"},
    {"first_name": "Mark", "last_name": "Kelly", "state": "Arizona"},
    {"first_name": "John", "last_name": "Kennedy", "state": "Louisiana"},
    {"first_name": "Andy", "last_name": "Kim", "state": "New Jersey"},
    {"first_name": "Angus", "last_name": "King", "state": "Maine"},
    {"first_name": "Amy", "last_name": "Klobuchar", "state": "Minnesota"},
    {"first_name": "James", "last_name": "Lankford", "state": "Oklahoma"},
    {"first_name": "Mike", "last_name": "Lee", "state": "Utah"},
    {"first_name": "Ben Ray", "last_name": "Luján", "state": "New Mexico"},
    {"first_name": "Cynthia", "last_name": "Lummis", "state": "Wyoming"},
    {"first_name": "Edward", "last_name": "Markey", "state": "Massachusetts"},
    {"first_name": "Roger", "last_name": "Marshall", "state": "Kansas"},
    {"first_name": "Mitch", "last_name": "McConnell", "state": "Kentucky"},
    {"first_name": "David", "last_name": "McCormick", "state": "Pennsylvania"},
    {"first_name": "Jeff", "last_name": "Merkley", "state": "Oregon"},
    {"first_name": "Ashley", "last_name": "Moody", "state": "Florida"},
    {"first_name": "Jerry", "last_name": "Moran", "state": "Kansas"},
    {"first_name": "Bernie", "last_name": "Moreno", "state": "Ohio"},
    {"first_name": "Markwayne", "last_name": "Mullin", "state": "Oklahoma"},
    {"first_name": "Lisa", "last_name": "Murkowski", "state": "Alaska"},
    {"first_name": "Christopher", "last_name": "Murphy", "state": "Connecticut"},
    {"first_name": "Patty", "last_name": "Murray", "state": "Washington"},
    {"first_name": "Jon", "last_name": "Ossoff", "state": "Georgia"},
    {"first_name": "Alex", "last_name": "Padilla", "state": "California"},
    {"first_name": "Rand", "last_name": "Paul", "state": "Kentucky"},
    {"first_name": "Gary", "last_name": "Peters", "state": "Michigan"},
    {"first_name": "Jack", "last_name": "Reed", "state": "Rhode Island"},
    {"first_name": "John", "last_name": "Ricketts", "state": "Nebraska"},
    {"first_name": "James", "last_name": "Risch", "state": "Idaho"},
    {"first_name": "Jacklyn", "last_name": "Rosen", "state": "Nevada"},
    {"first_name": "Mike", "last_name": "Rounds", "state": "South Dakota"},
    {"first_name": "Bernie", "last_name": "Sanders", "state": "Vermont"},
    {"first_name": "Brian", "last_name": "Schatz", "state": "Hawaii"},
    {"first_name": "Adam", "last_name": "Schiff", "state": "California"},
    {"first_name": "Eric", "last_name": "Schmitt", "state": "Missouri"},
    {"first_name": "Charles", "last_name": "Schumer", "state": "New York"},
    {"first_name": "Rick", "last_name": "Scott", "state": "Florida"},
    {"first_name": "Tim", "last_name": "Scott", "state": "South Carolina"},
    {"first_name": "Jeanne", "last_name": "Shaheen", "state": "New Hampshire"},
    {"first_name": "Tim", "last_name": "Sheehy", "state": "Montana"},
    {"first_name": "Elissa", "last_name": "Slotkin", "state": "Michigan"},
    {"first_name": "Tina", "last_name": "Smith", "state": "Minnesota"},
    {"first_name": "Dan", "last_name": "Sullivan", "state": "Alaska"},
    {"first_name": "John", "last_name": "Thune", "state": "South Dakota"},
    {"first_name": "Thomas", "last_name": "Tillis", "state": "North Carolina"},
    {"first_name": "Thomas", "last_name": "Tuberville", "state": "Alabama"},
    {"first_name": "Chris", "last_name": "Van Hollen", "state": "Maryland"},
    {"first_name": "Mark", "last_name": "Warner", "state": "Virginia"},
    {"first_name": "Raphael", "last_name": "Warnock", "state": "Georgia"},
    {"first_name": "Elizabeth", "last_name": "Warren", "state": "Massachusetts"},
    {"first_name": "Peter", "last_name": "Welch", "state": "Vermont"},
    {"first_name": "Sheldon", "last_name": "Whitehouse", "state": "Rhode Island"},
    {"first_name": "Roger", "last_name": "Wicker", "state": "Mississippi"},
    {"first_name": "Ron", "last_name": "Wyden", "state": "Oregon"},
    {"first_name": "Todd", "last_name": "Young", "state": "Indiana"}
]

# Initialize the WebDriver (e.g., Chrome)
driver = webdriver.Chrome()  # Replace with the path to your WebDriver if needed

# Open the SFD website
driver.get("https://efdsearch.senate.gov/")
auth_checkbox = driver.find_element(By.ID, "agree_statement")
if not auth_checkbox.is_selected():
    auth_checkbox.click()

# Function to search for a senator's periodic transactions
def search_senator_transactions(first_name, last_name, state):
    try:
        # Enter the senator's first name
        first_name_input = driver.find_element(By.ID, "firstName")
        first_name_input.clear()
        first_name_input.send_keys(first_name)

        # Enter the senator's last name
        last_name_input = driver.find_element(By.ID, "lastName")
        last_name_input.clear()
        last_name_input.send_keys(last_name)

        # Check the "Senator" checkbox
        senator_checkbox = driver.find_element(By.ID, "filerTypeLabelSenator")
        if not senator_checkbox.is_selected():
            senator_checkbox.click()

        # Select the state (if needed)
        #state_dropdown = Select(driver.find_element(By.ID, "senatorFilerState"))
        #state_dropdown.select_by_visible_text(state)

        # Check the "Periodic Transactions" checkbox
        periodic_transactions_checkbox = driver.find_element(By.ID, "reportTypeLabelPtr")
        if not periodic_transactions_checkbox.is_selected():
            periodic_transactions_checkbox.click()

        # Set the date range for the last two years
        end_date = datetime.now()
        start_date = end_date - timedelta(days=730)  # 2 years ago
        start_date_str = start_date.strftime("%m/%d/%Y")
        end_date_str = end_date.strftime("%m/%d/%Y")
        print(start_date)

        # Enter the start date
        start_date_input = driver.find_element(By.ID, "fromDate")
        start_date_input.clear()
        start_date_input.send_keys(start_date_str)

        # Enter the end date
        end_date_input = driver.find_element(By.ID, "toDate")
        end_date_input.clear()
        end_date_input.send_keys(end_date_str)

        # Click the "Search Reports" button
        search_button = driver.find_element(By.XPATH, "//*[@id='searchForm']/div/button")
        search_button.click()
        time.sleep(2)  # Wait for the page to load

        # Capture the links to the periodic transaction reports (handling pagination)
        report_links = []
        while True:
            # Extract links from the current page
            results = driver.find_elements(By.XPATH, "//table[@id='filedReports']//tr")
            for result in results:
                try:
                    link = result.find_element(By.TAG_NAME, "a").get_attribute("href")
                    report_links.append(link)
                except:
                    continue

            # Check if there is a "Next" button and if it's clickable
            try:
                next_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Next')]")
                if "disabled" in next_button.get_attribute("class"):
                    break  # Exit the loop if the "Next" button is disabled
                next_button.click()
                time.sleep(3)  # Wait for the next page to load
            except:
                break  # Exit the loop if the "Next" button is not found

        return report_links

    except Exception as e:
        print(f"Error searching for {first_name} {last_name}: {e}")
        return []

# Function to extract transaction details from a report
def extract_transaction_details(report_url):
    try:
        # Open the report URL in a new tab
        driver.execute_script(f"window.open('{report_url}', '_blank');")
        driver.switch_to.window(driver.window_handles[1])  # Switch to the new tab
        time.sleep(3)  # Wait for the page to load

        # Extract transaction details
        transactions = []
        rows = driver.find_elements(By.XPATH, "//*[@id='content']/div/div/section/div/div/table/tbody/tr")
        for row in rows:
            try:
                cells = row.find_elements(By.TAG_NAME, "td")
                if len(cells) >= 8:  # Ensure there are enough columns
                    transaction_date = cells[1].text
                    owner = cells[2].text
                    ticker = cells[3].text
                    asset_name = cells[4].text
                    asset_type = cells[5].text
                    transaction_type = cells[6].text
                    amount = cells[7].text
                    comment = cells[8].text

                    transactions.append({
                        "transaction_date": transaction_date,
                        "owner": owner,
                        "ticker": ticker,
                        "asset_name": asset_name,
                        "asset_type": asset_type,
                        "transaction_type": transaction_type,
                        "amount": amount,
                        "comment": comment
                    })
  
            except:
                continue

        # Close the report tab and switch back to the main tab
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(2)

        return transactions

    except Exception as e:
        print(f"Error extracting details from {report_url}: {e}")
        return []

# Loop through all senators and search for their periodic transactions
all_transactions = []
for senator in senators:
    first_name = senator["first_name"]
    last_name = senator["last_name"]
    state = senator["state"]

    print(f"Searching for {first_name} {last_name} ({state})...")
    report_links = search_senator_transactions(first_name, last_name, state)

    # Extract transaction details from each report
    for report_link in report_links:
        print(f"Extracting details from {report_link}...")
        transactions = extract_transaction_details(report_link)
        for transaction in transactions:
            transaction.update({
                "first_name": first_name,
                "last_name": last_name,
                "state": state
            })
            all_transactions.append(transaction)

    # Go back to the search page for the next senator
    driver.get("https://efdsearch.senate.gov/")
    time.sleep(2)


# Close the WebDriver
driver.quit()

# Save the results to a CSV file
df = pd.DataFrame(all_transactions)
df.to_csv("senator_transactions_details.csv", index=False)
print("Results saved to senator_transactions_details.csv")
