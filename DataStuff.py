import pandas as pd

inputFile = 'H:/russelltest.csv'
data = pd.read_csv(inputFile)
def screen_mktCap(universe, threshold=1000, columnheader='Adj. Market Value'):
    if universe.dtypes[columnheader] in ('string','object'):
        universe[columnheader] = universe[columnheader].str.replace(
            ',', '').astype(float)

    mcExclusions = universe.copy()
    mcExclusions = mcExclusions[mcExclusions[columnheader] < threshold]
    mcExclusions.loc[:,'Fail'] = 'Market Cap Screen'
    universe.drop(mcExclusions.index, inplace=True)
    return mcExclusions

exclusions = screen_mktCap(data)
data.set_index('Symbol',inplace=True)
print(data.head())
print(exclusions.head())