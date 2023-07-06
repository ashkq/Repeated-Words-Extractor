# Repeated-Words-Extractor
1. The function opens the input file specified by in_file using the open() function and assigns it to the open_file variable.
2. It also opens the output file specified by out_file in write mode ('w') using the open() function and assigns it to the write_file variable.
3. The variable is_write_file_empty is set to True initially. This variable is used to track if the output file is empty or not.
4. The code then enters a loop that iterates over each line in the input file (open_file). For each line, it performs the following operations:
   - It splits the line into a list of words using the split() method and assigns it to the words variable.
   - It creates an empty dictionary called word_dict to store the count of repeated words in the current line.
   - It initializes an empty string called out_file_line to store the line that will be written to the output file.
   - It iterates over each word in the words list. For each word, it removes any leading or trailing punctuation characters (',', '.', '?', '!') and converts it to lowercase.
   - If the current word is not present in the word_dict dictionary, it adds the word as a key and sets its value to 1 (indicating that it has occurred once).
   - If the current word is already present in the word_dict dictionary, it increments its count by 1.
   - After processing all the words in the current line, it enters another loop that iterates over each word in the word_dict dictionary.
   - If the count of a word is greater than 1 (meaning it has occurred more than once), it appends the word to the out_file_line string followed by a space.
   - After iterating over all the words in word_dict, it removes any trailing spaces from the out_file_line string using the strip() method.
   - If the out_file_line is not an empty string, it writes it to the output file using the write() method of the write_file object. If the output file is not empty (is_write_file_empty is False), it writes a new line character ('\n') before writing the line.
5. The function continues this process for each line in the input file until there are no more lines.

In summary, this code reads a file, counts the occurrences of each word in each line, and writes only the repeated words (appearing more than once) to the output file, each on a separate line.
