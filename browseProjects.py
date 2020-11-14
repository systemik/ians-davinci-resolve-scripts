#!/usr/bin/env python3

import json
import argparse


def main():
    """
    docstring
    """

    parser = argparse.ArgumentParser(
        description="Browse json that represents a Resolve database.")

    parser.add_argument("pathToJson", type=str, help="Path to the json")

    args = parser.parse_args()
    
    f = open(args.pathToJson)
    data = json.load(f)
    
    indent = 0
    def recurse(obj):
        for f in obj:
            # nonlocal indent
            # print("NEW THINGIE")
            # print("_" * 60, "\nNEW THINGIE", "_" * 60, sep="\n")
            # print(obj)
            # print("\t" * indent, f)
            # indent += 1
            print(f)
            if f is not "_":
                recurse(f)
            # indent -= 1
        
    
    recurse(data["root"])
    # for item in data["root"]:
        # print(item)


if __name__ == "__main__":
    main()
