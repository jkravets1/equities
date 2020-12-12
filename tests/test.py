import os ;from equities import Universe
import random

u = Universe()

k,f,s = 'bar',(10,7),True
ciks = u.ciks
random.shuffle(ciks)

for cik in u.ciks:

    c = u.company(cik)

    income = c['income']
    if not income.empty:
        income.to_csv(os.path.join('data','income'+c['name']+'.csv'))

    balance = c['balance']
    if not balance.empty:
        balance.to_csv(os.path.join('data','balance'+c['name']+'.csv'))

    cash = c['cash']
    if not cash.empty:
        cash.to_csv(os.path.join('data','cash'+c['name']+'.csv'))

    prices = c['prices']
    if not prices.empty:
        prices.to_csv(os.path.join('data','prices'+c['name']+'.csv'))
