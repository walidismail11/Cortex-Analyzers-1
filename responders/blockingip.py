#!/usr/bin/env python3
# encoding: utf-8

import traceback
import datetime
from netmiko import ConnectHandler
from cortexutils.responder import Responder

class BLOCKIPCODE(Responder):
    def __init__(self):
        Responder.__init__(self)
        self.PALOALTO_username = self.get_params('config.PALOALTO_username', None, 'PALOALTO username is require to login')
        self.PALOALTO_password = self.get_params('config.PALOALTO_password', None, 'PALOALTO Password is require to login')
        self.PALOALTO_ip = self.get_params('config.PALOALTO_ip', None, 'Set a PALOALTO IP')
        self.time = ''
        print(self.PALOALTO_username)
        print(self.PALOALTO_password)
        print(self.PALOALTO_ip)

    def run(self):
       Responder.run(self)
       data = self.get_param('data.data')
       device = ConnectHandler(device_type='PAN-OS', ip=self.Paloalto_ip, username=self.Paloalto_username, password=self.Paloalto_password, secret=self.Paloalto_secret)
       print(data)
       
       config_commands = [
            "config firewall address",
            "edit ipblock" + '$data',
            "set subnet" + '$data',
            "end",
            "config firewall addrgrp", 
            "edit BLOCKIPCODE", 
            "append member ipblock" + '$data',
            "end",
       ]
       print(config_commands)
       output = device.send_config_set(config_commands)

if __name__ == '__main__':
    BLOCKIPCODE().run()
    
