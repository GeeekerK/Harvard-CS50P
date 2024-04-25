strword = input("plz input:")
for i in strword:
    if i in "aeiouAEIOU":
        strword = strword.replace(i,"")
    else:
        continue
print(strword)

# s = input("Input: ")

# ans = "".join([ch for ch in s if ch.lower() not in "aeiou"])
# print("Output:", ans)