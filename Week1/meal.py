def main():
    a = convert(input("What time is it?"))
    if a>= 7.0 and a<=8.0:
        print("breakfast")
    elif a>=12.0 and a<=13.0:
        print("lunch")
    elif a>=18.0 and a<=19.0:
        print("dinner")
    else:
        return None
def convert(time):
    time = time.split(":")
    time = int(time[0])+float(time[1])/60
    return time
if __name__ == "__main__":
    main()

#def convert(time):
#   hours, minutes = map(int, time.replace("a.m.", "").replace("p.m.", "").split(":"))
#    if "p.m." in time and hours != 12:
#       hours += 12
#    if "a.m." in time and hours == 12:
#        hours = 0
#    return hours + minutes / 60