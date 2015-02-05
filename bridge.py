#!/usr/bin/python 

from pynetlinux import brctl,ifconfig,vconfig

def create_bridge_with_vid(name, vid):
    devlist = [dev for dev in ifconfig.iterifs(physical=False) if dev.name == "eth1.10"]
    if len(devlist) != 0:
       raise Exists("eth1.10")
    
    br0 = brctl.findbridge(name)
    if br0:
       raise Exists("br0")

    br0 = brctl.addbr(name)
    
    vconfig.add_vlan("eth1", vid)
    
    iface1 = ifconfig.Interface("eth1.%s" % vid) 
    br0.addif(iface1)
    br_iface  = ifconfig.Interface(name)
    iface1.up()
    br_iface.up()
    return

class Exists(BaseException):
    def __str__(self): return "This thing already exists"
