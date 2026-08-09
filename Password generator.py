#Password generator
import random #to randomly choose characters
import string # import digits,punctuations

def generate_password(min_length,numbers=True,special_characters=True):
    letters=string.ascii_letters#collection of alphabets
    digits=string.digits#collection of numbers
    special=string.punctuation #contains special characters

    characters=letters #initially a character
    if numbers:
        characters += digits #if it have number add it to prev character
    if special_characters:
        characters += special #if it have special characters ,then add o previous intial character

    pwd =""
    meets_criteria=False
    has_number=False
    has_special=False
    while not meets_criteria or len(pwd) < min_length: #this is continue loop to say if no criteria met then ask again
        new_char=random.choice(characters) #pick one random character from characters
        pwd += new_char

        if new_char in digits: #if digit put into charater
            has_number=True
        elif new_char in special:
            has_special=True #if special character put into the character

        meets_criteria=True
        if numbers: #if requirements are satisfied then should check if contained number
            meets_criteria=has_number
        if special_characters: #else check special characters
            meets_criteria=meets_criteria and has_special #both must be true to make the password correct


    return pwd 


min_length=int(input("Enter the minimum length: "))
has_number=input("Do you want to have numbers? (y/N)").lower()=="y"
has_special=input("Do you want to have special characters? (y/N)" ).lower() == "y"
pwd= generate_password(min_length,has_number,has_special)

print("The generated password is:" ,pwd)  