import os
import yaml

from equities.include.dirs import lib_dir

config_path = os.path.join(lib_dir,'config','essential.yaml')
with open(config_path, "r") as yml_file:
    config = yaml.load(yml_file)

bucket_name = config['google_cloud_platform']['bucket_name']
bucket_uri = 'https://storage.googleapis.com/' \
    + bucket_name + '/'