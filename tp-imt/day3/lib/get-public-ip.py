# -*- coding: utf-8 -*-
import sys

# Ext-Net=2001:41d0:302:1100::8:f101, 54.38.91.45; provider-net=192.168.0.2
ext_ips = [ ip.strip('Ext-Net=') for ip in sys.argv[1].split(';')\
                                 if ip.startswith('Ext-Net') ][0]
print(filter(lambda ip: '.' in ip, ext_ips.split(','))[0].strip())
