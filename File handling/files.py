import os

# r = Read
# a = Append
# w = Write
# x = Create

# Read - error if it doesn't exist

f = open("names.txt")
# print(f.read())
# print(f.read(3))

# print(f.readline())
# print(f.readline())

for i in f:
    print(i)

f.close()

try:
    f = open("names.txt")
    print(f.read())
except:
    print("The file you want to read doesn't exist")
finally:
    f.close()

# Append - creates the file if it doesn't exist

f = open("names.txt","a")
f.write("\nSam")
f.close()

f = open('names.txt')
print(f.read())
f.close()

# Write (Overwrite)

f = open("context.txt","w")
f.write("I deleted all the context")
f.close()

f = open("context.txt")
print(f.read())
f.close()

# Two ways to create a new file

# Opens a file for writing ,creates the file if it doesn't exist
f = open("names_list.txt","w")
f.close()

# Creates the specified file, but returns an error if the file exists
if not os.path.exists("bilal.txt"):
    f = open("bilal.txt","x")
    f.close()

# Delete a file

# Avoid an error if the file doesn't exist
if os.path.exists("bilal.txt"):
    os.remove("bilal.txt")
else:
    print("File doesn't exist")

# copying and pasting all the data from one file to another.

with open("more_name.txt") as f:
    content = f.read()

with open("names.txt","w") as f:
    f.write(content)