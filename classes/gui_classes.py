import tkinter as tk

# List of classes for application


# Creates a frame using tk.Frame with set requirements in the application
class Frame(tk.Frame):
    def __init__(self, window_name, border_width=0, relief_frame="flat"):
        super().__init__(window_name, borderwidth=border_width, relief=relief_frame)


# Creates a label using tk.Label with set requirements in the application
class Label(tk.Label):
    def __init__(self, frame, text_info, wraplength=0):
        super().__init__(frame, text=text_info, wraplength=wraplength)
        self.pack()


# Creates a scale using tk.Scale and a text box which affects the scale (and vice versa)
class Scale(tk.Scale):
    # Constructor for class
    def __init__(self, frame, start, end, orient):
        # Creates scale using tk.Scale and packs it in frame
        self.var = tk.IntVar()
        super().__init__(frame, from_=start, to=end, orient=orient, variable=self.var, command=self.scale_change)
        self.pack()

        # Creates entry box using tk.Entry and packs in frame
        self.entry = tk.Entry(frame, width=5)
        self.entry.pack()

        # Binds entry box to function entry_change with event <KeyRelease> (user keystroke)
        self.entry.bind("<KeyRelease>", self.entry_change)

    # Changes entry box to match scale value
    def scale_change(self, value):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, value)

    # Changes scale to match entry box value
    def entry_change(self, event):
        try:
            value = int(self.entry.get())
            if value < self['from']:
                value == self['from']
            elif value > self['to']:
                value == self['to']
            self.set(value)
        except ValueError:
            pass
        

# Creates a checkbox using tk.Checkbutton
class Checkbox(tk.Checkbutton):
    # Constructor
    def __init__(self, frame, text_info, checked=False):
        # Creates checkbox and packs it in frame to left (west)
        self.var = tk.BooleanVar(value=checked)
        super().__init__(frame, text=text_info, variable=self.var)
        self.pack(anchor='w')


# Creates an entry box using tk.Entry
class Entry(tk.Entry):
    # Constructor
    def __init__(self, frame, text_info="", width_info=30, border_width=2, relief_info="sunken", var=True):
        # Checks if variable is set to True (meaning variable is needed)
        if var:
            # Creates entry box with variable
            self.var = tk.StringVar()
            super().__init__(frame, text=text_info, width=width_info, borderwidth=border_width, relief=relief_info, textvariable=self.var)
        else:
            # Creates entry box without variable (to store input)
            # For boxes like generated password, where text is copied, but nothing is stored
            super().__init__(frame, text=text_info, width=width_info, borderwidth=border_width, relief=relief_info)
        # Packs entry box in frame
        self.pack()


# Creates a button using tk.Button
class Button(tk.Button):
    def __init__(self, frame, text, command):
        super().__init__(frame, text=text, command=command)
        self.pack()