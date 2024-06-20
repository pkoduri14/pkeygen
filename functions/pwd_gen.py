import secrets
import string

# Generates password based on inputs

def pwdgen(length=8, special=True, lower=True, upper=True, digits=True, special_chars=None, min_lower=0, min_upper=0, min_special=0, min_digits=0):

    # Creates list of characters in password
    pwd_list = []

    # Default list of special characters
    chars = ["!", "?", "&", "#", "$", "*", "@"]

    # Checks if special=True and applies appropriate set of special characters
    if special:
        if special_chars is not None:
            pwd_list.extend([secrets.choice(special_chars) for _ in range(min_special)])
        else:
            pwd_list.extend([secrets.choice(chars) for _ in range(min_special)])

    # Checks and adds random lowercase characters (using secret module)
    if lower:
        pwd_list.extend([secrets.choice(string.ascii_lowercase) for _ in range(min_lower)])

    # Checks and adds random uppercase characters
    if upper:
        pwd_list.extend([secrets.choice(string.ascii_uppercase) for _ in range(min_upper)])
    
    # Checks and adds random digits
    if digits:
        pwd_list.extend([secrets.choice(string.digits) for _ in range(min_digits)])
    
    # Checks length of list and if below, adds a random assortment of characters
    while len(pwd_list) < length:
        choice = secrets.SystemRandom().randint(1, 3)

        if lower and choice == 1:
            pwd_list.append(secrets.choice(string.ascii_lowercase))
        elif upper and choice == 2:
            pwd_list.append(secrets.choice(string.ascii_uppercase))
        elif special and choice == 3:
            if special_chars != None:
                pwd_list.append(secrets.choice(special_chars))
            else:
                pwd_list.append(secrets.choice(chars))

    # Shuffles pwd_list
    secrets.SystemRandom().shuffle(pwd_list)

    # If length of list greater than length (variable), shortens to appropriate length
    if len(pwd_list) > length:
        pwd_list = pwd_list[:length]
    
    # Joins characters in pwd_list together
    pwd = ''.join(pwd_list)

    # Returns password to user
    return pwd
