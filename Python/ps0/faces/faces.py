def convert(emoticon):
    if emoticon == ":)":
        return "🙂"
    elif emoticon == ":(":
        return "🙁"
    else:
        return None

def main(): 
    user_input = input().strip().replace(':)',convert(':)')).replace(':(',convert(':('))
    print(user_input)
    
if __name__ == "__main__":
    main()