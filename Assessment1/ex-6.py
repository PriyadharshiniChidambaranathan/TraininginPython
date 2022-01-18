
user_list = input("Input words: ")
lst = user_list.split(",")
lst.sort()
print((', ').join(lst))
