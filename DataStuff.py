import pandas as pd
import pyfire

inputFile = 'H:/russelltest.csv'
outputFile = 'H:/screeneduniverse.csv'
data = pd.read_csv(inputFile)
def screen_mktCap(universe, threshold=1000, columnheader='Adj. Market Value'):
    """Screens a dataframe of holdings to exclude those with market cap below a given threshold. 
    Arguments: 
    universe -  a dataframe with holding identifiers in a column named Symbol.
    threshold - integer specifying the minimum market value to screen below. 
    columnheader - string specifying the column name with market values.
    """
    if universe.dtypes[columnheader] in ('string','object'):
        universe[columnheader] = universe[columnheader].str.replace(
            ',', '').astype(float)

    mcExclusions = universe.copy()
    mcExclusions = mcExclusions[mcExclusions[columnheader] < threshold]
    mcExclusions.loc[:,'Fail'] = 'Market Cap Screen'
    universe.drop(mcExclusions.index, inplace=True)
    return mcExclusions

def screen_divPayers(universe):
    """Screens a dataframe of holdings to exclude those with no trailing or indicated dividend yield
    Arguments: 
    universe -  a dataframe with holding identifiers in a column named Symbol.
    """
    divExclusions = universe.copy()
    return divExclusions

exclusions = screen_mktCap(data)
data.set_index('Symbol',inplace=True)
print(data.head())
print(exclusions.head())
data.to_csv(outputFile)