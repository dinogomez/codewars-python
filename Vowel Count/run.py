def get_count(input_str):
    num_vowels = 0
    vowel = ['a','e','i','o','u']
    if input_str is "":
        return num_vowels
    input_str = list(input_str)
    for i in input_str:
        if i in vowel:
            num_vowels += 1
    return num_vowels