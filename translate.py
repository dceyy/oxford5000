from googletrans import Translator
import random
import time
translator = Translator()
file = open("words.txt", "r")
dict={}
for line in file.readlines():
    line=line.strip()
    word = line.split(' ')
    dict[str(word[0])]={
        "type":word[1],
        "level":word[2],
    }


if __name__ == '__main__':
    while True:
        randomword=random.choice(list(dict.keys()))
        mean=translator.translate(randomword, dest='tr').text
        try:
            print("\nword: {} type:{} level:{}".format(randomword,dict[randomword]["type"],dict[randomword]["level"]))
            meaingFromUser=input("what is the meaning of {}: ".format(randomword))
            if meaingFromUser==mean:
                print("Correct!")
                time.sleep(0.2)
                delete=input("Do you want to delete this word? (y/n): ")
                if delete=="y":
                    del dict[randomword]
                    print("Deleted!")
                    time.sleep(0.2)
                    if len(dict)==0:
                        print("All words deleted!")
                        break
            else:
                print("Wrong")
                time.sleep(0.2)
                print("Meaning: '{}'".format(mean))
        except:
            print("Error")
        input("Press enter to continue ")

