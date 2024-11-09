text=input("Enter a sentence: ")
words=text.split(" ")

newText=""
splitWord=""

for word in words:
    for letter in word:
        splitWord=letter+splitWord
    newText+=splitWord+" "
    splitWord=""
print(newText)