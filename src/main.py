# Import the tkinter module for GUI
import tkinter as tk


# Function to be called when Hello World button is pressed
def hello_world():
    print("Hello, World!")


# Function to be called when Hello Earth button is pressed
def hello_earth():
    print("Hello, Earth!")


# Main function where all the code resides
def main():
    # Initialize a window for the tkinter GUI
    root = tk.Tk()

    # Create a Button with the text "Hello, World!" and link it to hello_world function
    button_world = tk.Button(root, text="Hello, World!", padx=20, pady=20, command=hello_world)
    # Place the button on the window using pack()
    button_world.pack(padx=20, pady=20)

    # Create a Button with the text "Hello, Earth!" and link it to hello_earth function
    button_earth = tk.Button(root, text="Hello, Earth!", padx=20, pady=20, command=hello_earth)
    # Place the button on the window using pack()
    button_earth.pack(padx=20, pady=20)

    # Start the main event loop for GUI
    root.mainloop()


# Check if the script is running directly or being imported
if __name__ == "__main__":
    # If script is running directly, call main function
    main()
