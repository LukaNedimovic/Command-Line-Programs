''' 
To run:
python covidcases.py {country name}

Example:
python covidcases.py Bosnia
'''


import sys      # Used to get arguments from command line
import requests # Used to fetch data from API 

class colors:          # Colors for printing - self-explanatory
    RED   = '\033[91m' 
    GREEN = '\033[92m'
    WHITE = '\033[0m'

'''
Function used for printing information
[Arguments]:
    [keys]: list of wanted information to print
    [data]: dictionary with all the data fetched from API 
'''
def log_keys(keys, data): 
    max_len = 0 # Maximum length of key - will be used for space offset later 
    for key in keys:
        max_len = max(len(key), max_len)

    for key in keys:
        offset     = max_len - len(key) # Offset is dependent on key length 
        offset_str = ' ' * offset       # Making offset string

        value = data[key] # Value of certain key
        if isinstance(value, int): # In case value is an integer - separate it 
            print(f'{colors.RED}[ {key} ]: {offset_str}{colors.GREEN}{value:,}')            
        else:                      # In any other case, print it as a string
            print(f'{colors.RED}[ {key} ]: {offset_str}{colors.GREEN}{str(value)}')
            
    print(f'{colors.WHITE}', end='') # Resetting the color to white


if __name__ == '__main__':
    args     = sys.argv     # Getting the arguments from command line
    country  = str(args[1]) # The first and the only argument is country name

    url  = f'https://disease.sh/v3/covid-19/countries/{country}' # country URL
    data = requests.get(url).json() # Getting the JSON data
    # Keys is a list of information you wish to see - feel free to modify it
    keys = ['country', 'cases', 'active', 'recovered', 'deaths', 'tests'] 

    log_keys(keys, data) # Logging the specific keys 