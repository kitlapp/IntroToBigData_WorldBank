import chardet  # For encoding detection
import re  # For regular expressions used in cleaning
import pandas as pd  # For creating the DataFrame


def detect_encoding(filepath):
    """
    Detect the file's encoding using chardet.
    Reads the file in binary mode (bytes), because chardet works on raw bytes.
    """
    # Open the file in binary mode to read raw bytes ('rb')
    with open(filepath, 'rb') as file:
        data_bytes = file.read()  # Read the entire file into memory
        # Detect encoding using chardet
        result = chardet.detect(data_bytes)  # The result is a dictionary

    # Extract the encoding name and confidence level from chardet's result
    encoding = result['encoding']
    return encoding


def explore_csv(filepath, encoding, line_number):
    """
    Print a single line from the file for quick inspection.
    Useful when checking how messy a CSV line is.
    """
    with open(filepath, 'r', encoding=encoding) as file:
        exploration = file.readlines()[line_number]
        return exploration


def clean_csv(filepath, encoding, separator, trail1=None, trail2=None, trail3=None, to_be_replaced=None, start_row=0):
    """
    Clean a messy CSV by:
     - removing specified characters if given (like quotes)
     - removing trailing characters (like newline)
     - replacing ', ' with a space (avoids wrong splitting)

    Parameters:
    - filepath: path of the file
    - encoding: encoding detected by chardet or provided manually
    - separator: the character used to split columns
    - to_be_replaced (str or None, default None): string to remove from each line
    - rstrip (str, default '\n'): characters to strip from the end of each line
    - start_row (int, default 0): skip this number of initial lines (metadata)

    Returns:
    - A pandas DataFrame created from the manually cleaned and split data.
    """
    with open(filepath, 'r', encoding=encoding) as file:
        lines = file.readlines()[start_row:]

    cleaned_list = []
    for line in lines:
        line = line.rstrip(trail1)  # Remove trailing characters
        line = line.rstrip(trail2)  # Remove trailing characters
        line = line.rstrip(trail3)  # Remove trailing characters
        if to_be_replaced:  # Only replace if a string is provided
            line = line.replace(to_be_replaced, '')
        line = re.sub(', ', ' ', line)  # Replace comma+space with space
        data = line.split(separator)  # SPlit based on the delimiter
        # Strip each value, and replace empty results with None
        data = [val.strip() if val.strip() != '' else None for val in data]
        cleaned_list.append(data)

    df = pd.DataFrame(data=cleaned_list[1:], columns=cleaned_list[0])
    return df


import pandas as pd

import pandas as pd


def calculate_nans_fixed_variables(all_dfs):
    """
    Calculate NaNs for the 8 fixed DataFrames and assign them directly to variables inside the function.

    Parameters:
    - all_dfs: list of 8 pandas DataFrames in the standard order:
        0: Current health expenditure (% of GDP)
        1: People using basic drinking water services, rural (%)
        2: People using basic drinking water services, urban (%)
        3: People using safely managed sanitation services, rural (%)
        4: People using safely managed sanitation services, urban (%)
        5: Total greenhouse gas emissions including LULUCF (Mt CO2e)
        6: Population, total
        7: Renewable energy consumption (% of total final energy consumption)

    Returns:
    - tuple of 8 DataFrames corresponding to the indicators in the same order
    """
    # Calculate NaNs for all DataFrames
    df_nans = []
    for df in all_dfs:
        data = df.isna().sum().values.reshape(1, len(df.columns))
        df_nan = pd.DataFrame(data=data, columns=df.columns)
        df_nans.append(df_nan)

    # Assign each DataFrame to a descriptive variable
    df_che_nans = df_nans[0]
    df_wr_nans = df_nans[1]
    df_wu_nans = df_nans[2]
    df_sr_nans = df_nans[3]
    df_su_nans = df_nans[4]
    df_gem_nans = df_nans[5]
    df_pop_nans = df_nans[6]
    df_ren_nans = df_nans[7]

    # Return all variables as a tuple
    return df_che_nans, df_wr_nans, df_wu_nans, df_sr_nans, df_su_nans, df_gem_nans, df_pop_nans, df_ren_nans


