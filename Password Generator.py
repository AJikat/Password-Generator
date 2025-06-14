import string
import re
import random

def Generator(): # I made the length 16, but you can change as desired, but 8 is the min recommendation
    upper_case = string.ascii_uppercase
    lower_case = string.ascii_lowercase
    numbers = string.digits
    special_chars = string.punctuation
    password_list = [random.choice(upper_case), random.choice(lower_case), random.choice(numbers), random.choice(special_chars)]
    random.shuffle(password_list)

    for i in range(12):
        choice_type = random.choice([upper_case, lower_case, special_chars, numbers])
        while True:
            choice = random.choice(choice_type)
            password_list.append(choice)
            if len(password_list) >= 2 and choice == password_list[-1] == password_list[-2]:
                password_list.pop()
                continue

            if re.search(r"(abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz|zyx|yxw|xwv|wvu|vut|uts|tsr|srq|rqp|qpo|pon|onm|nml|mlk|lkj|kji|jih|ihg|hgf|gfe|fed|edc|dcb|cba|012|123|234|345|456|567|678|789|890|987|876|765|654|543|432|321|210)", "".join(password_list).lower()):
                password_list.pop()
                continue

            else:
                break

    password = "".join(password_list)
    return password

def main():
    while True:
        option = input('Please enter one of the following:\nEnter g to generate a password\nEnter e to exit\nChoice: ').strip().lower()
        if option == 'g':
            while True:
                password = Generator()
                print(f'Your password is:\t {password}\n')
                option2 = input('Please enter one of the following:\nEnter g to generate a different password\nEnter e to exit\nChoice: ').lower().strip()
                if option2 == 'e':
                    break

                elif option2 == 'g':
                    continue
                
                else:
                    print('\nERROR, INVALID VALUE\n')
                    break
                    
        elif option == 'e':
            break

        else:
            print('\nERROR, INVALID VALUE\n')

if __name__ == "__main__" :
    main()
