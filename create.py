#!/usr/bin/python 

import argparse
import bridge

cmdline = argparse.ArgumentParser(description='Create a bridge with segmentation')

cmdline.add_argument("--name",required=True,
                   help='name of the bridge')

cmdline.add_argument("--vid",required=True, type=int,
                   help='Segmentation ID for the bridge')
args = cmdline.parse_args()

print "will create bridge \"%s\" with segmentation_id \"%s\"" % (args.name,args.vid)

bridge.create_bridge_with_vid(args.name,args.vid)
