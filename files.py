# myFiles = open("myFile.txt") # open the file
# print(myFiles.read()) # print the file content
# myFiles.seek(0) # seek to the start of the file
# print(myFiles.readlines()) # print the file content as array per line
# myFiles.close() # close the file


# by using the with statement below we don't need to close the file
# with open('myFile.txt', mode='r') as f:
    # print(f.read()) # print the file content
    # f.seek(0) # seek to the start of the file
    # print("\n")
    # print(f.read()) # print the file content

with open('myFile.txt', mode='a') as f:
    f.write('\nfour on FOUR') # print the file content

with open('myFile.txt', mode='r') as f:
    print(f.read()) # print the file content

with open('myNewFile.txt', mode='w') as f:
    f.write('new file')

with open('myNewFile.txt', mode='r') as f:
    print(f.read()) # print the file content