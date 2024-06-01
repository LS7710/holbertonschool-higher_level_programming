#!/usr/bin/python3
"""
mod 3
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a dictionary to XML and save it to the specified file.

    Parameters:
    dictionary (dict): The dictionary to serialize.
    filename (str): The name of the file to save the XML data.
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.Element(key)
        child.text = str(value)
        root.append(child)

    tree = ET.ElementTree(root)
    try:
        tree.write(filename)
        return True
    except Exception as e:
        print(f"An error occurred while writing XML to file: {e}")
        return False

def deserialize_from_xml(filename):
    """
    Deserialize XML data from the specified file into a dictionary.

    Parameters:
    filename (str): The name of the file to read the XML data from.

    Returns:
    dict: The deserialized dictionary, or None if an error occurs.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        dictionary = {child.tag: child.text for child in root}
        return dictionary
    except FileNotFoundError:
        print(f"The file {filename} was not found.")
        return None
    except ET.ParseError as e:
        print(f"An error occurred while parsing XML: {e}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    sample_dict = {
        'name': 'John',
        'age': '28',
        'city': 'New York'
    }

    xml_file = "data.xml"
    if serialize_to_xml(sample_dict, xml_file):
        print(f"Dictionary serialized to {xml_file}")
    else:
        print("Serialization failed.")

    deserialized_data = deserialize_from_xml(xml_file)
    if deserialized_data:
        print("\nDeserialized Data:")
        print(deserialized_data)
    else:
        print("Deserialization failed.")
