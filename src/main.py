# Import the tkinter module for GUI
import tkinter as tk


# Main function where all the code resides
def main():
    # Initialize a window for the tkinter GUI
    root = tk.Tk()

    # Create a Label with the text "Hello, World!"
    label = tk.Label(root, text="Hello, World!")

    # Place the label on the window adding padding using pack()
    label.pack(padx=20, pady=20)

    # Start the main event loop for GUI
    root.mainloop()


# Check if the script is running directly or being imported
if __name__ == "__main__":
    # If script is running directly, call main function
    main()
