from importlib import import_module


import_module('typer')
from ssg.site import Site

def main(source = "content", dest = "dist"):
    config = {
        'source' : 'source',
        'dest' : 'dest'
    }
    