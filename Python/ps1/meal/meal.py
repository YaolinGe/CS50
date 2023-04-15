def main():
    tid = input("What time is it? ").strip()
    num = convert(tid)
    if num >= 7.0 and num <= 8.0: 
        print("breakfast time")
    elif num >= 12.0 and num <= 13.0:
        print("lunch time")
    elif num >= 18.0 and num <= 19.0:
        print("dinner time")
    else:
        pass

def convert(time):
    hour, minute = time.split(":")
    return float(hour) + float(minute) / 60


if __name__ == "__main__":
    main()