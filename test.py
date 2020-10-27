from equities import Universe
import matplotlib.pyplot as plt 

u = Universe()

k,f,s = 'bar',(10,7),True
for cik in u.ciks[:5]:

    c = u.company(cik)

    income = c['income']
    if not income.empty:
        income.T.plot(
        kind=k,
        figsize=f,
        stacked=s)

    balance = c['balance']
    if not balance.empty:
        balance.T.plot(
        kind=k,
        figsize=f,
        stacked=s) 

    cash = c['cash']
    if not cash.empty:
        cash.T.plot(
        kind=k,
        figsize=f,
        stacked=s)

    prices = c['prices']
    if not prices.empty:
        prices.drop('Volume',axis=1).plot(
            kind='line',
            figsize=f)

plt.show()