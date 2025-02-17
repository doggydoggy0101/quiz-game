import os
import json

FILE_NAME = "toefl"

# load data
data_path = os.path.join("docs", FILE_NAME + ".json")
with open(data_path, encoding="utf-8") as f:
    data_json = json.load(f)


def get_index_by_value(data, word):
    for index, item in enumerate(data):
        if item["english"] == word:
            return index
    raise ValueError("Search word not in dataset.")


def add_word_to_data(dict_word, list_data):
    word = dict_word["english"]
    assert word != "", "Input word is empty."
    try:
        get_index_by_value(list_data, word)
        print("Word '{}' already exists.".format(word))
    except:
        list_data.append(dict_word)
        print("Word '{}' added successfully.".format(word))

    with open(data_path, "w", encoding="utf-8") as f:
        json.dump(list_data, f, ensure_ascii=False, indent=2)

    print("number of words:", len(list_data))


# modify dataset
# fmt: off
word_list = [
    ["", ""], 
]
# fmt: on

for word in word_list:
    dict_word = {"english": word[0], "chinese": word[1]}
    add_word_to_data(dict_word, data_json)
