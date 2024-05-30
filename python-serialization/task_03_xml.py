#!/usr/bin/python3
"""
mod 3
"""


from task_03_xml import serialize_to_xml, deserialize_from_xml

def main():
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

if __name__ == "__main__":
    main()
