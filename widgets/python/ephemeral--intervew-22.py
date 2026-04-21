def decode(message_file):
    with open(message_file, 'r') as file:
        lines = file.readlines()
    number_word_dict = {}
    for line in lines:
        number, word = line.split(maxsplit=1)
        number_word_dict[int(number)] = word.strip()
    current_line = 1
    last_number_in_line = 0
    message_words = []
    while last_number_in_line < max(number_word_dict.keys()):
        last_number_in_line += current_line
        if last_number_in_line in number_word_dict:
            message_words.append(number_word_dict[last_number_in_line])
        current_line += 1
    return ' '.join(message_words)
x=decode('coding_qual_input.txt')
print(x)