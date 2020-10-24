from polity.api import Client

class Universe(object):

    def __init__(self):
        self.api = Client()

    def __len__(self):
        return len(self.ciks())

    def ciks_to_names(self):
        return self.api._fetch_cik_to_name_map()

    def ciks(self):
        return self.api.companies()

    def search(self,query):
        def invert_dict(to_invert):
            return {v.lower():k.lower() for k,v in to_invert.items()}
        name_to_cik = invert_dict(self.api._fetch_cik_to_name_map())
        matches = [name for name in name_to_cik.keys() if name in query.lower()]
        return name_to_cik.map(matches)

    def Company(self,cik):
        return self.api.company(cik)

    def Statement(self,cik,kind):
        return self.api.financial_statement(
            cik,kind,df=True)



