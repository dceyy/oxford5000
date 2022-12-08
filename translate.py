import random
from colorama import Fore, Back, Style
from googletrans import Translator
translate = Translator()
w=[]
redBack=Back.RED
greenBack=Back.GREEN
green=Fore.GREEN
red=Fore.RED
blue=Fore.BLUE
yellow=Fore.LIGHTYELLOW_EX
cyan=Fore.CYAN
reset=Style.RESET_ALL

with open("words.txt", "r") as f:
    words = f.readlines()
    for word in words:
        l=[]
        word = word.strip()
        word=word.split(" ")
        for i in word:
            if i!="":
                l.append(i)
        w.append(l)

        
if __name__=="__main__":
    print(Fore.MAGENTA+
            """\n\tIMPROVE YOUR ENGLISH\n"""+reset)

    while True:
        print(cyan+"press q to quit"+reset)
        wr=random.choice(w)
        word=wr[0].lower()
        meaning=translate.translate(word, dest='tr').text.lower().capitalize()
       
        print(f"Word: {blue} {word.capitalize()} {reset} Type: {yellow} {wr[1].capitalize()} {reset} Level: {green} {wr[2]} {reset}")
        k=input("Enter the meaning of the word: ").capitalize()
        if k=="q" or k=="Q":
            break
        elif k==meaning:
            print(f"{greenBack}CORRECT!!{reset}\n")

        elif k!=meaning:
            print(f"{redBack}WRONG!!{reset} The meaning of the word is {cyan} {meaning} {reset}\n")
            

