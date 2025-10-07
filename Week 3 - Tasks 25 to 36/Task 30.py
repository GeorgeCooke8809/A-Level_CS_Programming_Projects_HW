def my_mod(note, funds):
    number_notes = funds // note
    remaining = funds % note

    return [int(number_notes), remaining]

def get_notes(funds):
    notes = []
    for i in [50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]:
        returned = my_mod(i, funds)
        try:
            notes.append(returned[0])
            funds = returned[1]
        except:
            pass

    return notes

total = float(input("Funds: £"))
note_combination = get_notes(total)

print(f"£50 Notes: {note_combination[0]}\n£20 Notes: {note_combination[1]}\n£10 Notes: {note_combination[2]}\n£5 Notes: {note_combination[3]}\n£2 Coins: {note_combination[4]}\n£1 Coins: {note_combination[5]}\n£0.50 Coins: {note_combination[6]}\n£0.20 Coins: {note_combination[7]}\n£0.10 Coins: {note_combination[8]}\n£0.05 Coins: {note_combination[9]}\n£0.02 Coins: {note_combination[10]}\n£0.01 Coins: {note_combination[11]}\n") 