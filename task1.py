line = input("sentence input: ")

words = line.split() #разбирает строки на слова 
print(words)        #это можно убрать task Разбейте введенную строку на слова

revers = words[::-1] #Переворот списка слов 

for words in revers: #Вывод каждого слова в новой строке  ;)
    print(words)    #вывести слова (список в консоль)
    
