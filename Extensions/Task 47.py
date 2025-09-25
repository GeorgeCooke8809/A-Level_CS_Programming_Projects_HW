def wordCount(string):
    string = string.split(" ")

    return len(string)

def vowelCount(string):
    letters = list(string)

    vowels_list = ["A", "E", "I", "O", "U"]
    vowels = 0

    for i in letters:
        if i.upper() in vowels_list:
            vowels += 1

    return vowels

sentence = input("Sentence Analysis\nEnter a sentence then press ENTER.\n\n")

words = wordCount(sentence)
vowels = vowelCount(sentence)

print(f"Your sentence has {words} words and a total of {vowels} vowels.")