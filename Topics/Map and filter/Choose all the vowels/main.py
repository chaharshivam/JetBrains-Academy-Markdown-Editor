def choose_vowels(letters):
    vowels = ['a', 'e', 'i', 'u', 'o']
    return list(filter(lambda letter: letter in vowels, letters))
