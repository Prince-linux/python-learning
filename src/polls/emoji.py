# A program to translate a character to an emoji using dictionaries in python

message = input(">")
words = message.split(' ')
emojis = {
    ":)": "😀",
    ":(": "😔"
}
output = ""
for word in words:
     output += emojis.get(word, word) + " "

print(output)