#! /usr/bin/env python3

import json
import xml.etree.ElementTree as ET
from collections import defaultdict


def all_text(elem):
    if isinstance(elem, str):
        return elem
    a = elem.text or ""
    b = "".join([all_text(subelem) for subelem in elem])
    c = elem.tail or ""
    return a + b + c


def convert_library(library):
    j = {
        "groups": defaultdict(dict),
        "typedefs": defaultdict(dict),
        "structs": defaultdict(dict),
    }
    xml = ET.parse(open("{}.xml".format(library), "rb"))
    for groups in xml.findall("groups"):
        for group in groups.findall("group"):
            enums = []
            for enum in group.findall("enum"):
                enums.append(enum.attrib["name"])
            j["groups"][group.attrib["name"]] = enums
    for types in xml.findall("types"):
        for type in types.findall("type"):
            name = None
            for name_ in type.findall("name"):
                name = name_.text
            if name and name.startswith("struct "):
                j["structs"][name[len("struct ") :]]
            elif name:
                j["typedefs"][name] = all_text(type).strip()
    with open("{}.json".format(library), "w") as out:
        json.dump(j, out, sort_keys=True, indent=" " * 2)


def main():
    for library in ["gl", "glx", "wgl"]:
        convert_library(library)


if __name__ == "__main__":
    main()
