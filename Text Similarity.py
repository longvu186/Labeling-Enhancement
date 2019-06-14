from difflib import SequenceMatcher
import pandas
import sys

# Some function


def get_similarity_ratio(string_1, string_2):
    compare = SequenceMatcher(lambda x: x == "\n", string_1, string_2)
    return round(compare.ratio(), 3)


def check_similarity_with_dict(line, dict, list, ratio):
    for key in dict:
        if get_similarity_ratio(line, list[key]) >= ratio:
            return key
            break
    return "different from dict"


# Ratio to evaluate similarity (given ratio > eval_ratio => similar)
eval_ratio = 0.9

# Read file
data = pandas.read_excel("Data.xlsx")

# Handle data
similarity_dict = {0: []}
data_list = list(data["Content"])

# Label similar content
for value, line in enumerate(data_list):
    checking_line = check_similarity_with_dict(line, similarity_dict, data_list, eval_ratio)
    if checking_line == "different from dict":
        similarity_dict.update({value: []})
    else:
        similarity_dict[checking_line].append(value)
    # Loading
    sys.stdout.write('\r')
    sys.stdout.write('{}%'.format(round((value+1)/len(data_list)*100)))
similarity_dict[0] = []
print(similarity_dict)

# Export label for excel
result = []
for key, value in similarity_dict.items():
    if value != []:
        result.append(key+2)
        for item in value:
            result.append(key+2)
    else:
        result.append(key+2)
print(result)

# Write to excel
data["Similarity"] = result
print(data)
data.to_excel('Data.xlsx', index=False)
