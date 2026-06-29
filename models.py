from string import ascii_letters ,ascii_lowercase, ascii_uppercase, punctuation
from colorama import Style, Back , Fore


class PasswordChecker:
    def __init__(self, username:str, password:str, birthday:str="None"):
        self.username = username
        self.password = password
        self.birthday = birthday
        self.score = 0
#=============================================================================================
    def length_of_letters(self):
        '''This function gets the length of the password and 
        returns a score if it is greater than 8.'''
        if len(self.password) >= 8:
            print(Fore.GREEN,"\t✅ Password length is enough.",Style.RESET_ALL)
            self.score += 1
        else:
            print(Fore.RED,"\t❌ Password length is not enough.",Style.RESET_ALL)
#============================================================================================= 
    def contain_letter_english(self):
        '''Checks if the password contains English words.'''
        flag = False
        for char in self.password:
            if char in ascii_letters:
                flag = True
        if flag:
            print(Fore.GREEN,"\t✅ Contains at least one English letter.",Style.RESET_ALL)
            self.score += 1
        else:
            print(Fore.RED,"\t❌ Password does not contain any English letters.",Style.RESET_ALL)
#=============================================================================================
    def contains_special_characters(self):
        '''Checks if the password contains special characters'''
        flag = False
        for char in self.password:
            if char in punctuation:
                flag = True
        
        if flag:
            print(Fore.GREEN,"\t✅ Contains at least one special character.",Style.RESET_ALL)
            self.score += 1
        else:
            print(Fore.RED,"\t❌ Password does not contain any special characters.",Style.RESET_ALL)
#=============================================================================================
    def contains_uppercase_letter(self):
        '''Check if the password contains special characters'''
        flag = False
        for char in self.password:
            if char in ascii_uppercase:
                flag = True
        
        if flag:
            print(Fore.GREEN,"\t✅ Contains at least one uppercase letter.",Style.RESET_ALL)
            self.score += 1
        else:
            print(Fore.RED,"\t❌ Password does not contain any uppercase letters.",Style.RESET_ALL)
#==============================================================================================
    def has_username(self):
        '''Checks if the password is the same as the username.'''
        if self.username not in self.password:
            print(Fore.GREEN,"\t✅ Not identical to the username.",Style.RESET_ALL)
            self.score += 1
        else:
            print(Fore.RED,"\t❌ Password is identical to the username.",Style.RESET_ALL)
#==============================================================================================
    def has_swapcase_username(self):
        '''Checks if the password not the swapcase version of the username'''
        if self.username.swapcase() not in self.password:
            print(Fore.GREEN,"\t✅ Not the swapcase version of the username.",Style.RESET_ALL)
            self.score += 1
        else:
            print(Fore.RED,"\t❌ The password is a swapcase version of the username",Style.RESET_ALL)
#==============================================================================================
    def replace_with_special_char(self):

        special_character = {
            "@" : "a",
            "!" : "i",
            "0" : "o",
            "$" : "s"
        }

        username_ = self.username.lower()
        password_ = self.password.lower()


        for special_char , char in special_character.items():
            username_ = username_.replace(special_char, char)
        
        for special_char, char in special_character.items():
            password_ = password_.replace(special_char, char)
        
        if username_ in password_:
            print(Fore.RED,"\t❌ Is a special-character version of the username (s → $, a → @).",Style.RESET_ALL)
        else:
            print(Fore.GREEN,"\t✅ Not a special-character version of the username.",Style.RESET_ALL)
            self.score += 1
#==============================================================================================
    def password_similar_common_passwords(self):
        common_password = "123456", "12345678", "12345", "111111", "123456789", "qwerty", "asdfgh", "zxcvbnm", "password", "admin", "P@s$w0rd", "asdfg54321@"

        if self.password not in common_password:
            print(Fore.GREEN,"\t✅ Not a common password.",Style.RESET_ALL)
            self.score += 1
        else:
            print(Fore.RED,"\t❌ Password is one of the most common passwords.",Style.RESET_ALL)