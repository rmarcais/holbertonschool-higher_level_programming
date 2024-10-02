#!/usr/bin/python3
"""Serializing and Deserializing with XML"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a dictionary <dictionary> into XML
    and save it in the file <filename>
    """

    root = ET.Element("data")

    for k, v in dictionary.items():
        child = ET.SubElement(root, k)
        child.text = str(v)

    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """
    Reads the XML data from the file <filename>
    and returns a deserialized dictionary.
    """

    tree = ET.parse(filename)
    root = tree.getroot()

    d = {}

    for child in root:
        d[child.tag] = child.text

    return d
