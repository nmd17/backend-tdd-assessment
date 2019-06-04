#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility"""

__author__ = "nmd3"


import sys
import argparse

def create_parser():
    """Creates and returns an argparse cmd line option parser"""

    parser = argparse.ArgumentParser(description="Perform transformation on input text.")

    parser.add_argument("-u", "--upper", action="store_true", help="convert text to uppercase")
    parser.add_argument("-l", "--lower", action="store_true", help="convert text to lowercase")
    parser.add_argument("-t", "--title", action="store_true", help="convert text to titlecase")
    parser.add_argument('text', help="text to be manipulated")
    
    return parser



def main():
    parser = create_parser()
    args = parser.parse_args()

    result = args.text
   
    if args.upper:
       result = result.upper()
    if args.lower:
        result = result.lower()
    if args.title:
        result = result.title()
    if len(sys.argv) == 2:
        print(result)
        return result

    print(result)
    return result
    
    


   







if __name__ == '__main__':
    main()
