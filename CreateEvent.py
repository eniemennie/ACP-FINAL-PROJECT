from tkinter import *  # Import all classes and functions from tkinter for GUI creation
from GenerateNewCode import random_id  # Import function to generate a random event ID
from DataBase import EventDetails  # Import function to retrieve event details from the database
from DataBase import CreateNewEvent  # Import function to create a new event in the database
from Message import show_message  # Import function to display messages to the user
from tkcalendar import DateEntry  # Import DateEntry widget for date selection
from datetime import date  # Import date class to work with dates

def CreateEvent():
    # Retrieve existing event IDs to ensure new event ID is unique
    event_ids = EventDetails()[1]
    
    # Create the main window for creating an event
    top2 = Tk()
    top2.geometry('360x450')  # Set the window size
    top2.title('Create new Event')  # Set the window title
    top2.resizable(False, False)  # Disable window resizing to maintain layout
    top2.configure(bg='#08C2FF')  # Set the background color of the window
    
    # Define StringVar variables to hold user input
    event_name = StringVar(top2)  # Variable for event name
    event_id = StringVar(top2)  # Variable for event ID
    event_date = StringVar(top2)  # Variable for event date
    event_date.set(date.today())  # Set default event date to today
    event_time = StringVar(top2)  # Variable for event time
    event_duration = StringVar(top2)  # Variable for event duration
    event_type = StringVar(top2)  # Variable for event type
    
    # Generate a unique event ID
    while True:
        new_event_id = random_id()  # Generate a new random event ID
        if new_event_id not in event_ids:  # Check if the ID is unique
            event_id.set(new_event_id)  # Set the unique event ID
            break  # Exit the loop once a unique ID is found
        continue  # Repeat if the ID is not unique
    
    # Function to create the event when the submit button is clicked
    def CreateNow():
        # Validate that the event name is at least 5 characters long
        if len(event_name.get()) < 5:
            show_message('Error', 'Enter valid details')  # Show error message if invalid
            return
        # Call the function to create a new event with the provided details
        event_status = CreateNewEvent(event_name.get(), event_id.get(), event_date.get(), event_time.get(), event_duration.get(), event_type.get())  # Include event_type
        if event_status == 'Success':
            show_message('Success', 'Event created successfully')  # Show success message if event creation is successful
            return
        else:
            show_message('Error', event_status)  # Show error message if event creation fails
    
    # Create and place labels and input fields in the window
    Label(top2, text='Enter details', font=('Times New Roman', 20, 'bold'), bg='#006BFF', fg='white', relief='raised').grid(row=0, column=0, padx=10, pady=10, columnspan=2)  # Header label
    
    Label(top2, text='Event Name', font=('Times New Roman', 15, 'bold'), bg='#006BFF', fg='white', relief='raised').grid(row=1, column=0, padx=10, pady=10, sticky='w')  # Label for event name
    Entry(top2, textvariable=event_name).grid(row=1, column=1)  # Input field for event name
    
    Label(top2, text='Event Id', font=('Times New Roman', 15, 'bold'), bg='#006BFF', fg='white', relief='raised').grid(row=2, column=0, padx=10, pady=10, sticky='w')  # Label for event ID
    Entry(top2, textvariable=event_id, state='disabled').grid(row=2, column=1)  # Display event ID (not editable)
    
    Label(top2, text='Event Date', font=('Times New Roman', 15, 'bold'), bg='#006BFF', fg='white', relief='raised').grid(row=3, column=0, padx=10, sticky='w', pady=10)  # Label for event date
    DateEntry(top2, selectmode='day', year=2023, month=1, day=25, textvariable=event_date).grid(row=3, column=1)  # Date picker for event date
    
    Label(top2, text='Event Time', font=('Times New Roman', 15, 'bold'), bg='#006BFF', fg='white', relief='raised').grid(row=4, column=0, padx=10, pady=10, sticky='w')  # Label for event time
    Entry(top2, textvariable=event_time).grid(row=4, column=1)  # Input field for event time
    
    Label(top2, text='Event Duration', font=('Times New Roman', 15, 'bold'), bg='#006BFF', fg='white', relief='raised').grid(row=5, column=0, padx=10, pady=10, sticky='w')  # Label for event duration
    Entry(top2, textvariable=event_duration).grid(row=5, column=1)  # Input field for event duration
    
    Label(top2, text='Event Type', font=('Times New Roman', 15, 'bold'), bg='#006BFF', fg='white', relief='raised').grid(row=6, column=0, padx=10, pady=10, sticky='w')  # Label for event type
    Entry(top2, textvariable=event_type).grid(row=6, column=1)  # Input field for event type
    
    # Create and place the submit button to create the event
    Button(top2, text='Submit', bg='green', fg='white', font=('Arial', 17), width=9, command=lambda: CreateNow()).grid(row=8, column=0, pady=(10, 20), columnspan=2)  # Button to submit event details
    
    top2.mainloop()  # Start the GUI event loop to display the window and wait for user interaction