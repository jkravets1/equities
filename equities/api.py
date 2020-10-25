from polity.api import Client as PolityClient
from polity.static import EQUITIES_PUBLIC_API_KEY as API_KEY

class Universe(object):

    def __init__(self):

        def initialize():
            print('-'*40+'\n  🐋\tWelcome to equities.\n'
                +'-'*40+'\n Initializing Universe...')

        def initialized():
            print('\r> 🌌\tUniverse initialized. size: %s\n'
                %str(len(self.ciks))+' Success. You\'re good to go!\n'
                +'-'*40)

        def cik_to_name():
            labels = self._api._fetch_cik_to_name_map()
            return dict(zip(labels.keys(),labels.values()))

        def invert_dict(to_invert):
            return {v:k for k,v in to_invert.items()}

        initialize()
        self._api = PolityClient(api_key=API_KEY)
        self.cik_to_name = cik_to_name()
        self.name_to_cik = invert_dict(self.cik_to_name)
        self.ciks = list(self.cik_to_name.keys())
        self.names = list(self.cik_to_name.values())
        initialized()

    def __len__(self):
        return len(self.ciks)

    def __str__(self):
        return str(self.name_to_cik)

    def search(self,query):
        # search ciks 
        matches = []        
        for name in self.names:
            if query.lower() in name.lower():
                matches.append(self.name_to_cik[name])
        for cik in self.ciks:
            if query in cik:
                matches.append(cik)
        print('\r> 🛰️\tSearch query: "%s" found %s matches.'%(query,str(len(matches))))
        return {self.cik_to_name[match]:match for match in matches}

    def company(self,cik):
        return  self._api.company(cik,df=True)

    def financial_statement(self,cik,kind):
        return self._api.financial_statement(cik,kind,df=True)