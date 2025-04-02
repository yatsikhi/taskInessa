words= input("введите текст:").split()

bigWord = max(words, key= len)
smallWord  = min(words, key=len)

print("big word", bigWord)
print("little word", smallWord)
