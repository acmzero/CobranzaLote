
#
# Default setup file for a Camelot application
#
# To build a windows installer, execute this file with :
#
#     python setup.py egg_info bdist_cloud wininst_cloud
#
# Running from the Python SDK command line
#

import datetime
import logging

from setuptools import setup, find_packages

logging.basicConfig( level=logging.INFO )

setup(
    name = 'Cobranza',
    version = '1.0',
    author = '-',
    url = '-',
    include_package_data = True,
    packages = find_packages(),
    py_modules = ['settings', 'main'],
    entry_points = {'gui_scripts':[
                     'main = main:start_application',
                    ],},
    options = {
        'bdist_cloud':{'revision':'0',
                       'branch':'master',
                       'uuid':'a888c28c-fe23-49d2-8141-4c3cf9962b2e',
                       'update_before_launch':False,
                       'default_entry_point':('gui_scripts','main'),
                       'changes':[],
                       'timestamp':datetime.datetime.now(),
                       },
        'wininst_cloud':{ 'excludes':'excludes.txt',
                          'uuid':'a888c28c-fe23-49d2-8141-4c3cf9962b2e', },
    }, 

  )

    