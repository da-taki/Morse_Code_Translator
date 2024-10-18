#Importing libraries
import winsound
import time

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
              "9" : "----.",
              "!" : "-.-.--",
              "@" : ".--.-.",
              "(" : "-.--.",
              ")" : "-.--.-",
              "=" : "-...-",
              "+" : ".-.-.",
              "." : ".-.-.-",
              "?" : "..--..",
              "," : "--..--",
              "-" : "-....-",
              "/" : "-..-.",
              ":" : "---...",
              "\"": ".-..-."}

#getting the input from the user
mssg = input("Enter the line which you want to translate to morse code: ")
try:
    voice = int(input("Do you want to hear how this morse codw will sound(1 for yes 0 for no)?: "))
except ValueError:
    print("Please enter either 1 or 0!")
    voice = 0
#turing the message into lower case
mssg = mssg.lower()

#fucntion for playing beeps
def play_sound(ms_code):
    for symbol in ms_code:
        if symbol == ".":
            winsound.Beep(1000,450) #Dot sound
        if symbol == "-":
            winsound.Beep(1000,900) #Dash sound
        time.sleep(0.2)

#using a for loop to translate the input into morse code 
for i in mssg:
    if morse_code.get(i) == None:
        continue
    else:
        ms_code = morse_code[i]
        print(morse_code[i], end=" ")
        if voice == 1:
            play_sound(ms_code)
        time.sleep(0.8)
