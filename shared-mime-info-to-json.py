#!/usr/bin/env python3

import json
import xml.etree.ElementTree

root = xml.etree.ElementTree.parse("./freedesktop.org.xml",).getroot()

out_dict = dict()

shared_mime_xml_namespace = "http://www.freedesktop.org/standards/shared-mime-info"

def without_shared_mime_ns(string):
    return string.replace("{http://www.freedesktop.org/standards/shared-mime-info}", "")

lang_attr = "{http://www.w3.org/XML/1998/namespace}lang"

for mime_type_child in root:
    mime_type = mime_type_child.attrib["type"]
    out_dict[mime_type] = {}
    single_mimes = out_dict[mime_type]
    single_mimes["type"] = mime_type
    single_mimes["description"] = {}
    per_lang_descriptions = single_mimes["description"]
    alias = None
    for desc_child in mime_type_child:
        tag = without_shared_mime_ns(desc_child.tag)
        text = lambda: desc_child.text
        if tag == "comment":
            lang = "en"
            if desc_child.attrib:
                lang = desc_child.attrib[lang_attr]
            per_lang_descriptions[lang] = text()
        elif tag == "acronym":
            single_mimes["acronym"] = text()
        elif tag == "expanded-acronym":
            single_mimes["expanded"] = text()
        elif tag == "generic-icon":
            single_mimes["icon"] = desc_child.attrib["name"]
        elif tag == "alias":
            alias = desc_child.attrib["type"]
    if alias is not None:
        out_dict[alias] = single_mimes

out_file = open("./mimetype-descriptions-map.js", "w")

json_mimes = json.dumps(out_dict)
json_ready_for_node_module = "module.exports = " + json_mimes

out_file.write(json_ready_for_node_module)
