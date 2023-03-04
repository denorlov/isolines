import json
import sys

from rdp import rdp

input_file_name = 'data/contours.json'
output_file_name = 'data/compacted_contours.json'
rdp_epsilon = 0.1

if __name__ == "__main__":
    arg_count = len(sys.argv)
    print(f"Arguments count: {arg_count}")
    proc_args = sys.argv
    for i, arg in enumerate(proc_args):
        print(f"Argument {i}: {arg}")

    if arg_count == 1:
        print("Use:")
        print(" python compact.py {input_file_name} {output_file_name} {rdp_epsilon}")
    else:
        if arg_count > 1:
            input_file_name = proc_args[1]
        if arg_count > 2:
            output_file_name = proc_args[2]
        if arg_count > 3:
            rdp_epsilon = proc_args[3]

print(f"input_file_name: {input_file_name}")
print(f"output_file_name: {output_file_name}")
print(f"rdp epsilon: {rdp_epsilon}")

with open(input_file_name) as json_file:
    data = json.load(json_file)
    json_file.close()

compacted_data = dict()
compacted_data["contours"] = list()

print()

for contour in data["contours"]:
    print(f"processing contour z:{contour['z']}")
    compacted_sets = list()
    compacted_contour = {"z": contour['z'], "sets": compacted_sets}
    for i, curve in enumerate(contour['sets']):
        print(f"processing line #{i}")
        compacted_sets.append(rdp(curve, epsilon=rdp_epsilon))
    compacted_data["contours"].append(compacted_contour)

with open(output_file_name, 'w') as json_file:
    json.dump(compacted_data, json_file, indent=3)
    json_file.close()
