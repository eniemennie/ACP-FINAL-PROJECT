from tkinter import *  # Import all classes and functions from the tkinter module for GUI creation
from DataBase import EventDetails  # Import the EventDetails function from the DataBase module
from DataBase import TicketDetails  # Import the TicketDetails function from the DataBase module

def ViewEvents():
    # Retrieve event details from the database (the 5th element is the event details)
    event_details = EventDetails()[5]
    
    # Create a new Tkinter window for viewing events
    top4 = Tk()
    top4.geometry('850x800')  # Set the window size
    top4.title('View Events')  # Set the window title
    top4.resizable(False, False)  # Disable window resizing
    top4.configure(bg='#08C2FF')  # Set the background color of the window

    # Create and place labels for the header of the event details table
    Label(top4, text="Event Name", font=('Times New Roman', 15, 'bold'), background='#006BFF', fg='white', relief='raised').grid(row=0, column=0, padx=10, pady=10)
    Label(top4, text="Event ID", font=('Times New Roman', 15, 'bold'), background='#006BFF', fg='white', relief='raised').grid(row=0, column=1, padx=10)
    Label(top4, text="Event Date", font=('Times New Roman', 15, 'bold'), background='#006BFF', fg='white', relief='raised').grid(row=0, column=2, padx=10)
    Label(top4, text="Event Time", font=('Times New Roman', 15, 'bold'), background='#006BFF', fg='white', relief='raised').grid(row=0, column=3, padx=10)
    Label(top4, text="Event Duration", font=('Times New Roman', 15, 'bold'), background='#006BFF', fg='white', relief='raised').grid(row=0, column=4, padx=10)
    Label(top4, text="Event Type", font=('Times New Roman', 15, 'bold'), background='#006BFF', fg='white', relief='raised').grid(row=0, column=5, padx=10)

    # Loop through the event details and create labels for each event's information
    for i in range(len(event_details)):
        Label(top4, text=event_details[i][0], font=('Arial', 10), width=15, wraplength=100, bg='#08C2FF').grid(row=i+2, column=0)  # Event Name
        Label(top4, text=event_details[i][1], font=('Arial', 10), width=15, wraplength=100, bg='#08C2FF').grid(row=i+2, column=1)  # Event ID
        Label(top4, text=event_details[i][2], font=('Arial', 10), width=15, wraplength=100, bg='#08C2FF').grid(row=i+2, column=2)  # Event Date
        Label(top4, text=event_details[i][3], font=('Arial', 10), width=15, wraplength=100, bg='#08C2FF').grid(row=i+2, column=3)  # Event Time
        Label(top4, text=event_details[i][4], font=('Arial', 10), width=15, wraplength=100, bg='#08C2FF').grid(row=i+2, column=4)  # Event Duration
        Label(top4, text=event_details[i][5], font=('Arial', 10), width=15, wraplength=100, bg='#08C2FF').grid(row=i+2, column=5)  # Event Type
    
    # Start the Tkinter event loop to display the window
    top4.mainloop()