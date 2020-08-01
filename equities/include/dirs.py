import os 

file_dir = os.path.dirname(os.path.realpath(__file__))
lib_dir  = os.path.join(file_dir,'..')
data_dir = os.path.join(lib_dir,'data')

financial_data_dir = os.path.join(
    data_dir,
    'package',
    'home',
    'ljwcharles',
    'equities-compute',
    'streamer',
    'equities',
    'data'
)

meta_data_dir = os.path.join(
    data_dir,
    'package',
    'equities',
    'lib',
    'pull'
)