#!/usr/bin/env python3
# saved as pyro-client.py

# allowed sections in the jason-configfile
sections_allowed = ["Pyro4","Kivy"]


import json
config = json.load(open('config.json','r'))

class cnf_obj():
    def __init__(self, initial_dict=None):
        for key in initial_dict:
            self.__setattr__(key, initial_dict[key])

import sys
thismodule = sys.modules[__name__]

for section in sections_allowed:
    if section in config:
        setattr(thismodule, section, cnf_obj(config[section]))


if __name__=='__main__':
    print('Configuration self test and verification pretty print')
    sections = filter(lambda s: s in sections_allowed, dir())
    for sec in sections:
        print('\n[{}]'.format(sec))
        sec_obj = eval(sec)
        for key in dir(sec_obj):
            if not key[:2] == '__':
                print('{}={}'.format(key,getattr(sec_obj,key)))
