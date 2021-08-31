#This is the most shortcut way to slice the list.
Phrase = "Don't panic!"
plist = list(Phrase)
print(Phrase)
print(plist)
new_phrase = ''.join(plist[1:3])
#print(new_phrase)
new_phrase = new_phrase+''.join([plist[5], plist[4], plist[7], plist[6]])
print(new_phrase)