import os


# prompt user for directory

directory = input("Enter directory to save file: ")

# directory defaults to current directory if user enter key

if directory == "":

    directory = "."

filename = input("Enter filename: ")

name = input("enter name: ")

address = input("enter address: ")

phone = input("enter phone: ")
if not os.path.exists(directory):
    os.mkdir(directory)
    print('created directory', directory)

with open("{}/{}.".format(directory, filename), 'w') as file:

  file.write(name+','+ address+','+ phone+'\n')

with open("{}/{}.".format(directory, filename), 'r') as file:

  print("{}/{}".format(directory, filename))

  print(file.read())
print('n')


