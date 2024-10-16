# Making a dictionary where letters and digits are keys and the 
# values are their respective translation in morse morse_code
morse_code = {"a" : ".-",
              "b" : "-...",
              "c" : "-.-.",
              "d" : "-..",
              "e" : ".",
              "f" : "..-.",
              "g" : "--.",
              "h" : "....",
              "i" : "..",
              "j" : ".---",
              "k" : "-.-",
              "l" : ".-..",
              "m" : "--",
              "n" : "-.",
              "o" : "---",
              "p" : ".--.",
              "q" : "--.-",
              "r" : ".-.",
              "s" : "...",
              "t" : "-",
              "u" : "..-",
              "v" : "...-",
              "w" : ".--",
              "x" : "-..-",
              "y" : "-.--",
              "z" : "--..",
              "0" : "-----",
              "1" : ".----",
              "2" : "..---",
              "3" : "...--",
              "4" : "....-",
              "5" : ".....",
              "6" : "-....",
              "7" : "--...",
              "8" : "---..",
              "9" : "----."}

#getting the input from the user
mssg = input("Enter the line which you want to translate to morse code: ")

#turing the message into lower case
mssg = mssg.lower()

#using a for loop to translate the input into morse code 
for i in mssg:
    if i.isalnum():                   #making sure the values are alphanumeric as I havent added translation for symbols
        if morse_code.get(i) == None:
            continue
        else:
            print(morse_code[i], end=" ")
    else:
        continue
