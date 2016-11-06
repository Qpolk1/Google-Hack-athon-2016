import csv #Creating Files
import os #Checking if File is open
from pathlib import Path

dictionary = {
    "Beaucoup": ["(BOOKOO) Many or alot"],
    "Hackathon": ["Please let us go home"],
    "Col'": ["Extremely cool"],
    "Yall":["The best way to address Multiple people"],
    "New Orleans":["The greatest city ever"],
    "Who Dat":["Term used by hardcore saints fans"],
    "Bruh":["Dude"],
    "How yah doing":["Common expression used to greet others "],
   
}




            
def createDictionary():
    file = open("CajunCollections.txt", "w", newline='')
    w = csv.writer(file)
    for key, val in dictionary.items():
        w.writerow([key] + val)
    file.close()

def readDict():
    file = open("CajunCollections.txt", "r")
    for value in csv.reader(file):
        new_val = val[1:]
        print('{} : {}' .format(value[0], new_val))
    
            
def display(dict1):
    print(dict1)


def search(dict1):
    real = str(input('what word would you like to define? '))
    for keys in dict1:
        if real == keys:
            print(dictionary[keys])

def add_dictionary(dict1):
    new_word = input('new word')
    new_def = input('what is the definition?')
    dict1[new_word]= [new_def]

def add_definition(dict1):
    new_def_word = input('What is word to add too? ')
    if new_def_word in dictionary.keys():
        new_def_def = input('What is the definition of the new word?')
        dict1[new_def_word].append(new_def_def)

def delete_definition(dict1):
    delete_word = input('What word would you like to delete? ')
    for i in dict1:
        if delete_word == i:
            print(dict1[i])
            location = int(input('enter the location '))
            location -= 1
            dict1[i].pop(location)

def delete_word(dict1):
    delete_word = input('What word would you like to delete? ')
    for power in dict1:
        if delete_word == power:
            user = input('Are you sure?')
            if user == 'yes':
                del dict1[delete_word]
                break

def reverse(dict1):
    word_in_dic = input('Enter part of or whole definition ')
    dic_values = dict1.values()
    for key in dict1:
        for i in dict1[key]:
            if word_in_dic in i:
                print(key)



def main():
    createDictionary()
    dict1 = dictionary
    statement = True
    while statement:
        action = input('What action would you like to take? ')
        action = action.lower()
        if action == 'search':
            search(dict1)
        elif action == 'display':
            display(dict1)
        elif action == 'add dictionary':
            add_dictionary(dict1)
        elif action == 'add definition':
            add_definition(dict1)
        elif action == 'delete word':
            delete_word(dict1)
        elif action == 'delete definition':
            delete_definition(dict1)
        elif action == 'reverse':
            reverse(dict1)
        else:
            print('Invalid input')

        cont = input('Continue (y/n): ')
        if cont == 'n':
            createDictionary();
            statement = False
                
    return None
        
            
main()


