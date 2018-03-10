#!/usr/bin/env python3
# saved as pyro-server.py
import config
import Pyro4
Pyro4.config.NS_HOST = config.Pyro4.NS_HOST
Pyro4.config.NS_PORT = config.Pyro4.NS_PORT

@Pyro4.expose
class GreetingMaker(object):
    def broardcast_msg(self, msg, name):
        print('got a ping from {} at xxx'.format(name))
        return "{0} - Your message was succesfully send\n" \
               "--- {1}".format(name,msg)
    def pyroid(self):
        return self._pyro_id
        



daemon = Pyro4.Daemon()                # make a Pyro daemon
ns = Pyro4.locateNS()                  # find the name server
print('--- connected to nameserver {0}'.format(ns))
uri = daemon.register(GreetingMaker)   # register the greeting maker as a Pyro object
ns.register("example.greeting", uri)   # register the object with a name in the name server

print("Ready.")
daemon.requestLoop()                   # start the event loop of the server to wait for calls
