#!/usr/bin/env python

'''
Sample custom dynamic inventroy script for Ansible, in Python.
'''

import os
import sys
import argparse

try:
    import json
except ImportError:
    import simplejson as json

class ExampleInventory(object):
    
    def __init__(self):
        self.inventroy = {}
        self.read_cli_args()

        # Called with '--list'
        if self.args.list:
            self.inventroy = self.example_inventory()
        # Called with '--host [hostname]'
        elif self.args.host:
            # Not implemented, sinc we return _meta info "--list'
            self.inventroy = self.empty_inventory()
        # If no groups or var are present, return an empty inventory
        else:
            self.inventroy = self.empty_inventory()
        
        print(json.dumps(self.inventroy));
    
    def example_inventory(self):
        return {
            "group": {
                "hosts": [
                    "192.168.56.12",
                    "192.168.56.13",
                ],
                "vars": {
                    "example_variables": "value"
                }
            },
            "_meta": {
                "hostvars": {
                    "192.168.56.12": {
                        "host_specific_var": "web"
                    },
                    "192.168.56.13": {
                        "host_specific_var": "db"
                    },
                }
            }
        }

    # Empty inventory for testing
    def empty_inventory(self):
        return { '_meta': { 'hostvars': {}}}

    # Read the command line args passed to the script.
    def read_cli_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--list', action = 'store_true')
        parser.add_argument('--host', action = 'store')
        self.args = parser.parse_args()

# Get the inventory
ExampleInventory()
