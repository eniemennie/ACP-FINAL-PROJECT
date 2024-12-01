from tkinter import *
from GenerateNewCode import random_id  # Import function to generate random ticket IDs
from DataBase import TicketDetails  # Import function to get ticket details
from DataBase import EventDetails  # Import function to get event details
from DataBase import BookTicket  # Import function to book a ticket
from Message import show_message  # Import function to show messages to the user

def Book():
    # Fetch existing ticket IDs and event names/types from the database
    ticket_ids = TicketDetails()[1]
    event_names_list, event_types_list = EventDetails()[0], EventDetails()[5]  # Fetch event names and event types
    
    # Create the main window for booking
    top1 = Tk()
    top1.geometry('440x320')  # Set the window size
    top1.title('Book ticket')  # Set the window title
    top1.resizable(False, False)  # Disable window resizing
    top1.configure(bg='#08C2FF')  # Set background color
    
    # Define StringVar variables to hold user input and selected values
    customer_name = StringVar(top1)
    ticket_id = StringVar(top1)
    event_name = StringVar(top1)
    selected_event_type = StringVar(top1)  # Variable to hold the selected event type
    
    event_name.set('Select event')  # Set default value for event selection
    
    # Generate a unique ticket ID
    while True:
        new_ticket_id = random_id()  # Generate a new random ticket ID
        if new_ticket_id not in ticket_ids:  # Check if the ticket ID is unique
            ticket_id.set(new_ticket_id)  # Set the unique ticket ID
            break  # Exit the loop once a unique ID is found
        continue
    
    # Function to update the event type based on the selected event name
    def update_event_type(*args):
        selected_index = event_names_list.index(event_name.get())  # Get the index of the selected event
        selected_event_type.set(event_types_list[selected_index])  # Update the selected event type

    # Trace changes in event_name to call update_event_type when it changes
    event_name.trace("w", update_event_type)

    # Function to handle the booking process
    def BookNow():
        # Validate customer name length
        if len(customer_name.get()) < 5:
            show_message('Error', 'Enter valid details')  # Show error message if name is invalid
            return
        # Attempt to book the ticket
        booking_status = BookTicket(customer_name.get(), ticket_id.get(), event_name.get())
        if booking_status == 'Success':
            show_message('Success', 'booking successful')  # Show success message if booking is successful
            return
        else:
            show_message('Error', booking_status)  # Show error message if booking fails
    
    # Create and place labels and input fields in the window
    Label(top1, text='Enter details', font=('Times New Roman', 20, 'bold'), background='#006BFF', fg='white', relief='raised').grid(row=0, column=0, padx=10, pady=10, columnspan=2)
    
    Label(top1, text='Name', font=('Times New Roman', 15, 'bold'), background='#006BFF', fg='white', relief='raised').grid(row=1, column=0, padx=10, pady=10, sticky='w')
    Entry(top1, textvariable=customer_name).grid(row=1, column=1)
    
    Label(top1, text='Ticket Id', font=('Times New Roman', 15, 'bold'), background='#006BFF', fg='white', relief='raised').grid(row=2, column=0, padx=10, pady=10, sticky='w')
    Entry(top1, textvariable=ticket_id, state='disabled').grid(row=2, column=1)  # Ticket ID is displayed but not editable
    
    Label(top1, text='Event', font=('Times New Roman', 15, 'bold'), background='#006BFF', fg='white', relief='raised').grid(row=3, column=0, padx=10, sticky='w', pady=10)
    OptionMenu(top1, event_name, *event_names_list, selected_event_type).grid(row=3, column=1)  # Dropdown for event selection
    
    # Button to confirm booking
    Button(top1, text='Confirm', bg='green', fg='white', font=('Arial', 17), width=9, command=lambda: BookNow()).grid(row=5, column=1, pady=10)
    
    top1.mainloop()  # Start the GUI event loop