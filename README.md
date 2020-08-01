
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

The library consists of two central objects, Universe and Company. 

## Universe: 

#### Building the Universe

We begin by initializing our universe and downloading our sec data packages.

    from equities import Universe
    u = Universe()

#### Essential Methods 

To get the number of companies in the universe call: 
    len(u)

To get a dataframe of XBRL metadata from of all companies in the universe call: 

    u.properties()

"CIK" numbers are the sec's official unique identifier for public companies. To get a full list of the cik numbers call:

    u.ciks()

#### Accessing Companies

Universe objects are indexable by "CIK" integers. As an example, to access the first company in the universe call: 

    first_cik = universe.ciks()[0]
    u[first_cik] # This returns an Company object.

## Company: 

A Company object should be thought of as an abstract representation of a real company. Every 
company must have an associated Universe of origin. 

    from equities import Company

#### Accessing the Financial Statements

Consider the first Company in our universe, universe[u.ciks()[0]]. It is a Company object. 

    c = u[u.ciks()[0]]

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
of the first three companies in the universe.

To perform this experiment, run the following: 

    from equities import test
    test()

Here is the code that this function executes: 

    import pandas as pd
    from equities import Universe, Company
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
