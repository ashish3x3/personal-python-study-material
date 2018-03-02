

# US NYSE works 252 days in a year..

''' Building a dataframe in pandas   '''

import pandas as pd

def test_run():
	start_data = '2010-01-22'
	end_date = '2010-01-26'
	dates = pd.date_range(start_data,end_date)
	df1 = pd.DataFrame(index=dates)  # without this by default index are 0,1,2,etc

	#  read SPY matching data in date range into temprory dataframe
	''' this won't work as the index is different in df1. so we have to pass which column we want to work as index. alsowe want to parse date as datetime present in csv bcz index=dates converts date t datetime..and we want the ndex to match. Inc sv only date is present and not datetime..

	#dfSPY = pd.read_csv("data/SPY.csv")
	'''
	dfSPY = pd.read_csv("data/SPY.csv", index_col="Date", parse_dates = True, usecols=['Date','Adj CLose'], na_values=['nan'])

	dfSPY = dfSPY.rename(columns={'Adj Close': 'SPY'})

	#join the two dataframe using Dataframe.join()
	df1 =df1.join(dfSPY, how='inner')  # only match if present in both.. leftjoin... inner join

	# read in more stocks
	symbols = ['GOOG', 'IBM', 'GLD']
	for symbol in symbols:
		df_temp = pd.read_csv("data/{}.csv".format(symbol), index_col="Date", parse_dates = True, usecols=['Date','Adj CLose'], na_values=['nan'])

		# rename column to prevent clash
		df_temp = df_temp.rename(columns={'Adj Close':symbol})
		df1 = df1.join(df_temp)  # use default how=left

	# Drop NaN Values
	df1 = df1.dropna()
	print df1


if __name__ == "__main__":
	test_run()




'''
               SPY    GOOG     IBM     GLD
2010-01-22  104.34  550.01  119.61  107.17
2010-01-25  104.87  540.00  120.20  107.48
2010-01-26  104.43  542.42  119.85  107.56
'''

"""Utility functions"""

import os
import pandas as pd

def symbol_to_path(symbol, base_dir="data"):
    """Return CSV file path given ticker symbol."""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))


def get_data(symbols, dates):
    """Read stock data (adjusted close) for given symbols from CSV files."""
    df = pd.DataFrame(index=dates)
    if 'SPY' not in symbols:  # add SPY for reference, if absent
        symbols.insert(0, 'SPY')

    for symbol in symbols:
        # TODO: Read and join data for each symbol
        dfTemp = pd.read_csv(symbol_to_path(symbol), index_col="Date", parse_dates = True, usecols=['Date','Adj Close'], na_values=['nan'])
        dfTemp = dfTemp.rename(columns={'Adj Close':symbol})
        df = df.join(dfTemp, how='left')
        #df = df.dropna()
        # dropping of the nan from SPY as we are using it as a reference
        if symbol == 'SPY': # drop dates spy did not trade
        	df =df.dropna(subset=["SPY"])  # this ill ensure only those rows where SPY is None si dropped. Alo this enssure there is no NaN is SPY columns

    return df


def test_run():
    # Define a date range
    dates = pd.date_range('2010-01-22', '2010-01-26')

    # Choose stock symbols to read
    symbols = ['GOOG', 'IBM', 'GLD']

    # Get stock data
    df = get_data(symbols, dates)
    print df


if __name__ == "__main__":
    test_run()





"Slicing in DF ... row slicing and column slicing "

print df.ix['2010-01-01': '2010-01-31']  # the month of january..ROW slicing..will return all column in rows
print df['2010-01-01': '2010-01-31'] #...same as row slicing

# if you pass dates in reverese chronological order, pandas will return empty date frame

print df['IBM', 'GOOG']  # COLUMN SLICING...all rows with only these columns

print df.ix['2010-01-01':'2010-01-31', ['IBM', 'GOOG']]  # mix of both..only thse 2 column in all retuned rows


"""Slice and plot"""

import os
import pandas as pd
import matplotlib.pyplot as plt


def plot_selected(df, columns, start_index, end_index):
    """Plot the desired columns over index values in the given range."""
    # TODO: Your code here
    # Note: DO NOT modify anything else!
    df = df.ix[start_index:end_index, columns]
    plot_data(df)


def symbol_to_path(symbol, base_dir="data"):
    """Return CSV file path given ticker symbol."""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))


def get_data(symbols, dates):
    """Read stock data (adjusted close) for given symbols from CSV files."""
    df = pd.DataFrame(index=dates)
    if 'SPY' not in symbols:  # add SPY for reference, if absent
        symbols.insert(0, 'SPY')

    for symbol in symbols:
        df_temp = pd.read_csv(symbol_to_path(symbol), index_col='Date',
                parse_dates=True, usecols=['Date', 'Adj Close'], na_values=['nan'])
        df_temp = df_temp.rename(columns={'Adj Close': symbol})
        df = df.join(df_temp)
        if symbol == 'SPY':  # drop dates SPY did not trade
            df = df.dropna(subset=["SPY"])

    return df

# normalizing.. so that all graph start from one point
# wedivide by row1
def normalize_data(df):
	""" Normaloze stock price using the first row of the dataframe """
	return df/df.ix[0,:]  # df.ix[0,:] returns first row


def plot_data(df, title="Stock prices"):
    """Plot stock prices with a custom title and meaningful axis labels."""
    ax = df.plot(title=title, fontsize=12)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.show()


def test_run():
    # Define a date range
    dates = pd.date_range('2010-01-01', '2010-12-31')

    # Choose stock symbols to read
    symbols = ['GOOG', 'IBM', 'GLD']  # SPY will be added in get_data()

    # Get stock data
    df = get_data(symbols, dates)

    # Slice and plot
    plot_selected(df, ['SPY', 'IBM'], '2010-03-01', '2010-04-01')


if __name__ == "__main__":
    test_run()
