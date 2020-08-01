from equities.src.Universe import Universe
from equities.src.Company  import Company

def test():

    import matplotlib.pyplot as plt 

    u = Universe()
    
    k,f,s = 'bar',(13,8),True
    for cik in u.ciks()[:5]:

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

