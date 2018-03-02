import pandas as pd


def test_run():
    """Function called by Test Run."""
    df = pd.read_csv("data/AAPL.csv")
    # TODO: Print last 5 rows of the data frame
    print df.head() # top 5 line
    print df.tail() # last 5 line
    print df.tail(8)
    print df[10:21] # slicing from 10-20


if __name__ == "__main__":
    test_run()



"""Compute mean volume"""
'''

AAPL  Date      Open    High     Low   Close    Volume     Adj Close
0  2012-09-12  666.85  669.90  656.00  669.79  25410600     669.79
1  2012-09-11  665.11  670.10  656.50  660.59  17987400     660.59
2  2012-09-10  680.45  683.29  662.10  662.74  17428500     662.74
3  2012-09-07  678.05  682.48  675.77  680.44  11773800     680.44
4  2012-09-06  673.17  678.29  670.80  676.27  13971300     676.27

IBM  Date       Open    High     Low   Close   Volume     Adj Close
0  2012-09-12  203.52  204.65  202.96  203.77  3284000     203.77
1  2012-09-11  200.55  203.46  200.51  203.27  3910600     203.27
2  2012-09-10  199.39  201.82  198.73  200.95  4208000     200.95
3  2012-09-07  199.12  199.50  198.08  199.50  3413700     199.50
4  2012-09-06  196.26  199.46  196.11  199.10  3931700     199.10

'''

import pandas as pd

def get_mean_volume(symbol):
    """Return the mean volume for stock indicated by symbol.

    Note: Data for a stock is stored in file: data/<symbol>.csv
    """
    df = pd.read_csv("data/{}.csv".format(symbol))  # read in data
    #print df.head()
    # TODO: Compute and return the mean volume for this stock
    return df['Volume'].mean()  # return df['Adj Close'].max()



def test_run():
    """Function called by Test Run."""
    for symbol in ['AAPL', 'IBM']:
        print "Mean Volume"
        print symbol, get_mean_volume(symbol)


if __name__ == "__main__":
    test_run()


"""Plot High prices for IBM"""

import pandas as pd
import matplotlib.pyplot as plt

def test_run():
    df = pd.read_csv("data/IBM.csv")
    # TODO: Your code here
    df['High'].plot()
    plt.show()  # must be called to show plots

    df['Adj Close'].plot()
    plt.show()

    df[['Adj Close', 'High']].plot()
    plt.show()  # will auto add legends in the graph to differentiate both graphs


if __name__ == "__main__":
    test_run()

