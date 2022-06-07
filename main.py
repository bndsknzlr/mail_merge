# read start content
with open("./Input/Letters/starting_letter.txt") as letter_start:
    start_content = letter_start.read()

# put names into list and strip strings from unused letters
with open("./Input/Names/invited_names.txt") as letter_names:
    name_list = letter_names.readlines()
    stripped_list = []
    for i in name_list:
        stripped_names = i.strip("\n")
        stripped_list.append(stripped_names)

# create letters
for name in stripped_list:
    with open(f"./Output/ReadyToSend/letter_for_ {name}", 'w+') as top:
        new_content = start_content.replace("[name]", name)
        new_letter = top.write(new_content)
