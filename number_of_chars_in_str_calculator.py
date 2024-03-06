from collections import Counter
def number_of_chars_in_str_calculator(str):
    return dict(Counter(str))
print(number_of_chars_in_str_calculator("hello"))