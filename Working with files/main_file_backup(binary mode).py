# Making copies of file into new backup file
flag = 0
while flag == 0:
    try:
        filename1 = input('Input the filename you want to backup: ')
        if filename1 == 'exit':
            break
            print('You stopped the program.')
        filename2 = 'backup' + filename1
        file1 = open(filename1, 'rb')
        file2 = open(filename2, 'wb')
        file2.write(file1.read())
        file1.close
        file2.close
        flag = 1
        print('Backup was succesfully made!')
    except FileNotFoundError:
        print("File doesn`t exist. Try again!")

inp = input()

# open('filename', 'r or w or a or b(rb\wb)')
# r - Read file
# w - Write file
# a - Append file(Дополнить)
#
# b - Binary mode

# cmd -> pyinstaller -F filename.py

# with open('filename', 'r') as f:
#     print(f.read(5)) # read first 5 bytes of the file
#     # "with" will close the file after executing
#     # this indentation block
# so you don`t need f.close here
