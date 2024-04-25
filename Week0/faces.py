def main():
    a = input("plz emoji")
    print(convert(a))

def convert(text):
    return text.replace(":)","🙂").replace(":(","🙁")
main()

#other way
#print(input("plz").rreplace(":)","🙂").replace(":(","🙁"))