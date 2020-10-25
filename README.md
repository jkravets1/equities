
# 🐋 equities 

### access to public company financial data

## Overview: 

    equities allows for easy access to the SEC's XBRL Financial Statement Dataset.
    Data is served to the user in pandas dataframes. 

###### The Dataset: 

https://www.sec.gov/dera/data/financial-statement-data-sets.html

## Install: 

    pip3 install equities

## TUTORIAL: 

#### Instantiating a Universe

We begin by initializing a universe client.

    from equities import Universe
    u = Universe()

#### Essential Methods 

To get the number of companies in the universe call: 
    len(u)

"CIK" numbers are the sec's official unique identifier for public companies. To get a full list of the cik numbers call:

    u.ciks

To get a dictionary mapping "cik" numbers to the names of companies execute:

    u.cik_to_name

Alternatively you can get the inverse to this mapping though:

    u.name_to_cik

## Search: 

You can search for companies by names or ciks by using the search function.

    u.search("aetna")

Here are the results of this query.

    > 🛰️     Search query: "aetna" found 1 matches.
    {'AETNA INC /PA/': '1122304'}

## Queries: 

#### Company 

company data can be obtained by passing a "cik" into the "company()" function on the universe.
    
    u.company(cik="1122304")

Here is the sample output of the above request. It is a dictionary. Observe that the keys, "income","balance","cash","equity" are dataframes and encode the income statement, balance sheet, cashflow statement and equity statement respectively of the company in question.

     📦    Fetching company: 1122304 ...
    {'name': 'AETNA INC /PA/', 'sic': '6324.0', 'business_address': {'country': 'US', 'city': 'HARTFORD', 'zip': '06156', 'adr1': '151 FARMINGTON AVENUE', 'adr2': 'nan'}, 'mailing_address': {'country': 'US', 'city': 'HARTFORD', 'zip': '06156', 'adr1': '151 FARMINGTON AVENUE', 'adr2': 'nan', 'state': 'CT'}, 'phone': '8602730123', 'country_incorporated': 'US', 'state_incorporated': 'PA', 'ein': '232229683.0', 'former_name': 'AETNA U S HEALTHCARE INC', 'income':                                                    2009q2        2009q3        2009q4        2010q1        2010q2        2010q4        2011q3
    AdministrativeServicesContractMemberCoPaymentsA...   None           NaN           NaN           NaN           NaN  6.450000e+07  3.820000e+07
    PremiumsEarnedNetAccidentAndHealth                   None  7.030500e+09  1.899320e+10  2.150010e+10  6.992200e+09  2.111550e+10  1.381030e+10
    PharmaceuticalAndProcessingCosts                     None           NaN           NaN           NaN           NaN  1.200000e+09  7.027000e+08
    InsuredMemberCoPayments                              None           NaN           NaN           NaN           NaN  3.100000e+07  3.750000e+07
    OtherPremiumRevenueNet                               None  4.759000e+08  1.432400e+09  1.876800e+09  4.851000e+08  4.489000e+08  4.518000e+08
    OtherIncome                                          None  1.654600e+09  2.488700e+09  3.044000e+09  8.930000e+08  8.532000e+08  8.965000e+08
    NetInvestmentIncome                                  None  2.588000e+08  7.317000e+08  9.100000e+08  2.752000e+08  2.482000e+08  2.413000e+08
    RealizedInvestmentGainsLosses                        None  8.400000e+06 -3.568000e+08  5.500000e+07  7.670000e+07  1.800000e+07  4.340000e+07
    Revenues                                             None  1.556680e+10  2.319140e+10  3.476410e+10  8.614700e+09  2.570610e+10  1.673220e+10
    PolicyholderBenefitsAndClaimsIncurredHealthCare      None  6.102400e+09  5.216600e+09  2.078550e+10  5.804200e+09  1.699890e+10  1.071480e+10
    PolicyholderBenefitsAndClaimsIncurredNet             None  5.038000e+08  5.145000e+08  2.248100e+09  5.270000e+08  1.521600e+09  1.007700e+09
    SellingExpense                                       None  3.038000e+08  9.385000e+08  1.060900e+09  3.225000e+08  3.048000e+08  2.672000e+08
    GeneralAndAdministrativeExpense                      None  1.160200e+09  1.263300e+09  5.131100e+09  1.195700e+09  1.263300e+09  1.255600e+09
    OperatingExpenses                                    None  2.798900e+09  4.233600e+09  5.046400e+09  1.552300e+09  1.554100e+09  1.591700e+09
    InterestExpense                                      None  1.110000e+08  1.715000e+08  1.806000e+08  6.150000e+07  6.060000e+07  6.070000e+07
    AmortizationOfIntangibleAssets                       None           NaN  2.540000e+07  1.082000e+08  2.450000e+07  7.200000e+07  5.190000e+07
    TotalBenefitsAndExpenses                             None  1.610120e+10  7.201900e+09  2.877650e+10  7.820500e+09  2.337440e+10  1.501270e+10
    IncomeLossFromContinuingOperationsBeforeIncomeT...   None           NaN           NaN           NaN           NaN  1.662600e+09  1.564500e+09
    CurrentIncomeTaxExpenseBenefit                       None  4.879000e+08  5.790000e+08           NaN  2.083000e+08  5.790000e+08  4.549000e+08
    DeferredIncomeTaxExpenseBenefit                      None -3.600000e+06 -5.250000e+07           NaN  2.280000e+07 -5.090000e+07  3.370000e+07
    IncomeTaxExpenseBenefit                              None  4.843000e+08  1.521000e+08  6.247000e+08  2.311000e+08  5.520000e+08  5.109000e+08
    NetIncomeLoss                                        None  7.844000e+08  1.189400e+09  1.384100e+09  4.378000e+08  1.551200e+09  1.122700e+09
    EarningsPerShareBasic                                None  7.800000e-01  7.500000e-01  2.890000e+00  1.300000e+00  3.670000e+00  2.940000e+00
    EarningsPerShareDiluted                              None  1.820000e+00  2.400000e+00  3.470000e+00  9.500000e-01  2.460000e+00  2.420000e+00
    ReductionOfReserveForAnticipatedFutureLossesOnD...   None  0.000000e+00  0.000000e+00  0.000000e+00           NaN           NaN           NaN
    IncomeBeforeIncomeTax                                None           NaN  4.227000e+08  1.901200e+09  8.010000e+08           NaN           NaN
    AmortizationOfOtherAcquiredIntangibleAssets          None  4.900000e+07           NaN           NaN           NaN           NaN           NaN
    IncomeBeforeIncomeTaxes                              None  5.154000e+08           NaN           NaN           NaN           NaN           NaN, 'balance':                                                    2009q2        2009q4        2010q1        2010q2        2010q4
    CommonStockParOrStatedValuePerShare                  None  1.000000e-02  1.000000e-02  1.000000e-02  1.000000e-02
    CommonStockSharesAuthorized                          None  2.700000e+09  2.700000e+09  2.700000e+09  2.700000e+09
    CashAndCashEquivalentsAtCarryingValue                None  1.830100e+09  1.254000e+09  1.747300e+09  1.830100e+09
    CommonStockSharesIssuedAndOutstanding                None  4.335000e+08  4.308000e+08  4.249000e+08  4.001000e+08
    ShortTermInvestments                                 None  2.125700e+09  2.922700e+09  2.922700e+09  2.179600e+09
    PremiumsReceivableAtCarryingValue                    None  6.164000e+08  6.164000e+08  6.304000e+08  6.304000e+08
    OtherReceivables                                     None  5.543000e+08  5.543000e+08  6.340000e+08  6.267000e+08
    AccruedInvestmentIncomeReceivable                    None  2.028000e+08  2.092000e+08  2.160000e+08  2.074000e+08
    CashCollateralForBorrowedSecurities                  None  7.496000e+08  7.496000e+08  4.224000e+08  3.084000e+08
    IncomeTaxesReceivable                                None  1.216000e+08  8.950000e+07  8.950000e+07  8.950000e+07
    DeferredTaxAssetsNetCurrent                          None  3.015000e+08  3.015000e+08  3.834000e+08  4.395000e+08
    OtherAssetsCurrent                                   None  4.526000e+08  4.526000e+08  6.882000e+08  5.514000e+08
    AssetsCurrent                                        None  4.918400e+09  4.918400e+09  6.826900e+09  7.074400e+09
    LongTermInvestments                                  None  1.616340e+10  1.616340e+10  1.780950e+10  1.705110e+10
    ReinsuranceRecoverables                              None  1.010300e+09  1.010300e+09  9.780000e+08  9.869000e+08
    Goodwill                                             None  5.085600e+09  5.085600e+09  5.146200e+09  5.146200e+09
    IntangibleAssetsNetExcludingGoodwill                 None  5.945000e+08  5.907000e+08  5.907000e+08  5.187000e+08
    PropertyPlantAndEquipmentNet                         None  4.675000e+08  4.675000e+08  5.510000e+08  5.398000e+08
    DeferredTaxAssetsNetNoncurrent                       None  7.787000e+08  7.787000e+08  3.334000e+08  2.512000e+08
    OtherAssetsNoncurrent                                None  7.821000e+08  7.811000e+08  7.811000e+08  7.721000e+08
    SeparateAccountAssets                                None  5.919900e+09  5.919900e+09  5.369500e+09  5.454000e+09
    Assets                                               None  3.813500e+10  3.855040e+10  3.855040e+10  3.855040e+10
    ShortTermHealthCareCostsPayable                      None  2.890700e+09  2.895300e+09  2.965400e+09  2.653600e+09
    ShortTermFuturePolicyBenefits                        None  7.288000e+08  7.396000e+08  7.396000e+08  7.225000e+08
    ShortTermUnpaidClaims                                None  5.738000e+08  5.595000e+08  5.790000e+08  5.654000e+08
    UnearnedPremiums                                     None  2.386000e+08  2.386000e+08  4.112000e+08  3.264000e+08
    PolicyholdersFunds                                   None  7.971000e+08  7.883000e+08  8.319000e+08  8.719000e+08
    DepositsReceivedForSecuritiesLoanedAtCarryingValue   None  7.496000e+08  2.100000e+08  2.100000e+08  2.100000e+08
    ShortTermBorrowings                                  None  2.157000e+08  2.157000e+08  4.796000e+08  4.808000e+08
    OtherLongTermDebtCurrent                             None           NaN           NaN  4.497000e+08  8.997000e+08
    OtherLiabilitiesCurrent                              None  2.564200e+09  2.484300e+09  2.484300e+09  2.422900e+09
    LiabilitiesCurrent                                   None  7.554800e+09  8.464200e+09  8.464200e+09  8.359900e+09
    LongTermFurturePolicyBenefits                        None  6.554200e+09  6.470100e+09  6.433200e+09  6.344400e+09
    LongTermUnpaidClaims                                 None  1.271200e+09  1.271200e+09  1.470800e+09  1.483800e+09
    LongTermPolicyholdersFunds                           None  1.171700e+09  1.171700e+09  1.307100e+09  1.294100e+09
    LongTermDebtNoncurrent                               None  3.639200e+09  3.639500e+09  3.639500e+09  3.639500e+09
    OtherLiabilitiesNoncurrent                           None  1.344800e+09  1.344800e+09  1.433800e+09  1.546900e+09
    SeparateAccountsLiability                            None  5.919900e+09  6.283100e+09  6.283100e+09  5.454000e+09
    Liabilities                                          None  2.766610e+10  2.766610e+10  2.904660e+10  2.915400e+10
    CommonStockIncludingAdditionalPaidInCapital          None  4.568000e+08  4.701000e+08  4.992000e+08  5.735000e+08
    RetainedEarningsAccumulatedDeficit                   None  9.716500e+09  1.025670e+10  1.056740e+10  1.025670e+10
    AccumulatedOtherComprehensiveIncomeLossNetOfTax      None -1.118600e+09 -1.223000e+09 -1.223000e+09 -1.223000e+09
    StockholdersEquity                                   None  9.540000e+09  9.503800e+09  8.186400e+09  9.503800e+09
    LiabilitiesAndStockholdersEquity                     None  3.585250e+10  3.855040e+10  3.897280e+10  3.855040e+10
    TaxesPayableCurrent                                  None           NaN           NaN  1.173000e+08           NaN, 'cash':                                                    2009q2        2009q3        2009q4        2010q1        2010q2        2010q4        2011q3
    NetIncomeLoss                                        None  3.466000e+08  3.262000e+08  1.384100e+09  5.626000e+08  4.976000e+08  5.367000e+08
    GainLossOnSaleOfInvestments                          None -8.400000e+06 -2.640000e+07 -5.500000e+07 -7.670000e+07  1.997000e+08 -6.110000e+07
    DepreciationAmortizationAndAccretionNet              None  2.009000e+08  3.068000e+08  4.160000e+08  9.700000e+07  3.133000e+08  2.149000e+08
    IncomeLossFromEquityMethodInvestments                None  3.410000e+07  6.540000e+07 -1.570000e+07  1.020000e+07 -7.000000e+06 -9.700000e+06
    StockOptionPlanExpense                               None  5.570000e+07  8.110000e+07  9.070000e+07  2.760000e+07  8.590000e+07  7.470000e+07
    AccretionAmortizationOfDiscountsAndPremiumsInve...   None -3.550000e+07 -5.460000e+07 -1.520000e+07 -1.160000e+07  2.000000e+07 -2.600000e+06
    IncreaseDecreaseInAccruedInvestmentIncomeReceiv...   None -3.100000e+06 -9.200000e+06 -1.560000e+07 -6.800000e+06  1.800000e+06 -1.200000e+06
    IncreaseDecreaseInOtherReceivables                   None -2.940000e+08 -1.574000e+08 -9.170000e+07 -9.330000e+07  9.800000e+07 -3.130000e+08
    IncreaseDecreaseInAccruedIncomeTaxesPayable          None -2.690000e+07 -9.550000e+07 -1.375000e+08  2.167000e+08  2.020000e+07  5.690000e+07
    IncreaseDecreaseInOtherOperatingCapitalNet           None -7.850000e+07 -5.520000e+07 -1.163000e+08 -6.610000e+07  2.464000e+08  2.720000e+07
    HealthCareAndInsuranceLiabilities                    None  2.010000e+08  8.270000e+07  2.380000e+07  3.617000e+08  3.350000e+08 -2.789000e+08
    AdjustmentsNoncashItemsToReconcileNetIncomeLoss...   None -9.000000e+05  9.000000e+05 -4.500000e+06 -1.000000e+06 -3.700000e+06 -6.000000e+05
    NetCashProvidedByUsedInOperatingActivities           None           NaN           NaN  2.488300e+09  8.373000e+08  8.466000e+08  8.965000e+08
    ProceedsFromSaleAndMaturityOfMarketableSecurities    None  4.961800e+09  9.143200e+09  1.002960e+10  2.462200e+09  7.714800e+09  4.947100e+09
    PaymentsToAcquireInvestments                         None  7.025900e+09  7.934300e+09  1.064220e+10  2.287300e+09  8.324900e+09  5.046500e+09
    PaymentsToAcquirePropertyPlantAndEquipment           None  1.929000e+08  2.594000e+08  4.004000e+08  8.860000e+07  2.171000e+08  1.371000e+08
    PaymentsToAcquireBusinessesNetOfCashAcquired         None  6.100000e+06  6.100000e+06  7.510000e+07  1.000000e+05  1.000000e+05  1.000000e+05
    NetCashProvidedByUsedInInvestingActivities           None -3.829000e+08 -1.356700e+09 -1.073300e+09  1.148000e+08 -4.850000e+08 -2.580000e+07
    RepaymentsOfLongTermDebt                             None           NaN           NaN           NaN           NaN           NaN  9.000000e+08
    ProceedsFromIssuanceOfLongTermDebt                   None           NaN  0.000000e+00  4.848000e+08           NaN  6.978000e+08  4.801000e+08
    ProceedsFromRepaymentsOfShortTermDebt                None  5.058000e+08 -1.049000e+08  2.661000e+08 -1.148000e+08  2.454000e+08  5.498000e+08
    AdditionsToContractHoldersFunds                      None  4.100000e+06  4.900000e+06  7.100000e+06  1.900000e+06  4.900000e+06  3.100000e+06
    WithdrawalFromContractHoldersFunds                   None  7.100000e+06  8.000000e+06  9.000000e+06  3.700000e+06  8.100000e+06  5.300000e+06
    ProceedsFromIssuanceOfCommonStock                    None  3.300000e+06  2.880000e+07  1.708000e+08  3.600000e+06  1.040000e+07  9.300000e+06
    ExcessTaxBenefitFromShareBasedCompensationFinan...   None  4.700000e+06  2.380000e+07  1.532000e+08 -1.000000e+06  9.600000e+06  3.100000e+06
    PaymentsForRepurchaseOfCommonStock                   None  1.157200e+09  1.672800e+09  1.695600e+09  2.638000e+08  6.572000e+08  7.010000e+08
    PaymentsOfDividends                                  None           NaN           NaN  1.730000e+07           NaN           NaN  0.000000e+00
    CollateralOnInterestRateSwaps                        None  3.300000e+07  0.000000e+00  0.000000e+00 -8.900000e+06  2.510000e+07 -3.900000e+07
    NetCashProvidedByUsedInFinancingActivities           None -6.149000e+08 -7.855000e+08 -6.537000e+08 -3.733000e+08  7.202000e+08 -5.266000e+08
    CashAndCashEquivalentsPeriodIncreaseDecrease         None -4.232000e+08 -3.898000e+08  3.740000e+08  5.678000e+08  6.506000e+08  2.024000e+08
    CashAndCashEquivalentsAtCarryingValue                None  1.207500e+09  1.830100e+09  1.203600e+09  1.179500e+09  1.830100e+09  1.406000e+09
    InterestPaid                                         None  1.232000e+08  1.580000e+08           NaN  3.680000e+07  1.564000e+08  1.214000e+08
    IncomeTaxesPaid                                      None  3.979000e+08  5.222000e+08           NaN  3.700000e+06  5.693000e+08  4.136000e+08
    NetCashProvidedByUsedInOperatingActivitiesConti...   None  9.267000e+08  1.855800e+09           NaN           NaN           NaN           NaN, 'equity':                                                    2009q2        2009q3        2009q4        2010q1        2010q2        2010q4        2011q3
    CommonStockSharesIssuedAndOutstanding                None           NaN           NaN           NaN           NaN  4.308000e+08  3.844000e+08
    NetIncomeLoss                                        None  9.121000e+08  1.189400e+09  1.831000e+09  4.378000e+08  1.110600e+09  1.053600e+09
    StockRepurchasedDuringPeriodValue                    None -1.200000e+09 -1.672800e+09 -1.787700e+09 -2.770000e+08 -1.007400e+09  7.500000e+08
    StockRepurchasedDuringPeriodShares                   None           NaN           NaN           NaN           NaN  3.300000e+07  1.800000e+07
    StockholdersEquity                                   None  9.705900e+09  9.296600e+09  1.003840e+10  9.923900e+09  9.540000e+09  9.890800e+09
    CumulativeEffectOfInitialAdoptionOfNewAccountin...   None           NaN           NaN  0.000000e+00           NaN -5.370000e+07           NaN
    OtherComprehensiveIncomeAvailableForSaleSecurit...   None           NaN -3.697000e+08  6.190000e+08 -6.530000e+07  3.745000e+08           NaN
    NetForeignCurrencyAndDerivativeGains                 None -5.000000e+05  2.010000e+07  3.400000e+07  2.400000e+06  2.010000e+07           NaN
    OtherComprehensiveIncomeDefinedBenefitPlansAdju...   None  1.000000e+06  1.500000e+06  2.488000e+08  3.470000e+07  1.043000e+08           NaN
    OtherComprehensiveIncomeLossNetOfTaxPeriodIncre...   None -1.442000e+08  8.164000e+08 -1.592900e+09 -2.820000e+07 -1.386000e+08           NaN
    CommonSharesIssuedForBenefitPlansIncludingTaxBe...   None  9.960000e+07  1.375000e+08  1.192000e+08  4.490000e+07  1.037000e+08           NaN
    DividendsCommonStock                                 None           NaN -1.730000e+07 -2.000000e+07           NaN -1.610000e+07           NaN
    DividendsPayableAmountPerShare                       None           NaN           NaN           NaN           NaN  4.000000e-02           NaN
    OtherComprehensiveIncomeUnrealizedHoldingGainLo...   None -1.447000e+08           NaN           NaN           NaN           NaN           NaN
    CumulativeEffectOfAdoptingNewAccountingStandard...   None           NaN           NaN  1.129000e+08           NaN           NaN           NaN
    BeginningBalanceAsOfJanuary12007AsAdjusted           None           NaN           NaN  9.258000e+09           NaN           NaN           NaN}

#### Individual Financial Statements

Full XLBR pandas dataframes of a company's financial statements can be obtained by specifying the company's "cik" number and the "kind" of the statement: 

    universe.financial_statement(cik,"income")      # income statement dataframe

    universe.financial_statement(cik,"balance")     # balance sheet dataframe

    universe.financial_statement(cik,"cash")        # cashflow statement dataframe

    
#### Example Use Case 

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
    for cik in universe.ciks[:5]:

        company = universe.company(cik)

        company['income].T.plot(
            kind=k,
            figsize=f,
            stacked=s)

        company['balance'].T.plot(
            kind=k,
            figsize=f,
            stacked=s)

        company['cash'].T.plot(
            kind=k,
            figsize=f,
            stacked=s)

    plt.show()

## Donate: 

Consider donating bitcoin to fund the future development of this project.

    bitcoin wallet address: 3LU5MEaAXRJoCo6vx67g1Jj7qDFRKhMs5t