#!/usr/bin/env python3
#
# TODO - MAP BLOCKS
#
# TODO - For example:
#
# map_blocks.py district-shapes.geojson tl_2020_04_tabblock20.zip
# map_blocks.py ~/Downloads/district-shapes.geojson ~/Downloads/tl_2020_04_tabblock20.zip
# map_blocks.py ~/dev/dra-data/district-shapes.geojson ~/dev/dra-data/tl_2020_04_tabblock20.zip
#
# For documentation, type:
#
# map_blocks.py -h

# from nagle import *

import sys
import os
import argparse
# import csv
# from collections import defaultdict


# Parse the command line arguments


def main():
    parser = argparse.ArgumentParser(description='Make a block-assignment file')
    parser.add_argument('container_path', help='Path to .geojson for shapes being mapped, e.g., districts')
    parser.add_argument('blocks_path', help='Path to .zip for block shapes being mapped to, e.g., 2020')
    parser.add_argument('-v', '--verbose', dest='verbose', action='store_true', help='verbose mode')

    args = parser.parse_args()

    container_path = os.path.abspath(args.container_path)
    blocks_path = os.path.abspath(args.blocks_path)

    verbose = args.verbose

    print("Mapping blocks ...")
    print("Shapes: ", container_path)
    print("Blocks: ", blocks_path)

# END


# Execute the script
main()
