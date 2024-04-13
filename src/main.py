# Import the tkinter module for GUI
import tkinter as tk


def create_button(root, text, command):
    """
    Create a button widget and pack it into the given root window.

    :param root: The root window where the button will be placed.
    :type root: tk.Tk
    :param text: The text to be displayed on the button.
    :type text: str
    :param command: The command to be executed when the button is clicked.
    :type command: function
    :return: None
    """
    button = tk.Button(root, text=text, padx=20, pady=20, command=command)
    button.pack(padx=20, pady=20)


def hello_world():
    """
    Prints "Hello, World!" to the console.

    :return: None
    """
    print("Hello, World!")
    pass


def hello_earth():
    """
    Prints "Hello, Earth!" to the console.

    :return: None
    """
    print("Hello, Earth!")
    pass


def main():
    """
    Entry point of the program.

    Creates a Tkinter root window and two buttons with their respective callback functions.
    Starts the Tkinter event loop.

    :return: None
    """
    root = tk.Tk()
    create_button(root, "Hello, World!", hello_world)
    create_button(root, "Hello, Earth!", hello_earth)
    root.mainloop()


# Check if the script is running directly or being imported
if __name__ == "__main__":
    # If script is running directly, call main function
    main()
