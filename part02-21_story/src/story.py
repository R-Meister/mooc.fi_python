# Write your solution here
story = ""
word = ''
lastword = ''
while True:
    story += (f"{word} ")
    word = str(input("Please type in a word: "))
    if word == 'end':
        print(story)
        break
    if word == lastword:
        print(story)
        break
    lastword = word
