# -*- coding: utf-8 -*-
from twisted.internet import iocpreactor
from twisted.internet.defer import Deferred
iocpreactor.install()
from twisted.internet import reactor
from twisted.internet.protocol import Protocol, ClientFactory, Factory, ReconnectingClientFactory
from twisted.internet.endpoints import TCP4ClientEndpoint
from twisted.internet import task
import sys, time, traceback, os, copy

class CloudClient( Protocol, object):
    def __init__(self, login_infos):
        pass
    

    
