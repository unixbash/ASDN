import json
import time
import datetime

#Generate timestamp
ts = time.time()

#this function was taken from https://stackoverflow.com/questions/7204805/dictionaries-of-dictionaries-merge
def mergeDicts(dict1, dict2):
    for k in set(dict1.keys()).union(dict2.keys()):
        if k in dict1 and k in dict2:
            if isinstance(dict1[k], dict) and isinstance(dict2[k], dict):
                yield (k, dict(mergeDicts(dict1[k], dict2[k])))
            else:
                # If one of the values is not a dict, you can't continue merging it.
                # Value from second dict overrides one in first and we move on.
                yield (k, dict2[k])
                # Alternatively, replace this with exception raiser to alert you of value conflicts
        elif k in dict1:
            yield (k, dict1[k])
        else:
            yield (k, dict2[k])

def generateStructure(str):
    d = current = {}
    list_of_nested_commands = []

    for line in str:
        list_words = line.split()
        for element in list_words:
            current[element] = {}
            current = current[element]
        list_of_nested_commands.append(d)
        d = current = {}

    final_dictionary = {}
    for dictionary in list_of_nested_commands:
        final_dictionary = dict(mergeDicts(final_dictionary, dictionary))

    with open('ml/hierarchy/device-structure' + datetime.datetime.fromtimestamp(ts).strftime('%H-%M-%S_%d-%m-%Y') + '.txt', 'w') as the_file:
        the_file.write(json.dumps(final_dictionary))