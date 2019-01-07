import constants
import logging
import numpy as np
import pandas as pd

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


def read_watchlist():
    watchlist_df = pd.read_csv(constants.STOCK_WATCHLIST, index_col=0)
    return watchlist_df


def load_price_data(stock_code):
    stock_price_file = constants.STOCK_DATA + str(stock_code) + '.csv'
    price_data = pd.read_csv(stock_price_file, index_col=0, parse_dates=True,
                             usecols=[u'Date', u'Open Price', u'High Price', u'Low Price', u'Close Price'],
                             dtype={u'Open Price': np.float64, u'High Price': np.float64,
                                    u'Low Price': np.float64, u'Close Price': np.float64}).sort_index()
    return price_data


def detect_hammer(stock_code, stock_name, price_data):
    pass

def detect_events(stock_code, stock_name, price_data):
    detect_hammer(stock_code, stock_name, price_data)


def read_last_analysis_date():
    update_tracker_df = pd.read_csv(constants.STOCK_UPDATE_TRACKER, index_col=0,
                                    parse_dates=True)
    tracker_dict = update_tracker_df['updated_date'].to_dict()
    return tracker_dict


def detect_events_on_watchlist():
    watchlist_df = read_watchlist()
    logging.debug('watchlist loaded : %s' % watchlist_df)
    last_analysis_dict = read_last_analysis_date()
    logging.debug('last_analysis_date : %s' % last_analysis_dict)

    for stock_code, row in watchlist_df.iterrows():
        stock_name = row['stock_name']
        logging.debug('analysing %s...' % stock_name)
        price_data = load_price_data(stock_code)
        logging.debug('%s : price data loaded...' % stock_name)
        events = detect_events(stock_code, stock_name, price_data)
        break
        #log_events(events)


if __name__ == '__main__':
    detect_events_on_watchlist()
