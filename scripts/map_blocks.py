#!/usr/bin/env python3
#
# MAKE A BLOCK-ASSIGNMENT FILE FOR A SET OF "CONTAINER" SHAPES, LIKE DISTRICTS
#
'''
For example:

map_blocks.py district-shapes.geojson tl_2020_04_tabblock20.zip
map_blocks.py ~/dev/temp/district-shapes.geojson ~/dev/temp/tl_2020_04_tabblock20.zip

Bad inputs cases:

map_blocks.py district-shapes.json tl_2020_04_tabblock20.zip
map_blocks.py district-shapes.geojson tl_2020_04_tabblock20.shp
map_blocks.py ~/dev/temp/doesnt-exist.geojson ~/dev/temp/tl_2020_04_tabblock20.zip
map_blocks.py ~/dev/temp/district-shapes.geojson ~/dev/temp/doesnt-exist.zip

For documentation, type:

map_blocks.py -h

'''

# from nagle import *

import sys
import os
import argparse
# import csv
# from collections import defaultdict

def main():
    # Parse & validate the args
    
    parser = argparse.ArgumentParser(description='Make a block-assignment file')
    parser.add_argument('container_path', help='Path to .geojson for shapes being mapped, e.g., districts')
    parser.add_argument('blocks_path', help='Path to .zip for block shapes being mapped to, e.g., 2020')
    parser.add_argument('-v', '--verbose', dest='verbose', action='store_true', help='verbose mode')

    args = parser.parse_args()

    container_path = os.path.abspath(args.container_path)
    blocks_path = os.path.abspath(args.blocks_path)

    verbose = args.verbose

    container_fn, container_ext = os.path.splitext(container_path)
    blocks_fn, blocks_ext = os.path.splitext(blocks_path)

    if (container_ext != '.geojson'):
        print("Container file must be a .geojson")
        sys.exit(0)
    
    try:
        f = open(container_path)
        f.close()
    except IOError:
        print("Container file does not exist.")
        sys.exit(0)

    if (blocks_ext != '.zip'):
        print("Blocks file must be a .zip")
        sys.exit(0)

    try:
        f = open(blocks_path)
        f.close()
    except IOError:
        print("Blocks file does not exist.")
        sys.exit(0)

    # Map the blocks to the shapes

    print("Mapping blocks ...")
    print("Shapes: ", container_path)
    print("Blocks: ", blocks_path)

# END


# Execute the script
main()
