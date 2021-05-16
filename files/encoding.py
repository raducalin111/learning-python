def open_file(file_name, encoding):
    with open(file_name, 'rt', encoding=encoding) as file:
        for line in file:
            print(line)


open_file('files/encoding.txt', 'UTF-8')
open_file('files/encoding.txt', 'utf_8_sig')
open_file('files/encoding.txt', 'ASCII')
