# 🐋 equities 
=====================================

democratizing u.s. public company data

## Overview: 

**equities** is a highly intuive package for accessing high fidelity public company financial data. 
    
**equities** takes the approach of composing already existing stable and highly maintained libraries and apis. 

All data is served back to the user as dictionary objects or **pandas** dataframes. 

###### Data Sources: 

    Financial Statements:
    Sec Xbrl Financial Statement Data:
        - https://www.sec.gov/dera/data/financial-statement-data-sets.html

    Prices, Recommendations, Major Holders, etc.. Data
    Yfinance Pypi Package
        - https://pypi.org/project/yfinance/

## Install: 

    pip3 install equities

## TUTORIAL: 

#### Instantiating a Universe

We begin by initializing a universe client.

    from equities import Universe
    u = Universe()

The results of initializing should look something like this: 

    ----------------------------------------
    🐋	Welcome to equities.
    ----------------------------------------
    Initializing Universe...
    > 🏛️	Welcome to polity.
    > ✨	Auth success. apis connected.
    > 🌌	Universe initialized. size: 7896
    Success. You're good to go!
    ----------------------------------------


#### Essential Methods 

To get the number of companies in the universe call: 

    len(u)

"CIK" numbers are the sec's official unique identifier for public companies. A full list of the cik numbers in the universe is found in:

    u.ciks

Similarly, if we want the names of companies in the universe we can call: 

    u.names

Finally, to get tickers we call:

    u.tickers

To get a dictionary mapping "cik" numbers to the names of companies execute:

    u.cik_to_name()

We can get get a map of cik numbers to tickers through :

    u.cik_to_ticker()


The inverses of both of these dictionaries are also accessible through u.name_to_cik() and u.ticker_to_cik()

## Search: 

You can search for companies by names, ticker or ciks by using the search function. Note that in all universe queries handle for case and whitespace.

    u.search("netflix")

Here are the results of this query.

    > 🛰️     Search query: "netflix" found 1 matches.
    {'NETFLIX INC': '1065280'}

Let's find the ticker of this company. 

    u.cik_to_ticker()['1065280']

Here are results:

    'nflx'

## Queries: 

#### Company 

company data can be obtained by passing a "cik" or "ticker" into the "company()" function on the universe. 
    
    u.company('nflx')
    
    # we can also pass in a query like this: u.company("Netflix",search=True). 
    # It returns the first result of the search query. 

