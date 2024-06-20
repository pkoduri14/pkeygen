import tkinter as tk
from functions.check import check_func
import classes.gui_classes as gc

def main():
    # Initialize the window & title
    root = tk.Tk()
    root.title("PKeyGen")

    # Sets parameters for resizing (not allowed) and the height & width of window
    root.resizable(width=False, height=False)
    root.minsize(height=600, width=600)

    # Sets icon in top left of window
    icon = tk.PhotoImage(file='static/icon.png')
    root.iconphoto(True, icon)

    # Initializes frames for window
    info_frame = gc.Frame(root)  # Introductory message
    length_frame = gc.Frame(root, 3, "groove")  # Frame with the length box & slider
    checkbox_frame = gc.Frame(root, 3, "groove") # Frame with the checkbox for password configuration
    min_lower_frame = gc.Frame(root, 3, "groove")  # Frame with the minimum lowercase chars box & slider
    min_upper_frame = gc.Frame(root, 3, "groove")  # Frame with the minimum uppercase chars box & slider
    min_special_frame = gc.Frame(root, 3, "groove")  # Frame with the minimum special chars box & slider
    special_chars_frame = gc.Frame(root, 3, "groove")  # Frame with the text box for special characters
    min_digits_frame = gc.Frame(root, 3, "groove") # Frame with minimum digits box and slider
    password_frame = gc.Frame(root, 4, "groove")  # Frame where password is placed once generated
    button_frame = gc.Frame(root)  # Submit button

    # Description of program (welcome message)
    main_intro = gc.Label(info_frame, text_info="Welcome to PKeyGen!")

    # Length frame parts
    length_desc = gc.Label(length_frame, "Password Length")  # Label for length
    length = gc.Scale(length_frame, 1, 100, "horizontal")  # Slider to set length

    # Checkbox frame parts
    checkbox_desc = gc.Label(checkbox_frame, "Character Selection")  # Label for checkbox 
    lower = gc.Checkbox(checkbox_frame, "Lowercase", checked=True)  # Checkbox button for lowercase chars
    upper = gc.Checkbox(checkbox_frame, "Uppercase", checked=True)  # Checkbox button for uppercase chars
    special = gc.Checkbox(checkbox_frame, "Special Characters", checked=True)  # Checkbox button for special chars
    digits = gc.Checkbox(checkbox_frame, "Digits (Numbers)", checked=True)  # Checkbox button for digits

    # Minimum lowercase chars slider parts
    min_lower_desc = gc.Label(min_lower_frame, "Minimum Lowercase Characters", wraplength=150)  # Label for minimum lowercase chars
    min_lower = gc.Scale(min_lower_frame, 0, 100, "horizontal")  # Slider for minimum lowercase chars

    # Minimum uppercase chars slider parts
    min_upper_desc = gc.Label(min_upper_frame, "Minimum Uppercase Characters", wraplength=150)  # Label for minimum uppercase chars
    min_upper = gc.Scale(min_upper_frame, 0, 100, "horizontal")  # Slider for minimum uppercase chars

    # Minimum special chars slider parts
    min_special_desc = gc.Label(min_special_frame, "Minimum Special Characters", wraplength=150)  # Label for minimum special chars
    min_special = gc.Scale(min_special_frame, 0, 100, "horizontal")  # Slider for minimum special chars

    # Minimum digits slider parts
    min_digit_desc = gc.Label(min_digits_frame, "Minimum Digits")  # Label for minimum digits
    min_digits = gc.Scale(min_digits_frame, 0, 100, "horizontal")  # Slider for minimum digits

    # Special chars text box input (for password configuration)
    special_chars_desc = gc.Label(special_chars_frame, "Special Characters List", wraplength=100)  # Label for special chars text box
    special_chars_text = gc.Entry(special_chars_frame, width_info=20, var=True)  # Text box for special characters

    # Area where generated password will show up
    password_desc = gc.Label(password_frame, "Generated Password")  # Description
    password_label = gc.Entry(password_frame, text_info="", width_info=30, border_width=2, relief_info="sunken")  # Box where password is generated
    password_label["state"] = "readonly"

    # Function that stores inputs, sends to check function, and returns back the generated password
    def store_inputs():

        # Stores each of the inputs to a variable
        pwd_length = length.var.get()  # Password length
        use_lower = lower.var.get()  # Whether lowercase characters are needed
        use_upper = upper.var.get()  # Whether uppercase characters are needed
        use_special = special.var.get()  # Whether special characters are needed
        use_digits = digits.var.get()
        min_lower_count = min_lower.var.get()  # Minimum lowercase chars
        min_upper_count = min_upper.var.get()  # Minimum uppercase chars
        min_digit_count = min_digits.var.get()
        min_special_count = min_special.var.get()  # Minimum special chars
        special_chars_list = special_chars_text.var.get()  # Special characters list

        # Stores return value (generated password) in variable
        generated_pwd = check_func(pwd_length, use_lower, use_upper, 
                        use_special, use_digits, min_lower_count, min_upper_count, 
                        min_special_count, min_digit_count, special_chars_list)
        
        # Makes entry box normal (in case repeated generations of passwords, so that last one can be cleared)
        password_label["state"] = "normal"
        
        # Clears data present in box
        password_label.delete(0, tk.END)

        # Places password in box (and if there are errors, displays them)
        if generated_pwd == 1:
            password_label.insert(0, "Please select at least one checkbox")
        elif generated_pwd == 2:
            password_label.insert(0, "Minimum settings exceed set password length")
        else:
            password_label.insert(0, generated_pwd)

        # Makes box readonly (so no edits)
        password_label["state"] = "readonly"

    # Submit button (to generate password)
    btn_submit = gc.Button(button_frame, "Generate Password", store_inputs)

    # Frame locations in application
    info_frame.pack(pady=20)
    length_frame.place(x=90, y=105)
    checkbox_frame.place(x=240, y=80)
    special_chars_frame.place(x=403, y=115)
    min_upper_frame.place(x=83, y=230)
    min_special_frame.place(x=250, y=230)
    min_lower_frame.place(x=407, y=230)
    min_digits_frame.place(x=250, y=360)
    password_frame.place(x=210, y=475)
    button_frame.place(x=250, y=550)

    root.mainloop()

if __name__ == "__main__":
    main()