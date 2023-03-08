import os

# Function that get a path and a word and look for that word in the files that find inside the path

def read_files(file_path, word):

    os.chdir(file_path)  # changing directory

    for item in os.listdir():   # for every item
        if (os.path.isfile(item)):  # if item is a file
            
            file = open(item, 'r', encoding='utf-8')    # open it with sweedish encoding
            if (file):

                text = file.read()
                if (text.find(word) >= 0):
                    print(word, " find it in item: ", item)
                    print("Path:", os.path.abspath(item))
                file.close()
            else:
                print("Error, file couldn,t be oppened. Path: ",os.path.abspath(file_path))

    for item in os.listdir():
        if (os.path.isdir(item)):  # if item is a directory
            newCwd = os.path.join(file_path, item)   # save a new path with the directory name
            read_files(newCwd, word)  # call the function with the new path (recursion)



 
cwd = os.getcwd()  # get current directory 


file_path = os.path.join(cwd, 'doc')  # writing and saving in a variable the directory where i have the text files


print("write the word you are looking for")
word = input()      # variabel that save the word we are looking for

read_files(file_path, word)  # calling the function


