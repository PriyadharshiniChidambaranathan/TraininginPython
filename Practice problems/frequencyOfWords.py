def freq_words():
  str=input("enter string: ")
  li=str.split()
  dict={}

  for i in li:
    if i not in dict.keys():
      dict[i]=0
    dict[i]=dict[i]+1
  print(dict)

freq_words()


----------------------------------
#output:
#           enter string: My name is pri . My sis name is kav
#           {'My': 2, 'name': 2, 'is': 2, 'pri': 1, '.': 1, 'sis': 1, 'kav': 1}
