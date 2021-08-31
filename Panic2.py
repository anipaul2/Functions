#In Panic code we used lists to convert Don't panic to ontap but here we used slices with lists.
Phrase = "Don't panic!"
plist = list(Phrase)
print(Phrase)
print(plist)
new_list = plist[-5:-7:-1]
new_listt = plist[1:5]
print(new_listt)
new_listt.pop(2)
Final  = ''.join(new_listt+new_list)
print(Final)

