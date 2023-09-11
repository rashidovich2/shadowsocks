#!/usr/bin/python

import json

with open('server-multi-passwd-performance.json', 'wb') as f:
    ports = {str(i): 'aes_password' for i in range(7000, 9000)}
    r = {
        'server': '127.0.0.1',
        'local_port': 1081,
        'timeout': 60,
        'method': 'aes-256-cfb',
        'port_password': ports,
    }
    print(r)
    f.write(json.dumps(r, indent=4).encode('utf-8'))
