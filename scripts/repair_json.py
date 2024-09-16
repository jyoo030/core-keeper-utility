import os

def add_commas_to_json(file_path, output_path):
    try:
        # Read the content of the JSON file
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Prepare to write updated content
        with open(output_path, 'w') as file:
            for i, line in enumerate(lines):
                stripped_line = line.strip()
                if '{' in stripped_line or '}' in stripped_line:
                    file.write(line)
                elif i < len(lines) - 2 or not lines[i+1].strip() == '}':
                    file.write(line.rstrip() + ',\n')
                else:
                    file.write(line)

        print(f"Updated file saved to {output_path}")
    
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except IOError as e:
        print(f"Error: An I/O error occurred: {e}")

input_file_path = ['dump/CoreKeeper/ExportedProject/Assets/StreamingAssets/Conf/ID/ObjectID.json', 'dump/CoreKeeper/ExportedProject/Assets/StreamingAssets/Conf/ID/ConditionID.json']
output_file_path = ['json/ObjectID_updated.json', 'json/ConditionID_updated.json']

for i in range(len(input_file_path)):
    add_commas_to_json(input_file_path[i], output_file_path[i])