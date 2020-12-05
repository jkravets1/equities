from equities import Universe 
import datetime as dt 

if __name__ == '__main__':


    universe = Universe(verbose = False)
    tickers = universe.tickers[50:90]

    # Without Multiprocessing 
    start_wo = dt.datetime.now()
    for ticker in tickers:
        universe.company(ticker)
    end_wo = dt.datetime.now()

    # With Multiprocessing
    start_w = dt.datetime.now()
    universe.company(tickers)
    end_w = dt.datetime.now()

    print('W   multiprocessing: %s'%(str(end_wo-start_wo)))
    print('W/O multiprocessing: %s'%(str(end_w-start_w)))