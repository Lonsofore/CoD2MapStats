import os
import sys

from appdirs import AppDirs

from cod2mapstats import CONFIG_NAME, CONFIG_DEFAULT, CONFIG_FORMAT, AUTHOR, PACKAGE_NAME
from .utility import get_script_dir, create_dir_if_not_exists, get_config


# init dirs
DIRS = AppDirs(PACKAGE_NAME, AUTHOR)


# init config
CONFIG_PATH_DEFAULT = os.path.join(get_script_dir(), '{}.{}'.format(CONFIG_DEFAULT, CONFIG_FORMAT))
CONFIG_PATH = os.path.join(DIRS.user_config_dir, '{}.{}'.format(CONFIG_NAME, CONFIG_FORMAT))
if not os.path.isfile(CONFIG_PATH):
    create_dir_if_not_exists(CONFIG_PATH)
    conf = open(CONFIG_PATH_DEFAULT, 'r').read()
    conf1 = open(CONFIG_PATH, 'w').write(conf)
CONFIG = get_config(CONFIG_PATH)


MAPS_PATH = CONFIG['maps_path']
DB_PATH = CONFIG['db_path']
TABLE_NAME = CONFIG['table_name']
