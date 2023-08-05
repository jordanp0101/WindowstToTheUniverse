import numpy as np
from plotnine import *
import pandas as pd

# for webscraping
from bs4 import BeautifulSoup
import requests



def scrape_planets_table(url):
    """Scrapes this specific table from this html webpage,
    and transforms it into a dataframe

    Args:
        url: The URL of the webpage to scrape.

    Returns:
        returns the created dataframe made up of the html table
    """
    # Make a request to the URL and get the HTML content
    req = requests.get(url)
    content = req.text

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(content, features="lxml")

    # Find the table containing the planets' data
    table_planets = soup.find('table')
    
    # Find all the table header elements (th tags)
    table_headers = table_planets.find_all('th')

    # Create an empty list to store the extracted table headers
    tlist = []
    
    # Loop through each table header element and extract the text
    for th in table_headers:
        text = th.text  # extract only th's text
        tlist.append(text)

    # Convert the list of table headers into a numpy array
    np_tlist = np.array(tlist)

    # Reshape the numpy array into a 2D array with shape (17, 9)
    np_tlist = np_tlist.reshape((17, 9))

    # Divide the numpy array into columns, indices, and values
    # Columns: extract the first row of the numpy array as column names (excluding the first element)
    columns = np_tlist[0, 1:]
    # Indices: extract the first column of the numpy array as row indices (excluding the first element)
    index = np_tlist[1:, 0]
    # Values: extract the content/values of the table (excluding the first row and the first column)
    values = np_tlist[1:, 1:]

    # Create a DataFrame using the extracted columns, indices, and values
    # Note: df_index = pd.Index(index) is commented out and not used in this version of the code
    df_table = pd.DataFrame(columns=columns, index=index, data=values)

    # Drop any rows containing NaN (Not a Number) values from the DataFrame (inplace is not specified, so the original DataFrame is not modified)
    df_table.dropna()

    # Transpose the DataFrame, swapping rows and columns
    df_table_transposed = df_table.transpose()

    # Return the transposed DataFrame
    return df_table_transposed




if __name__ == "__main__":

    # Set the URL of the webpage to scrape
    url = "https://www.windows2universe.org/?page=/our_solar_system/planets_table.html"

    # Call the scrape_planets_table function to fetch the data and transform it into a DataFrame
    df_planets = scrape_planets_table(url)

    # Save the DataFrame as a CSV file named "solarPlanets.csv" in the "data" directory
    df_planets.to_csv("data/solarPlanets.csv")

    # Print the DataFrame to the console
    print(df_planets)




