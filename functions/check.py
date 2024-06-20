import string
import re
from functions.pwd_gen import pwdgen

# Function to check inputs from main
def check_func(pwd_length, use_lower, use_upper, use_special, use_digits, min_lower_count, min_upper_count, min_special_count, min_digit_count, special_chars_list):
    # Checks if any of the checkboxes were selected, else returns 1
    if not (use_lower or use_upper or use_special or use_digits):
        return 1  # Please select at least one checkbox (error)
    
    # Initializes the total minimum count to a variable
    total_min_count = 0

    # Checks which checkboxes were selected and adds relevant minimum count
    if use_lower:
        total_min_count += min_lower_count
    if use_upper:
        total_min_count += min_upper_count
    if use_special:
        total_min_count += min_special_count
    if use_digits:
        total_min_count += min_digit_count
    
    # Checks if total minimum count greater than password length
    if total_min_count > pwd_length:
        return 2  # Minimum settings exceed set password length (error)
    else:
        # Checks if use_special is true
        if use_special:
            # Takes off whitespaces in box of special chars
            special_chars_list = re.sub(r"\s+", "", special_chars_list)
            
            # Checks if box is empty
            if special_chars_list == "":
                special_chars_list = None
        
        # Sends inputs to pwdgen function
        gen_pwd = pwdgen(pwd_length, use_special, use_lower, use_upper, use_digits, special_chars_list, min_lower_count, min_upper_count, min_special_count, min_digit_count)
        
        # Returns generated password
        return gen_pwd


        

    
            