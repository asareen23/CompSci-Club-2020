word_list = ["Comer","Cepillar","Beber","Vivir","Cantar","Escribir","Caminar","Sentar"]


#Without 'Extra'
for word in word_list:
  if word[-2:] == "ar":
    print(word,"is an -AR verb!")
  elif word[-2:] == "er":
    print(word,"is an -ER verb")
  elif word[-2:] == "ir":
    print(word,"is an -IR verb")
  else:
    print("I don't know what type of verb",word,"is!")

# With extra, the length of the word using the built-in len() function 
for word in word_list:
  if word[-2:] == "ar":
    print(word, "is a", len(word), "letter word and is an -AR verb")
  elif word[-2:] == "er":
    print(word, "is a", len(word), "letter word and is an -ER verb")
  elif word[-2:] == "ir":
    print(word, "is a", len(word), "letter word and is an -IR verb")
  else:
    print("I don't know what type of verb",word,"is, but it is", len(word), "letters!")