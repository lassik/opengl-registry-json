#! /usr/bin/env python3

import json
import xml.etree.ElementTree as ET
from collections import defaultdict


def convert_library(library):
    j = {"groups": defaultdict(dict)}
    xml = ET.parse(open("{}.xml".format(library), "rb"))
    for groups in xml.findall("groups"):
        for group in groups.findall("group"):
            enums = []
            for enum in group.findall("enum"):
                enums.append(enum.attrib["name"])
            j["groups"][group.attrib["name"]] = enums
    with open("{}.json".format(library), "w") as out:
        json.dump(j, out, sort_keys=True, indent=" " * 2)


def main():
    for library in ["gl", "glx", "wgl"]:
        convert_library(library)


if __name__ == "__main__":
    main()
