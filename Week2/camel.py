a =  input("cameal name:")
b = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
if a.islower():
    print("snake_case:",a)
else:
    for letter in a:
        if letter in b:
            a = a.replace(letter,"_"+letter.lower())
        else:
            continue
    print("snake_case:",a)

#key brief way
#snake = "".join(["_" + ch.lower() if ch.isupper() else ch for ch in camel])

