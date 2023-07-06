def repeat_words(in_file, out_file):
    open_file = open(in_file)
    write_file = open(out_file, 'w')
    is_write_file_empty = True
    for current_line in open_file:
        words = current_line.split()
        word_dict = {}
        out_file_line = ""
        for current_word in words:
            current_word = current_word.strip(' ,?!.').lower()
            if current_word not in word_dict:
                word_dict[current_word] = 1
            else:
                word_dict[current_word] = word_dict[current_word] +1
        for word in word_dict:
            if word_dict[word] >1:
                out_file_line = out_file_line + word + " "
        out_file_line = out_file_line.strip()
        if out_file_line != "":
            if not is_write_file_empty:
                write_file.write('\n')
            else:
                is_write_file_empty = False
            write_file.write(out_file_line)
