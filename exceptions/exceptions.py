import os


def open_file(file_name):
    try:
        print('Attempting to open file {0}'.format(file_name))
        open(file_name)
    except FileNotFoundError as err:
        print('Exception thrown: {0}'.format(err))
    else:
        print('Executed only if exception is not thrown')
    finally:
        print('Executed anyway')


print(f'Working directory is {os.getcwd()}')

# Check file that does not exist
open_file('../files/randomfilename.ttt')

# Check file that does exist
open_file('../files/pending.csv')
