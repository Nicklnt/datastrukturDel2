import hashlib

import os


#Function that go througth all the elements and encode it to create a hash table
def hashWord(file_path,hashT):
    os.chdir(file_path)  # changing directory
    dict= hashT

    for item in os.listdir():   # for every item
        if (os.path.isfile(item)):  # if item is a file
            
            file = open(item, 'r', encoding='utf-8')    # open it with sweedish encoding
            if (file):

                text = file.read()
        
                text_arr = text.split()    #create a array with every word that it´s finded

                #encode every word and save it in the hash tabel
                for i in text_arr:
                    nWord =i.encode()
                    key = hashlib.sha256(nWord).hexdigest()
                    value = os.path.abspath(item)
                    dict[key]= value
                    
               
            else:
                print("Error, file couldn,t be oppened. Path: ",os.path.abspath(file_path))

    for item in os.listdir():
        if (os.path.isdir(item)):  # if item is a directory
            newCwd = os.path.join(file_path, item)   # save a new path with the directory name
            hashWord(newCwd,dict)  # call the function with the new path and send the hash tabel(recursion)

    return 

#Function that look for words in a hash table
def searchWord(word,hashT):
    ew = word.encode()
    hWord = hashlib.sha256(ew).hexdigest()  # hasha the word that we are looking for
    
    print(hashT[hWord])
    
    
    
    


cwd = os.getcwd()  # get current directory 

file_path = os.path.join(cwd, 'doc')  # writing and saving in a variable the directory where i have the text files
hashT={}

hashWord(file_path,hashT)   #call the function to create the hash table
print(hashT)


print("witch word are you looking for?")
w = input()
searchWord(w,hashT)     #Call the function that look for the word use it as a input

