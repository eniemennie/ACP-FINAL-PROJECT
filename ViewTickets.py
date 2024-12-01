from tkinter import *  # Import all classes and functions from the tkinter module for GUI creation
from DataBase import EventDetails  # Import the EventDetails function from the DataBase module
from DataBase import TicketDetails  # Import the TicketDetails function from the DataBase module

def ViewTickets():
    # Create a new Tkinter window for viewing tickets
    top4 = Tk()
    top4.geometry('940x280')  # Set the window size
    top4.title('View Tickets')  # Set the window title
    top4.configure(bg='#08C2FF')  # Set the background color of the window
    top4.resizable(False, False)  # Disable window resizing

    # Retrieve the list of event names from the EventDetails function
    event_names_list = EventDetails()[0]
    
    event_name = StringVar(top4)  # Create a StringVar to hold the selected event name
    event_name.set('Select event')  # Set the default value for the event selection

    def ShowTickets():
        # Create and place labels for the header of the ticket details table
        Label(top4, text="Customer Name", font=('Times New Roman', 12, 'bold'), background='#006BFF', fg='white', relief='raised').grid(row=3, column=0, padx=10, pady=10)
        Label(top4, text="Ticket ID", font=('Times New Roman', 12, 'bold'), background='#006BFF', fg='white', relief='raised').grid(row=3, column=1, padx=10, pady=10)
        Label(top4, text="Event Name", font=('Times New Roman', 12, 'bold'), background='#006BFF', fg='white', relief='raised').grid(row=3, column=2, padx=10, pady=10)
        Label(top4, text="Event Date", font=('Times New Roman', 12, 'bold'), background='#006BFF', fg='white', relief='raised').grid(row=3, column=3, padx=10, pady=10)
        Label(top4, text="Event Time", font=('Times New Roman', 12, 'bold'), background='#006BFF', fg='white', relief='raised').grid(row=3, column=4, padx=10, pady=10)
        Label(top4, text="Event Duration", font=('Times New Roman', 12, 'bold'), background='#006BFF', fg='white', relief='raised').grid(row=3, column=5, padx=10, pady=10)

        required_tickets = []  # Initialize a list to hold tickets for the selected event
        for i in TicketDetails()[7]:  # Iterate through the ticket details
            if event_name.get() in i:  # Check if the selected event name matches the ticket's event name
                required_tickets.append(i)  # Add matching tickets to the list

        # Loop through the required tickets and create labels for each ticket's information
        for i in range(len(required_tickets)):
            Label(top4, text=required_tickets[i][0], font=('Arial', 12), width=15, wraplength=100, bg='#08C2FF').grid(row=i+4, column=0)  # Customer Name
            Label(top4, text=required_tickets[i][1], font=('Arial', 12), width=15, wraplength=100, bg='#08C2FF').grid(row=i+4, column=1)  # Ticket ID
            Label(top4, text=required_tickets[i][2], font=('Arial', 12), width=15, wraplength=100, bg='#08C2FF').grid(row=i+4, column=2)  # Event Name
            Label(top4, text=required_tickets[i][4], font=('Arial', 12), width=15, wraplength=100, bg='#08C2FF').grid(row=i+4, column=3)  # Event Date
            Label(top4, text=required_tickets[i][5], font=('Arial', 12), width=15, wraplength=100, bg='#08C2FF').grid(row=i+4, column=4)  # Event Time
            Label(top4, text=required_tickets[i][6], font=('Arial', 12), width=15, wraplength=100, bg='#08C2FF').grid(row=i+4, column=5)  # Event Duration
            Label(top4, text=required_tickets[i][7], font=('Arial', 12), width=15, wraplength=100, bg='#08C2FF').grid(row=i+4, column= 6)  # Additional ticket information

    # Create and place a label for the event selection
    Label(top4, text='Select Event', font=('Times New Roman', 16, 'bold'), background='#006BFF', fg='white', relief='raised').grid(row=0, column=0, padx=10, sticky='w', pady=10)
    
    # Create a dropdown menu for selecting an event
    OptionMenu(top4, event_name, *event_names_list).grid(row=0, column=1)
    
    # Create a submit button that triggers the ShowTickets function when clicked
    Button(top4, text='Submit', command=ShowTickets, bg='green', fg='white', font=('Times New Roman', 12, 'bold')).grid(row=2, column=0, columnspan=3)
    
    # Start the Tkinter event loop to display the window
    top4.mainloop()