while True:
    username = input("Please enter your username: ")
    if not username:
        print("⚠️ Username cannot be empty. Please try again.")
        continue
    if username: 
        break
#====================================================================================
while True:
    password = input("Please enter your password: ")
    if not password:
        print("⚠️ Password cannot be empty. Please try again.")
        continue
    if password: 
        break
#======================================================================================
while True:
    birthday = input("Please enter your birthday: ")
    if not birthday.isdigit():
        print("⚠️ Please enter just number.(0-9)")
        continue
        
        
    if not birthday:
        print("⚠️ birthday cannot be empty. Please try again.")
        continue
    if birthday:
        break
print("\n")
#===================================================================================
score = 0
charecter_count = len(password)

if charecter_count < 8 :
    print("❌ Password is shorter than 8 characters.")
    
elif charecter_count >= 8 :
    print("✅ Password length is sufficient.")
    score += 1


#=====================================================================================

have_letter_eng = False

for i in password:
    if("a" <= i <= "z") :
        have_letter_eng = True
        break
if have_letter_eng:
    print("✅ Contains at least one English letter.")
    score += 1
else:
    print("❌ Password does not contain any English letters.")

#======================================================================================
special_charecters_list = ["@", "!", "#", "$", "%", "&", "*", "+", "~", "_", "-", "^"]

special_charecters = False

for i in password:
    if i in special_charecters_list:
        special_charecters = True
        break

if special_charecters:
    print("✅ Contains at least one special character.")
    score += 1
else:
    print("❌ Password does not contain any special characters.")
#=========================================================================================

have_uppercase_letters = False

for i in password:
    if ("A" <= i <"Z"):
        have_uppercase_letters = True
        break

if have_uppercase_letters:
    print("✅ Contains at least one uppercase letter.")
    score += 1
else:
    print("❌ Password does not contain any uppercase letters.")
#=============================================================================

if password != username:
    print("✅ Password is not identical to the username.")
    score += 1
else:
    print("❌ password is identical to the username.")

#======================================================================

if password.swapcase() != username.swapcase():
    print("✅ Password is not the swapcase version of the username.")
    score += 1
else:
    print("❌ password is the swapcase version of te username.")

#==========================================================================

replace_with_char = {
    "@" : "a",
    "!" : "i",
    "0" : "o",
    "$" : "s"
}
user_lower = username.lower()

for char, rep in replace_with_char.items():
    user_lower = user_lower.replace(char, rep)

pass_lower = password.lower()

for char, rep in replace_with_char.items():
    pass_lower = pass_lower.replace(char, rep)

if user_lower in pass_lower:
    print("❌ Is a special-character version of the username (s → $, a → @).")
else:
    print("✅ Password is not a special-character version of the username.")
    score += 1

#=============================================================================

common_passwords = "123456", "12345678", "12345", "111111", "123456789", "qwerty", "asdfgh", "zxcvbnm", "password", "admin", "P@s$w0rd"

is_common_password = False

for i in common_passwords:
    if i == password:
        is_common_password = True
        break
if is_common_password:
    print("❌ Password is one of the most common passwords.")
else:
    print("✅ Not a common password")
    score += 1
#======================================================================

if birthday in password:
    print(f"❌ Your birthday ({birthday}) is in your password. Please change it for security.")
else:
    print("✅ Your birthday is not in the password.")
    score += 1
print("\n")
#====================================================================
print(f"🔒 final score : {score} out of 9")

if 9 >= score >= 8 :
    print("🔒 Security Level: Strong")
    print("🎉 Congratulations! Your password is highly secure and passed all security checks.")

elif 7 >= score > 4 :
    print("🔒 Security Level: Medium")
    print("📌 Tip: Your password is fairly secure, but try to avoid using patterns based on your")

elif score <= 3 :
    print("🔒 Security Level: Very Weak")
    print("📌 Tip: Your password is too simple and easy to guess. Use a mix of letters, numbers, and symbols.")
