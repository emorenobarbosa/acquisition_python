#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 17:43:04 2018

@author: laboratorio
"""

import visa
from struct import unpack
import pylab
import numpy as np
import numpy as np
import matplotlib.pyplot as plt
import time
import os

os.chdir('/Users/laboratorio/rx')


rm = visa.ResourceManager()
rm.list_resources()
rm.list_resources()[0]

scope = rm.open_resource(rm.list_resources()[0])

scope.write('DATA:SOU CH1;:DATA:WIDTH 1;:DATA:ENC RPB;:DATA:START 1;:DATA:STOP 1000;:ACQ:STOPA SEQ')

fopen=open("acquisition.dat","a")
print time.time()
for i in range(50000):
    while '1' in scope.ask("ACQ:STATE?"):
        time.sleep(0.05)
    scope.write('CURVE?')
    data=scope.read_raw()
    hl=2+int(data[1])
    wave=data[hl:-1]
    fopen.write(wave)
    if i%1000==0:
        print i
    scope.write("ACQ:STATE ON")
print time.time()
fopen.close()

)
