import pandas as pd 
from equities import logs
from polity.api import Client as PolityClient
from pytrends.request import TrendReq as GoogleTrendClient
import yfinance as YahooFinanceClient
from polity.static import EQUITIES_PUBLIC_API_KEY as API_KEY

class Universe(object):

    def __init__(self):
        try:
            logs.initialize()
            self._polity = PolityClient(api_key=API_KEY)
            self._pytrends = GoogleTrendClient(hl='en-US', tz=360)
            self.ciks = list(self._polity.cik_to_name.keys())
            self.names = list(self._polity.cik_to_name.values())
            self.tickers = list(set(self._polity.cik_to_ticker.values()))
            logs.initialized(self._polity._fetch_equities_messages(),len(self.ciks))
        except Exception as e:
            logs.failed(e)

    def __len__(self): return len(self.ciks)

    def __str__(self): return str(self._polity.name_to_cik)

    def _query_y_finance(self,cik_or_ticker):
        cik = self._convert_to_cik(cik_or_ticker)
        ticker = self._polity.cik_to_ticker[cik]
        return YahooFinanceClient.Ticker(ticker)

    def _convert_to_cik(self,cik_or_ticker):
        symbol = cik_or_ticker.lower().replace(' ','')
        if symbol in self.tickers:
            return self._polity.ticker_to_cik[symbol]
        elif str(int(cik_or_ticker)) in self.ciks:
            return str(int(cik_or_ticker))

    def _invert_dict(self,to_invert):
        return {v:k for k,v in to_invert.items()}

    def cik_to_name(self):
        labels = self._polity.cik_to_name
        return dict(zip(labels.keys(),labels.values()))

    def cik_to_ticker(self):
        labels = self._polity.cik_to_ticker
        return dict(zip(labels.keys(),labels.values()))

    def ticker_to_cik(self):
        return self._invert_dict(self.cik_to_name)

    def name_to_cik(self):
        return self._invert_dict(self.cik_to_name)

    def prices(self,cik_or_ticker):
        try:
            return self._query_y_finance(cik_or_ticker).history(period='max')
        except Exception as e:
            print(e)
            return pd.DataFrame()

    def actions(self,cik_or_ticker):
        try:
            return self._query_y_finance(cik_or_ticker).actions
        except Exception as e:
            print(e)
            return pd.DataFrame()

    def dividends(self,cik_or_ticker):
        try:
            return self._query_y_finance(cik_or_ticker).dividends
        except Exception as e:
            print(e)
            return pd.DataFrame()

    def splits(self,cik_or_ticker):
        try:
            return self._query_y_finance(cik_or_ticker).splits
        except Exception as e:
            print(e)
            return pd.DataFrame()

    def major_holders(self,cik_or_ticker):
        try:
            return self._query_y_finance(cik_or_ticker).major_holders
        except Exception as e:
            print(e)
            return pd.DataFrame()
        
    def institutional_holders(self,cik_or_ticker):
        try:
            return self._query_y_finance(cik_or_ticker).institutional_holders
        except Exception as e:
            print(e)
            return pd.DataFrame()

    def events(self,cik_or_ticker):
        try:
            return self._query_y_finance(cik_or_ticker).calendar
        except Exception as e:
            print(e)
            return pd.DataFrame()

    def recommendations(self,cik_or_ticker):
        try:
            return self._query_y_finance(cik_or_ticker).recommendations
        except Exception as e:
            print(e)
            return pd.DataFrame()

    def esg(self,cik_or_ticker):
        try:
            return self._query_y_finance(cik_or_ticker).sustainability
        except Exception as e:
            print(e)
            return pd.DataFrame()

    def financial_statement(self,cik_or_ticker,kind):
        try:
            cik = self._convert_to_cik(cik_or_ticker)
            return self._polity.financial_statement(cik,kind,df=True)
        except Exception as e:
            print(e)
            return pd.DataFrame()

    def interest(self,name):
        try:
            self._pytrends.build_payload(
                [name.replace('/','')],
                cat=0,
                timeframe='today 5-y',
                geo='',
                gprop='')
            return self._pytrends.interest_over_time()
        except Exception as e:
            print(e)
            return pd.DataFrame()

    def search(self,query):
        matches = []        
        for name in self.names:
            if query.lower() in name.lower():
                matches.append(self._polity.name_to_cik[name])
        for ticker in self.tickers:
            if query.lower() in ticker.lower():
                matches.append(self._polity.ticker_to_cik[ticker])
        for cik in self.ciks:
            if query in cik:
                matches.append(cik)
        logs.search(query,str(len(matches)))
        return {self._polity.cik_to_name[match]:match for match in matches}

    def company(self,cik_or_ticker_query,search=False):

        if search: cik = list(self.search(cik_or_ticker_query).values())[0]
        else: cik = self._convert_to_cik(cik_or_ticker_query)
        polity_data = self._polity.company(cik,df=True)
        yfinance_data = {
            'prices' : self.prices(cik),
            'actions' : self.actions(cik),
            'dividends' : self.dividends(cik),
            'splits' : self.splits(cik),
            'major_holders' : self.major_holders(cik),
            'institutional_holders': self.institutional_holders(cik),
            'events': self.events(cik),
            'recommendations': self.recommendations(cik),
            'esg': self.esg(cik),
            'interest': self.interest(polity_data['name'])
        }
        polity_data.update(yfinance_data)
        return  polity_data
