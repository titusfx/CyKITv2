#!/usr/bin/env python
import hidapi

hidapi.hid_init()

for dev in hidapi.hid_enumerate():
    print(50*'-')
    print(dev.description())
