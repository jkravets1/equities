import os 
import pandas as pd
from io import BytesIO
from zipfile import ZipFile
import requests
import shutil
import time

from equities.src.Company import Company

from equities.include.logs import *
from equities.include.dirs import *
from equities.include.buckets import *


class Universe(object):

    def __init__(self,auto_build=True):
        if len(self) == 0:
            log_empty()
            if auto_build:
                log_auto()
                self.build_storage()
                self = self.__init__(auto_build=False)
        else:
            log_full()

    def __len__(self):
        return len(self.ciks())

    def __getitem__(self,key):
        return Company(
            cik=key
        )

    def ciks(self):
        try:
            return os.listdir(
                os.path.join(
                    financial_data_dir,
                    'clean'
                )
            )
        except:
            return []

    def properties(self):
        return pd.read_json(
            os.path.join(meta_data_dir,'properties.json')
            )

    def manifest(self):
        return pd.read_json(
            os.path.join(meta_data_dir,'manifest.json')
            ).T.drop(['prices','dividends'])

    def build_storage(self):
        log_download()
        response = requests.get(bucket_uri + 'package.zip')
        log_parse()
        with ZipFile(BytesIO(response.content)) as zip_file:
            zip_file.extractall(
                os.path.join(data_dir,'package')
                )
        log_built()

    def purge_storage(self):
        try:
            shutil.rmtree(os.path.join(data_dir,'package'))
            log_purge()
            self = self.__init__(auto_build=False)
        except:
            pass

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