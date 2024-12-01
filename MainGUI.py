from tkinter import *
from tkinter import messagebox  # Importing messagebox for displaying pop-up messages
from tkinter import font  # Importing font for custom font styles
from Book import Book  # Importing the Book function from the Book module
from ViewTickets import ViewTickets  # Importing the ViewTickets function
from CreateEvent import CreateEvent  # Importing the CreateEvent function
from ViewEvents import ViewEvents  # Importing the ViewEvents function
from CancelTicket import CancelTicket  # Importing the CancelTicket function

class GreetingWindow:
    def __init__(self, master):                
        self.master = master  # Reference to the main window
        self.create_greeting_window()  # Call method to create the greeting window

    def create_greeting_window(self):
        # Create a new top-level window for the greeting
        self.greeting_window = Toplevel(self.master)
        self.greeting_window.title("Stage Master Concert Event Management System")  # Set the title
        self.greeting_window.geometry("600x500")  # Set the size of the window
        self.greeting_window.resizable(False, False)  # Disable resizing
        self.greeting_window.configure(bg='#08C2FF')  # Set background color

        # Define bold font for greeting message
        bold_font = font.Font(family="Times New Roman", size=30, underline=1, weight="bold", slant="italic")
       
        # Create and pack greeting message
        greeting_message = Label(
            self.greeting_window,
            text="Welcome to the Concert Event Management System! ⋆⁺₊⋆ ☾⋆⁺₊⋆",
            font=bold_font,
            bg='#006BFF',
            fg='white',
            wraplength=430,
            relief='raised'
        )
        greeting_message.pack(pady=10, expand=True)  # Add padding and allow expansion

        # Create a label and entry for the user's name
        self.name_label = Label(
            self.greeting_window,
            text="Please enter your name our dearest Moonchild:",
            font=('Times New Roman', 15, 'bold', 'italic'),
            bg='#006BFF',
            fg='white',
            relief='raised'
        )
        self.name_label.pack(pady=5)  # Add padding

        # Entry for user's name
        self.name_entry = Entry(self.greeting_window, width=40, font=('Times New Roman', 12, 'bold'))
        self.name_entry.pack(pady=3)  # Add padding

        # Create a button to close the greeting window
        self.continue_button = Button(self.greeting_window, text="Continue", command=self.on_continue)
        self.continue_button.pack(pady=10)  # Add padding
        self.continue_button.configure(activebackground='green')  # Set active background color

        # Center the window on the screen
        self.center_window()

    def center_window(self):
        # Get the dimensions of the screen
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

        # Calculate the x and y coordinates to center the window
        x = (screen_width // 2) - (300)  # Half of the window width
        y = (screen_height // 2) - (250)  # Half of the window height

        # Set the position of the window
        self.greeting_window.geometry(f"+{x}+{y}")

    def on_continue(self):
        # Get the user's name from the entry
        user_name = self.name_entry.get().strip()
        
        if user_name:
            # Display a welcome message
            messagebox.showinfo("Welcome", f"Hello Moonchild, {user_name}! Enjoy booking with us.❤︎")
            self.greeting_window.destroy()  # Close the greeting window
            self.master.deiconify()  # Show the main window
        else:
            messagebox.showwarning("Input Error", "Please enter your name.")  # Show warning if no name is entered

# Main Window function
def main():
    top = Tk()  # Create the main window
    top.geometry('600x500')  # Set the size of the window
    top.resizable(False, False)  # Disable resizing
    top.title('StageMaster Concert Event Management')  # Set the title

    # Hide the main window initially
    top.withdraw()

    # Show the greeting window
    greeting_window = GreetingWindow(top)

    # Wait until the greeting window is closed
    top.wait_window(greeting_window.greeting_window)

    # Create buttons for the main application after the greeting window is closed
    button_frame = Frame(top, bg='#08C2FF')  # Set the same background color for the button frame
    button_frame.pack(fill=BOTH, expand=True)  # Allow the button frame to expand

    # Create buttons for various functionalities
    Button(button_frame, text='Book Ticket', bg='#006BFF', fg='white', font=('Times New Roman', 18, 'bold'), command=lambda: Book()).grid(row=0, column=0, sticky='nsew', padx=15, pady=10)
    Button(button_frame, text='Create Event', bg='#006BFF', fg='white', font=('Times New Roman', 18, 'bold'), command=lambda: CreateEvent()).grid(row=1, column=0, sticky='nsew', padx=15, pady=10)
    Button(button_frame, text='View Tickets', bg='#006BFF', fg='white', font=('Times New Roman', 18, 'bold'), command=lambda: ViewTickets()).grid(row=0, column=1, sticky='nsew', padx=15, pady=10)
    Button(button_frame, text='View Events', bg='#006BFF', fg='white', font=('Times New Roman', 18, 'bold'), command=lambda: ViewEvents()).grid(row=1, column=1, sticky='nsew', padx=15, pady=10)
    Button(button_frame, text='Cancel Ticket', bg='#006BFF', fg='white', font=('Times New Roman', 18, 'bold'), command=lambda: CancelTicket()).grid(row=2, column=0, sticky='nsew', padx=15, pady=10)
    Button(button_frame, text='Quit App', bg='Red', fg='white', font=('Times New Roman', 18, 'bold'), command=lambda: top.destroy()).grid(row=2, column=1, sticky='nsew', padx=15, pady=10)

    # Configure grid weights to allow resizing
    button_frame.grid_rowconfigure(0, weight=1)
    button_frame.grid_rowconfigure(1, weight=1)
    button_frame.grid_rowconfigure(2, weight=1)
    button_frame.grid_columnconfigure(0, weight=1)
    button_frame.grid_columnconfigure(1, weight=1)

    # Center the main window after creating buttons
    def center_main_window():
        screen_width = top.winfo_screenwidth()
        screen_height = top.winfo_screenheight()
        x = (screen_width // 2) - (300)  # Half of the window width
        y = (screen_height // 2) - (250)  # Half of the window height
        top.geometry(f"+{x}+{y}")  # Set the position of the window

    center_main_window()  # Call the function to center the main window
    top.mainloop()  # Start the Tkinter event loop

if __name__ == "__main__":
    main()  # Run the main function when the script is executed