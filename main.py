
from models import PasswordChecker
from colorama import Fore , Style
def main():
    while True:
        username_input = input("Enter your username : ").strip()
        if not username_input :
            print("\n[Error] username must be set.\n")
            continue
        else:
            break
    
    
    while True:
        password_input = input("Enter your password : ").strip()
        if not password_input:
            print("\n[Error] password must be set.\n")
        else:
            break
    
    
    pass_checker = PasswordChecker(username_input, password_input)
    # ------------------------------------------------------------
    print(f"\nusername : ({username_input})")
    print(f"Password : ({password_input})\n")
    print(Fore.LIGHTBLUE_EX,"\nFilters checks:",Style.RESET_ALL)
    pass_checker.length_of_letters()
    pass_checker.contain_letter_english()
    pass_checker.contains_special_characters()
    pass_checker.contains_uppercase_letter()
    pass_checker.has_username()
    pass_checker.has_swapcase_username()
    pass_checker.replace_with_special_char()
    pass_checker.password_similar_common_passwords()
    # ------------------------------------------------------------


main()