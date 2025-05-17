def count_words(input_string):
    words_list = input_string.split()
    return len(words_list)

def count_letters(input_string):
    letter_counts = {}
    for char in input_string:
        if char.lower() in letter_counts:
            letter_counts[char.lower()] += 1
        else:
            letter_counts[char.lower()] = 1
    return letter_counts

def sort_on(unsorted_dict):
    return unsorted_dict["num"]

def sort_dict(unsorted_dict):
    multi_dict_list = []
    for item in unsorted_dict:
        multi_dict_list.append({"char": item, "num": unsorted_dict[item]})
    multi_dict_list.sort(reverse=True, key=sort_on)
    return multi_dict_list