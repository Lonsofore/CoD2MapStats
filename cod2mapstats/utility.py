import os
import sys
import inspect

from ruamel import yaml


def get_script_dir(follow_symlinks=True):
    if getattr(sys, 'frozen', False): # py2exe, PyInstaller, cx_Freeze
        path = os.path.abspath(sys.executable)
    else:
        path = inspect.getabsfile(get_script_dir)
    if follow_symlinks:
        path = os.path.realpath(path)
    return os.path.dirname(path)
    
    
def create_dir_if_not_exists(d):
    basedir = os.path.dirname(d)
    if not os.path.exists(basedir):
        os.makedirs(basedir)
    
    
def get_config(path):
    return yaml.safe_load(open(path, "r"))
    
    
def list_files(directory, *args):
    result = []
    for f in os.listdir(directory):
        for ext in args:
            if f.endswith('.{}'.format(ext)):
                result.append(f)
                break
    return result

    
def get_min_max(arr):
    amin = arr[0]
    amax = arr[0]
    for a in arr:
        if a < amin:
            amin = a
        elif a > amax:
            amax = a
    return (amin, amax)
