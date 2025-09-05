import requests
import pandas as pd
from bs4 import BeautifulSoup
from io import StringIO

def fetch_all_mutator_weeks():
    # Get URL
    try:
        url = "https://starcraft2coop.com/resources/weeklymutations"
        response = requests.get(url)
        response.raise_for_status()

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the webpage: {e}")
        return None
    
    # Extract table from url
    try:
        soup = BeautifulSoup(response.content, "html.parser")
        table = soup.find_all('table', id="mutationCycle")
        df = pd.read_html(StringIO(str(table)))[0]
    except Exception as e:
        print(f"Error parsing the HTML or reading the table: {e}")
        return e
    
    # Remove empty rows from table
    try:
        df = df.dropna(how="all")
        return df
    except Exception as e:
        print(f"Error cleaning or processing the DataFrame: {e}")
        return None

# Get table
mutators_df = fetch_all_mutator_weeks()

if mutators_df is not None:
    print("Successfully extracted the table!")
    # delete sixth column
    mutators_df = mutators_df.drop(mutators_df.columns[5], axis=1)
    # copy last character from first column into new 5th column
    mutators_df['Brutal+ Level'] = mutators_df['Name'].apply(lambda x: x.str[-1])
    # make adjustments to name column to remove last character and copy it over to 5th column
    mutators_df['Name'] = mutators_df['Name'].apply(lambda x: x.str[:-1])
    # delete second column
    mutators_df = mutators_df.drop(mutators_df.columns[1], axis=1)
    print(mutators_df)
    # save as csv
    file_name = "mutation_weeks"
    mutators_df.to_csv(f"{file_name}.csv", index=False)
    print(f"\nData saved to '{file_name}.csv'.")
else:
    print("Failed to extract the table.")