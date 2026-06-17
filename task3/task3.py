import sys
import json

def fill_values(obj, values_map):
    if isinstance(obj, dict):
        if 'id' in obj and obj['id'] in values_map:
            obj['value'] = values_map[obj['id']]
        for key, val in obj.items():
            fill_values(val, values_map)
    elif isinstance(obj, list):
        for item in obj:
            fill_values(item, values_map)

def main():
    if len(sys.argv) != 4:
        print("Usage: python task3.py <values.json> <tests.json> <report.json>")
        return

    values_path = sys.argv[1]
    tests_path = sys.argv[2]
    report_path = sys.argv[3]

    with open(values_path, 'r') as f:
        values_data = json.load(f)
    values_map = {item['id']: item['value'] for item in values_data}

    with open(tests_path, 'r') as f:
        tests_data = json.load(f)

    fill_values(tests_data, values_map)

    with open(report_path, 'w') as f:
        json.dump(tests_data, f, indent=2)

if __name__ == "__main__":
    main()