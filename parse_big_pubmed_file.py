from xml.etree import ElementTree as ET


def lazy_parse_xmls(filename='pubmed_result.xml'):
    parser = ET.iterparse(filename)

    for event, element in parser:
        # element is a whole element
        if element.tag == 'PubmedArticle':
            yield ET.tostring(element, encoding='latin1', method='xml').decode("latin1")


gen = lazy_parse_xmls()

filecount = 0

for xmlstring in gen:
    counter = "{:0>10d}".format(filecount)
    with open(f"article_{counter}.xml", "w", encoding='latin1') as xmlfile:
        xmlfile.write(xmlstring)
    filecount += 1

