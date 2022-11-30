from googletrans import Translator
translator = Translator()
file = open("words.txt", "r")
dict={}
kelime=str(input("Kelime giriniz: "))
words = []
for line in file:
    word = line.split(' ')
    words.append(word[0])
if kelime in words:
    print(translator.translate(kelime, dest='tr').text)