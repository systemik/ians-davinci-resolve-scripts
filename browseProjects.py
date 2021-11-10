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

    # indent = 0
    # currentPath = ""

    def recurse(obj, currentPath):
        """
        obj is a dict from the json
        currentPath is a list to keep track of where we are
        """
        for f in obj.keys():
            if f == "projects":
                for y in obj["projects"].values():
                    # print("/".join(currentPath) + "/" + y)
                    print("\t", y)
                return
            else:
                currentPath.append(f)
                print("/".join(currentPath))

            # better make sure it's a dict before recursion
            if isinstance(obj[f], dict):
                recurse(obj[f], currentPath)

            # going back up a level
            currentPath.pop()

        return

    recurse(data["root"], [""])

    # for item in data["root"]:
    # print(item)


if __name__ == "__main__":
    main()
