def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) >= 2 and len(s) <= 6:
        if s[:2].isalpha():
            if is_all_alnumic(s[2:]):
                if is_pure_num(s[2:]):
                    if is_zero_start(s[2:]):
                        return False
                    else:
                        return True
                else:
                    if is_num_behind_letter(s[2:]):
                        return True
                    else:
                        return False
            else:
                return False
        else:
            return False
    else:
        return False
    

def is_pure_num(s):
    pure = True
    for c in s:
        if not c.isdigit():
            pure = False
            break
    return pure


def is_zero_start(s):
    if s[0] == '0':
        return True
    else:
        return False


def is_num_behind_letter(s):
    num_behind_letter = True
    for i in range(len(s)):
        if s[i].isdigit():
            for j in range(i, len(s)):
                if s[j].isalpha():
                    num_behind_letter = False
                    break
            if is_zero_start(s[i:]):
                num_behind_letter = False
                break
    return num_behind_letter


def is_all_alnumic(s):
    alnumic = True
    for c in s:
        if not c.isalnum():
            alnumic = False
            break
    return alnumic


main()