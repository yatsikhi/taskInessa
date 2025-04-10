
# 
words = input("Введите текст: ").split()
bigWord = max(words, key=len)

EsBigWord = bigWord.replace('e', 's')
smallWord = min(words, key=len)


print("Самое длинное слово (с заменой 'e' на 's'):", EsBigWord)
print("Самое короткое слово:", smallWord)
