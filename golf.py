import golf


# prompt user for directory

directory = input("Enter directory to save file: ")

# directory defaults to current directory if user enter key

if directory == "":

    directory = "."

filename = input("Enter filename: ")

name = input("enter name john rosales: ")

address = input("enter address 12345 ave: ")

phone = input("enter phone 18003456789: ")


with open("{}/{}.csv".format(directory, filename), 'w') as file:

  file.write(name+','+ address+','+ phone+'\n')

with open("{}/{}.csv".format(directory, filename), 'r') as file:

  print("{}/{}sv contents".format(directory, filename))

  print(file.read())
print('n')


