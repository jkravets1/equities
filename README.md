
# 🐋 equities 

## Overview: 

    equities allows for easy access to the SEC's XBRL Financial Statement Dataset
    Parsed data is stored locally and served to the user in pandas dataframes

###### The Dataset: 

https://www.sec.gov/dera/data/financial-statement-data-sets.html

## Install: 

    pip3 install equities

## Donate: 

Consider donating bitcoin to fund the future development of this project. 

    bitcoin wallet address: 3LU5MEaAXRJoCo6vx67g1Jj7qDFRKhMs5t

## TUTORIAL: 

#### Instantiating a Universe

We begin by initializing our universe and downloading our sec data packages.

    from equities import Universe
    u = Universe()

#### Essential Methods 

To get the number of companies in the universe call: 
    len(u)

"CIK" numbers are the sec's official unique identifier for public companies. To get a full list of the cik numbers call:

    u.ciks()

## Company Queries: 

#### Accessing Company 

Dataframes of the company's financial statements over the universe in question is given by: 

    c.income()      # income statement dataframe

    c.balance()     # Balancesheet dataframe

    c.cash()        # Cash Flow Statement dataframe

    c.equity()      # Consolidated Equity dataframe

#### Accessing the Financial Statements

Dataframes of the company's financial statements over the universe in question is given by: 

    c.income()      # income statement dataframe

    c.balance()     # Balancesheet dataframe

    c.cash()        # Cash Flow Statement dataframe

    c.equity()      # Consolidated Equity dataframe


#### Additional Company Details 

To get the XBRL metadata for a given company as a pandas series call: 

    c.properties()
    
#### Example 

I really want to demonstrate the beauty of this dataset since this is often difficult when looking
at thousands of numeric datatables. Let's take a very naive peek by plotting various statements 
as a kind of stacked timeseries. 

The following is a start to finish example of how one might plot the financial statements 
of the first five companies in the universe.

Here's how we'd implement that: 

    import pandas as pd
    from equities import Universe
    import matplotlib.pyplot as plt

    u = Universe()
    
    k,f,s = 'bar',(20,10),True
    for cik in u.ciks()[:5]:

        u.Statement().income().T.plot(
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
