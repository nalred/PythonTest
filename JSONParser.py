import json
import os

def update_JSON(d, element):
    if element in d:
        d.pop(element, None)
    else:
        for key, value in d.items():
            if isinstance(value, dict) and element in value:
                value.pop(element, None)
                d[key] = value
    return d

def parse_update_JSON(removeElements):
    with open('./Data/test_payload.json', 'r') as f:
        data = json.load(f)

    for element in removeElements:
        data = update_JSON(data, element)

    output_path = './Data/test_payload_updated.json'

    if os.path.exists(output_path):
        os.remove(output_path)

    with open(output_path, 'x') as f:
        data = json.dump(data, f)


if __name__ == '__main__':
    removeElements = ['outParams', 'appdate']
    parse_update_JSON(removeElements)