Here is the sample output of the above request. It is a dictionary. Here are it's keys: 

    dict_keys(['name', 'sic', 'business_address', 'mailing_address', 'phone', 'country_incorporated', 'state_incorporated', 'ein', 'former_name', 'income', 'balance', 'cash', 'equity', 'prices', 'actions', 'dividends', 'splits', 'major_holders', 'institutional_holders', 'events', 'recommendations', 'esg'])

 Observe that the keys, "income","balance","cash","equity" are dataframes and encode the income statement, balance sheet, cashflow statement and equity statement respectively of the company in question. Other keys also map to dataframes for example prices and institutional holders. this naming convention and structure is chosen for simplicity. 

    > 📦    Fetching company: 1065280 ...
    {'name': 'NETFLIX INC', 'sic': '7841.0', 'business_address': {'country': 'US', 'city': 'LOS GATOS', 'zip': '95032', 'adr1': '100 WINCHESTER CIRCLE', 'adr2': '.'}, 'mailing_address': {'country': 'US', 'city': 'LOS GATOS', 'zip': '95032-7606', 'adr1': '100 WINCHESTER CIRCLE', 'adr2': 'nan', 'state': 'CA'}, 'phone': '408-540-3700', 'country_incorporated': 'US', 'state_incorporated': 'DE', 'ein': '770467272.0', 'former_name': 'NETFLIX COM INC', 'income':                                                    2009q2 2009q3 2009q4 2010q1  ...        2019q3        2019q4        2020q2        2020q3
    Revenues                                             None   None   None   None  ...  3.907270e+09  3.999374e+09  5.767691e+09  6.148286e+09
    CostOfRevenue                                        None   None   None   None  ...  5.876271e+09  8.974190e+09  2.870614e+09  3.643707e+09
    MarketingExpense                                     None   None   None   None  ...  5.920070e+08  5.103300e+08  5.038300e+08  1.219728e+09
    ResearchAndDevelopmentExpense                        None   None   None   None  ...  5.814050e+08  8.900250e+08  4.538170e+08  3.832330e+08
    GeneralAndAdministrativeExpense                      None   None   None   None  ...  1.515240e+08  1.686280e+08  2.520870e+08  2.246570e+08
    OperatingIncomeLoss                                  None   None   None   None  ...  4.622130e+08  4.806680e+08  4.590840e+08  7.064190e+08
    InterestExpense                                      None   None   None   None  ...  2.875620e+08  4.482220e+08  1.355290e+08  1.891510e+08
    NonoperatingIncomeExpense                            None   None   None   None  ...  6.802800e+07  7.004000e+06  2.169700e+07  2.263400e+07
    IncomeLossFromContinuingOperationsBeforeIncomeT...   None   None   None   None  ...  7.282520e+08  1.107062e+09  7.958700e+08  9.005750e+08
    IncomeTaxExpenseBenefit                              None   None   None   None  ...  4.428700e+07  6.329520e+08  8.680300e+07  3.154060e+08
    NetIncomeLoss                                        None   None   None   None  ...  3.843490e+08  4.028350e+08  3.440520e+08  2.706500e+08
    EarningsPerShareBasic                                None   None   None   None  ...  8.800000e-01  9.200000e-01  7.900000e-01  6.200000e-01
    EarningsPerShareDiluted                              None   None   None   None  ...  1.360000e+00  2.830000e+00  7.600000e-01  1.360000e+00
    WeightedAverageNumberOfSharesOutstandingBasic        None   None   None   None  ...  4.375870e+08  4.380900e+08  4.369470e+08  4.375870e+08
    WeightedAverageNumberOfDilutedSharesOutstanding      None   None   None   None  ...  4.520630e+08  4.518960e+08  4.519220e+08  4.520630e+08
    GainsLossesOnExtinguishmentOfDebt                    None   None   None   None  ...           NaN           NaN           NaN           NaN
    OtherNonoperatingIncome                              None   None   None   None  ...           NaN           NaN           NaN           NaN
    CostOfGoodsSoldSubscription                          None   None   None   None  ...           NaN           NaN           NaN           NaN
    FulfillmentExpense                                   None   None   None   None  ...           NaN           NaN           NaN           NaN
    GrossProfit                                          None   None   None   None  ...           NaN           NaN           NaN           NaN
    OperatingExpenses                                    None   None   None   None  ...           NaN           NaN           NaN           NaN
    TechnologyandDevelopmentExpense                      None   None   None   None  ...           NaN           NaN           NaN           NaN

    [22 rows x 44 columns], 'balance':                                                 2009q2 2009q3 2009q4 2010q1  ...        2019q3        2019q4        2020q2        2020q3
    CommonStockParOrStatedValuePerShare               None   None   None   None  ...  1.000000e-03  1.000000e-03  1.000000e-03  1.000000e-03
    CommonStockSharesAuthorized                       None   None   None   None  ...  4.990000e+09  4.990000e+09  4.990000e+09  4.990000e+09
    CommonStockSharesIssued                           None   None   None   None  ...  4.378349e+08  4.382513e+08  4.397806e+08  4.410154e+08
    CashAndCashEquivalentsAtCarryingValue             None   None   None   None  ...  3.794483e+09  3.794483e+09  5.151884e+09  7.153248e+09
    AvailableForSaleSecuritiesCurrent                 None   None   None   None  ...           NaN           NaN           NaN           NaN
    CommonStockSharesOutstanding                      None   None   None   None  ...  4.365986e+08  4.382513e+08  4.397806e+08  4.388066e+08
    ContentAssetsNetCurrent                           None   None   None   None  ...           NaN           NaN           NaN           NaN
    OtherAssetsCurrent                                None   None   None   None  ...  7.484660e+08  7.484660e+08  1.295897e+09  1.160067e+09
    AssetsCurrent                                     None   None   None   None  ...  9.694135e+09  9.694135e+09  6.178504e+09  8.564139e+09
    ContentAssetsNetNoncurrent                        None   None   None   None  ...           NaN  2.323499e+10  2.526689e+10  2.515512e+10
    PropertyPlantAndEquipmentNet                      None   None   None   None  ...  4.182810e+08  4.819920e+08  5.652210e+08  7.519410e+08
    OtherAssetsNoncurrent                             None   None   None   None  ...  1.896043e+09  9.010300e+08  2.727420e+09  2.727420e+09
    Assets                                            None   None   None   None  ...  3.017134e+10  3.094171e+10  3.505991e+10  3.717528e+10
    ContentLiabilitiesCurrent                         None   None   None   None  ...           NaN  4.860542e+09  4.413561e+09  4.664733e+09
    AccountsPayableCurrent                            None   None   None   None  ...  4.421940e+08  5.629850e+08  6.743470e+08  6.743470e+08
    AccruedLiabilitiesCurrent                         None   None   None   None  ...  4.774170e+08  1.037723e+09  8.430430e+08  9.865950e+08
    DeferredRevenueCurrent                            None   None   None   None  ...           NaN           NaN           NaN           NaN
    LiabilitiesCurrent                                None   None   None   None  ...  6.487320e+09  7.257900e+09  6.855696e+09  6.855696e+09
    ContentLiabilitiesNoncurrent                      None   None   None   None  ...           NaN  3.759026e+09  3.206051e+09  3.208164e+09
    LongTermDebtNoncurrent                            None   None   None   None  ...  1.036006e+10  1.036006e+10  1.475926e+10  1.475926e+10
    OtherLiabilitiesNoncurrent                        None   None   None   None  ...  1.292310e+08  1.292310e+08  1.444276e+09  1.710948e+09
    Liabilities                                       None   None   None   None  ...  2.073564e+10  2.408021e+10  2.665062e+10  2.639356e+10
    CommitmentsAndContingencies                       None   None   None   None  ...           NaN           NaN           NaN           NaN
    CommonStockValue                                  None   None   None   None  ...  2.315988e+09  2.315988e+09  2.793929e+09  2.793929e+09
    AccumulatedOtherComprehensiveIncomeLossNetOfTax   None   None   None   None  ... -1.958200e+07 -1.958200e+07 -2.352100e+07 -3.407200e+07
    RetainedEarningsAccumulatedDeficit                None   None   None   None  ...  2.942359e+09  4.224779e+09  5.520816e+09  4.811749e+09
    StockholdersEquity                                None   None   None   None  ...  3.581956e+09  3.581956e+09  5.703058e+09  7.582157e+09
    LiabilitiesAndStockholdersEquity                  None   None   None   None  ...  2.597440e+10  2.597440e+10  3.505991e+10  3.717528e+10
    PreferredStockParOrStatedValuePerShare            None   None   None   None  ...           NaN           NaN           NaN           NaN
    PreferredStockSharesAuthorized                    None   None   None   None  ...           NaN           NaN           NaN           NaN
    PreferredStockSharesIssued                        None   None   None   None  ...           NaN           NaN           NaN           NaN
    PreferredStockSharesOutstanding                   None   None   None   None  ...           NaN           NaN           NaN           NaN
    PreferredStockValue                               None   None   None   None  ...           NaN           NaN           NaN           NaN
    ContentLibraryNetCurrent                          None   None   None   None  ...           NaN           NaN           NaN           NaN
    PrepaidContentCurrent                             None   None   None   None  ...           NaN           NaN           NaN           NaN
    ContentLibraryNetNoncurrent                       None   None   None   None  ...           NaN           NaN           NaN           NaN
    DueToRelatedPartiesNoncurrent                     None   None   None   None  ...           NaN           NaN           NaN           NaN
    AdditionalPaidInCapitalCommonStock                None   None   None   None  ...           NaN           NaN           NaN           NaN
    ContractWithCustomerLiabilityCurrent              None   None   None   None  ...  7.608990e+08  9.155060e+08  9.247450e+08  1.029261e+09
    ShortTermBorrowings                               None   None   None   None  ...           NaN           NaN  0.000000e+00  4.991610e+08
    OtherPrepaidExpenseCurrent                        None   None   None   None  ...           NaN           NaN           NaN           NaN
    ContentAccountsPayableCurrent                     None   None   None   None  ...           NaN           NaN           NaN           NaN
    ContentAccountsPayableNoncurrent                  None   None   None   None  ...           NaN           NaN           NaN           NaN
    SeniorLongTermNotes                               None   None   None   None  ...           NaN           NaN           NaN           NaN
    RelatedPartyTransactionDueFromToRelatedParty      None   None   None   None  ...           NaN           NaN           NaN           NaN
    LicensingAssetCurrent                             None   None   None   None  ...           NaN  5.151186e+09           NaN           NaN

    [46 rows x 44 columns], 'cash':                                                    2009q2 2009q3 2009q4 2010q1  ...       2019q3        2019q4        2020q2        2020q3
    NetIncomeLoss                                        None   None   None   None  ...  384349000.0  4.028350e+08  7.090670e+08  2.706500e+08
    AdditionstoStreamingContentAssets                    None   None   None   None  ...          NaN  9.971141e+09  3.294275e+09  2.510782e+09
    ChangeInStreamingContentLiabilities                  None   None   None   None  ...          NaN -9.554800e+07  2.589450e+08 -1.084320e+08
    CostofServicesAmortizationofStreamingContentAssets   None   None   None   None  ...          NaN  1.911767e+09  2.483385e+09  4.356601e+09
    CostofServicesAmortizationofDVDContentAssets         None   None   None   None  ...          NaN  2.281900e+07           NaN           NaN
    ...                                                   ...    ...    ...    ...  ...          ...           ...           ...           ...
    ProceedsFromSaleOfAvailableForSaleSecuritiesDebt     None   None   None   None  ...          NaN           NaN           NaN           NaN
    InterestPaidNet                                      None   None   None   None  ...          NaN           NaN           NaN           NaN
    ProceedsfromPublicOfferingofCommonStock              None   None   None   None  ...          NaN           NaN           NaN           NaN
    ExtinguishmentOfDebtAmount                           None   None   None   None  ...          NaN           NaN           NaN           NaN
    ForeignCurrencyTransactionLossBeforeTax              None   None   None   None  ...          NaN           NaN           NaN           NaN

    [71 rows x 44 columns], 'equity':                                                    2009q2 2009q3 2009q4 2010q1  ...        2019q3        2019q4        2020q2        2020q3
    NetIncomeLoss                                        None   None   None   None  ...  6.147020e+08  1.279946e+09  3.440520e+08  2.706500e+08
    OtherComprehensiveIncomeLossNetOfTaxPortionAttr...   None   None   None   None  ...           NaN           NaN           NaN           NaN
    StockIssuedDuringPeriodSharesStockOptionsExercised   None   None   None   None  ...           NaN           NaN           NaN           NaN
    StockIssuedDuringPeriodValueStockOptionsExercised    None   None   None   None  ...           NaN           NaN           NaN           NaN
    StockIssuedDuringPeriodSharesConversionOfConver...   None   None   None   None  ...           NaN           NaN           NaN           NaN
    StockIssuedDuringPeriodValueConversionOfConvert...   None   None   None   None  ...           NaN           NaN           NaN           NaN
    AdjustmentsToAdditionalPaidInCapitalSharebasedC...   None   None   None   None  ...           NaN           NaN           NaN           NaN
    AdjustmentsToAdditionalPaidInCapitalTaxEffectFr...   None   None   None   None  ...           NaN           NaN           NaN           NaN
    StockholdersEquity                                   None   None   None   None  ...  6.105548e+09  6.861505e+09  5.703058e+09  6.105548e+09
    ComprehensiveIncomeNetOfTax                          None   None   None   None  ...           NaN           NaN           NaN           NaN
    StockIssuedDuringPeriodValueEmployeeStockPurcha...   None   None   None   None  ...           NaN           NaN           NaN           NaN
    StockIssuedDuringPeriodValueNewIssues                None   None   None   None  ...           NaN           NaN           NaN           NaN
    StockRepurchasedAndRetiredDuringPeriodValue          None   None   None   None  ...           NaN           NaN           NaN           NaN
    StockRepurchasedAndRetiredDuringPeriodShares         None   None   None   None  ...           NaN           NaN           NaN           NaN
    CumulativeEffectOfNewAccountingPrincipleInPerio...   None   None   None   None  ...           NaN           NaN           NaN           NaN
    StockIssuedDuringPeriodSharesNewIssues               None   None   None   None  ...           NaN           NaN           NaN           NaN

    [16 rows x 44 columns], 'prices':                   Open        High         Low       Close     Volume  Dividends  Stock Splits
    Date                                                                                          
    2002-05-23    1.156429    1.242857    1.145714    1.196429  104790000          0           0.0
    2002-05-24    1.214286    1.225000    1.197143    1.210000   11104800          0           0.0
    2002-05-28    1.213571    1.232143    1.157143    1.157143    6609400          0           0.0
    2002-05-29    1.164286    1.164286    1.085714    1.103571    6757800          0           0.0
    2002-05-30    1.107857    1.107857    1.071429    1.071429   10154200          0           0.0
    ...                ...         ...         ...         ...        ...        ...           ...
    2020-10-20  528.140015  533.780029  522.260010  525.419983   10047200          0           0.0
    2020-10-21  501.029999  506.850006  488.250000  489.049988   17405700          0           0.0
    2020-10-22  494.690002  495.140015  482.000000  485.230011    6997900          0           0.0
    2020-10-23  488.109985  490.059998  481.350006  488.279999    4922200          0           0.0
    2020-10-26  487.024994  496.820007  478.899994  488.239990    6186087          0           0.0

    [4640 rows x 7 columns], 'actions':             Dividends  Stock Splits
    Date                               
    2004-02-12        0.0           2.0
    2015-07-15        0.0           7.0, 'dividends': Series([], Name: Dividends, dtype: int64), 'splits': Date
    2004-02-12    2.0
    2015-07-15    7.0
    Name: Stock Splits, dtype: float64, 'major_holders':         0                                      1
    0   1.62%        % of Shares Held by All Insider
    1  83.49%       % of Shares Held by Institutions
    2  84.86%        % of Float Held by Institutions
    3    1975  Number of Institutions Holding Shares, 'institutional_holders':                               Holder    Shares Date Reported   % Out        Value
    0  Capital Research Global Investors  34111988    2020-06-29  0.0773  15522319019
    1         Vanguard Group, Inc. (The)  34001284    2020-06-29  0.0771  15471944271
    2                     Blackrock Inc.  29171135    2020-06-29  0.0661  13274033270
    3                           FMR, LLC  22033243    2020-06-29  0.0500  10026006894
    4      Price (T.Rowe) Associates Inc  20626346    2020-06-29  0.0468   9385812483
    5           State Street Corporation  16613245    2020-06-29  0.0377   7559691004
    6    Capital International Investors  15137030    2020-06-29  0.0343   6887954131
    7            Capital World Investors  13676170    2020-06-29  0.0310   6223204396
    8            Jennison Associates LLC   9099165    2020-06-29  0.0206   4140484041
    9        Baillie Gifford and Company   7713485    2020-06-29  0.0175   3509944214, 'events':                                     0                    1
    Earnings Date     2021-01-19 00:00:00  2021-01-25 00:00:00
    Earnings Average                 2.13                 2.13
    Earnings Low                     1.82                 1.82
    Earnings High                     2.3                  2.3
    Revenue Average            6379370000           6379370000
    Revenue Low                6281000000           6281000000
    Revenue High               6593000000           6593000000, 'recommendations':                                     0                    1
    Earnings Date     2021-01-19 00:00:00  2021-01-25 00:00:00
    Earnings Average                 2.13                 2.13
    Earnings Low                     1.82                 1.82
    Earnings High                     2.3                  2.3
    Revenue Average            6379370000           6379370000
    Revenue Low                6281000000           6281000000
    Revenue High               6593000000           6593000000, 'esg': None}

