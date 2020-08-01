import os 
from io import BytesIO
from zipfile import ZipFile
import requests
import threading
import shutil
import time

from alive_progress import alive_bar
import pandas as pd

bucket_name = 'equities-bucket'
bucket_uri = 'https://storage.googleapis.com/' \
    + bucket_name + '/'

file_dir = os.path.dirname(os.path.realpath(__file__))
data_dir = os.path.join(file_dir,'data')

financial_data_dir = os.path.join(
    data_dir,
    'package',
    'home',
    'ljwcharles',
    'equities-compute',
    'streamer',
    'equities',
    'data'
)

meta_data_dir = os.path.join(
    data_dir,
    'package',
    'equities',
    'lib',
    'pull'
)

class Universe(object):

    def __init__(self,auto_build=True):
        if len(self) == 0:
            print(" > 🗑️  ( empty equities universe ) - [local storage disconnected]")
            if auto_build:
                print(" > 🦀 ( autobuilder started )")
                self.build_storage()
                self = self.__init__(auto_build=False)
        else:
            print(" > 🐋 ( equities universe ) - [local storage connected]")

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

        print(" > 📦 ( downloading sec packages )\t")
        response = requests.get(bucket_uri + 'package.zip')

        print(" > 🏭 ( parsing structs )\t")
        with ZipFile(BytesIO(response.content)) as zip_file:
            zip_file.extractall(
                os.path.join(data_dir,'package')
                )

        print(" > ✨ ( built local storage )\t")
        
    def purge_storage(self):
        try:
            shutil.rmtree(os.path.join(data_dir,'package'))
            print(' > 💀 ( equities universe purged ) - [storage deleted]\t')
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


def test():

    import matplotlib.pyplot as plt

    u = Universe()
    u.build()
    
    k,f,s = 'bar',(20,10),True
    for cik in u.ciks()[:3]:

        u[cik].income().T.plot(
            kind=k,
            figsize=f,
            stacked=s)

        u[cik].cash().T.plot(
            kind=k,
            figsize=f,
            stacked=s)

        u[cik].balance().T.plot(
            kind=k,
            figsize=f,
            stacked=s)

    plt.show()