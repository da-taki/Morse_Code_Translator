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

mssg = input("Enter the line which you want to translate to morse code: ")
mssg = mssg.lower()
for i in mssg:
    if i.isalnum() == False:
        continue
    if morse_code.get(i) == None:
        continue
    else:
        print(morse_code[i], end=" ")