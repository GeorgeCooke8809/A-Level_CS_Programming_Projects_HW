sentence = input()

sentence_list = list(sentence)

total = len(sentence_list)
index = 0

final = ""

while index <= total:
    try:
        final = f"{final}{sentence_list[index+1]}{sentence_list[index]}"
    except:
        final = f"{final}{sentence_list[index]}"
    index += 2

print(final)