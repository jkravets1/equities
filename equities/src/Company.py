import os 
import pandas 

from equities.include.dirs import *

class Company(object):

    def __init__(self,cik):
        self.cik = cik

    def _getsheet(self,cik,sheet):
        cik_path = os.path.join(
            financial_data_dir,
            'clean',
            cik,
            sheet+'.csv'
        )
        return pd.read_csv(
            cik_path,
            index_col=0
        )

    def income(self):
        return self._getsheet(
            cik=self.cik,
            sheet='IS'
        )

    def cash(self):
        return self._getsheet(
            cik=self.cik,
            sheet='CF'
        )

    def balance(self):
        return self._getsheet(
            cik=self.cik,
            sheet='BS'
        )

    def properties(self):
        return pd.read_json(
            os.path.join(meta_data_dir,'properties.json')
            )[int(self.cik)]