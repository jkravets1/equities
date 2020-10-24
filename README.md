
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
    universe = Universe()

#### Essential Methods 

To get the number of companies in the universe call: 
    len(universe)

"CIK" numbers are the sec's official unique identifier for public companies. To get a full list of the cik numbers call:

    universe.ciks()

To get a dictionary mapping "cik" numbers to the names of companies execute:

    universe.ciks_to_names()

## Company Queries: 

#### Requesting Company Json Data

Company data can be accessed in data format by specifying the company's "cik" number.

    universe.Company(cik)      # full json data response (metadata and dataframes)

#### Requesting Dataframes of Financial Statements

Full XLBR pandas dataframes of a company's financial statements can be obtained by specifying the company's "cik" number and the "kind" of the statement: 

    universe.Statement(cik,"income")      # income statement dataframe

    universe.Statement(cik,"balance")     # balance sheet dataframe

    universe.Statement(cik,"cash")        # cashflow statement dataframe

    
#### Example 

I really want to demonstrate the beauty of this dataset since this is often difficult when looking
at thousands of numeric datatables. Let's take a very naive peek by plotting various statements 
as a kind of stacked timeseries. 

The following is a start to finish example of how one might plot the financial statements 
of the first five companies in the universe.

Here's how we'd implement that: 

    from equities import Universe
    import matplotlib.pyplot as plt 

    universe = Universe()

    k,f,s = 'bar',(20,10),True
    for cik in universe.ciks()[:5]:

        universe.Statement(cik,kind="income").T.plot(
            kind=k,
            figsize=f,
            stacked=s)

        universe.Statement(cik,kind="balance").T.plot(
            kind=k,
            figsize=f,
            stacked=s)

        universe.Statement(cik,kind="cash").T.plot(
            kind=k,
            figsize=f,
            stacked=s)

    plt.show()