#### Sub Functions

The above data request is Full XLBR pandas dataframes of a company's financial statements can be obtained by specifying the company's "cik" or "ticker" of "cik" to the following functions

.. code:: python
    u.prices(cik_or_ticker)                                 # prices,volume, splits dataframe

    u.dividends(cik_or_ticker)                              # dividend payouts dataframe

    u.financial_statement(cik_or_ticker,kind="income")      # income statement dataframe

    u.financial_statement(cik_or_ticker,kind="balance")     # balance sheet dataframe

    u.financial_statement(cik_or_ticker,"cash")             # cashflow statement dataframe

    u.major_sharholders(cik_or_ticker)                      # major shareholders dataframe

    u.major_sharholders(cik_or_ticker)                      # major shareholders dataframe

    u.institutional_holders(cik_or_ticker")                 # institutional holders dataframe

    u.events(cik_or_ticker)                                 # date of events dataframe

    u.splits(cik_or_ticker)                                 # stock split events dataframe

    u.recommendations(cik_or_ticker)                        # analyst recommendations dataframe

    u.esg(cik_or_ticker)                                    # esg metrics dataframe


#### Example Use Case 

I really want to demonstrate the beauty of what we have here since this is often difficult when
looking at thousands of numeric datatables. Let's take a very naive peek by plotting various 
dataframes as timeseries. 

The following is a start to finish example of how one might plot the financial statements and price 
series of the first five companies in the universe.

Here's how we'd implement that: 

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

        # Notice that the code above is expensive since we are interested in a few fields
        # within the results "c", using sub functions would be much more efficient.

    plt.show()

## Donate: 

Consider buying me a coffee to fund the future development of this project.

    bitcoin wallet address: 3LU5MEaAXRJoCo6vx67g1Jj7qDFRKhMs5t