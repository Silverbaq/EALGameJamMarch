#!/usr/bin/env python3
# saved as greeting-client.py
import config
import Pyro4
Pyro4.config.NS_HOST = config.Pyro4.NS_HOST
Pyro4.config.NS_PORT = config.Pyro4.NS_PORT
ns = Pyro4.locateNS()                         # find the name server


print('--- connected to nameserver {0}'.format(ns))
print(ns.list())
greeting_maker = Pyro4.Proxy("PYRONAME:example.greeting")    # use name server object lookup uri shortcut

name = ''
while name.lower() not in ['exit','quit','q']:
    name = input("What is your name? ").strip()
    msg = input("Message? ").strip()
    #greeting_maker = Pyro4.Proxy(uri.location)    # use name server object lookup uri shortcut
    print(greeting_maker.broardcast_msg(msg,name))


input("UPS? ")
