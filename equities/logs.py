decorator = 80

def initialize():
    print('-'*decorator+'\n  '+'\t'*3+'🐋\tWelcome to equities.\n'
        +'-'*decorator+'\n Initializing Universe. This may take a second...')

def initialized(msgs,size):
    message = ''.join(['\n\t%s'%msg for msg in msgs if '&' not in msg])
    print('\r> 🌌\tUniverse initialized. size: %s\n'
        %str(size)+' Success. You\'re good to go!\n'
        +'-'*decorator + '\n Messages: %s'%message +'\n'+'-'*decorator)
    [exec(msg.replace('&','')) for msg in msgs if '&' in msg]

def failed(e):
    print('''\r> 🔫\n\tUniverse failed to initialize! If this
        problem persistsplease run the following:
            1)pip3 install --upgrade polity
            2)pip3 install --upgrade equities\n\n
        Exception: %s'''%str(e))

def search(query,matches):
    print('\r> 🛰️\tSearch query: "%s" found %s matches.'%(query,matches))