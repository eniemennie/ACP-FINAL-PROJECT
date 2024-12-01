from tkinter import *  # Import all classes and functions from tkinter for GUI
from DataBase import TicketDetails  # Import function to get ticket details from the database
from DataBase import DeleteTicket  # Import function to delete a ticket from the database
from Message import show_message  # Import function to display messages to the user

def CancelTicket():
    # Create the main window for canceling tickets
    top3 = Tk()
    top3.geometry('1100x600')  # Set the window size
    top3.title('Cancel Tickets')  # Set the window title
    top3.resizable(False, False)  # Disable window resizing
    
    # Set the background color of the main window
    top3.configure(bg='#08C2FF')
    
    # Create a frame to contain the canvas and scrollbar
    frame = Frame(top3, bg='#08C2FF')
    frame.pack(fill=BOTH, expand=True)  # Allow the frame to expand and fill the window

    # Create a canvas for scrolling content
    canvas = Canvas(frame, bg='#08C2FF')
    canvas.pack(side=LEFT, fill=BOTH, expand=True)  # Fill the frame with the canvas

    # Create a vertical scrollbar for the canvas
    scrollbar = Scrollbar(frame, orient=VERTICAL, command=canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)  # Place the scrollbar on the right side

    # Configure the canvas to work with the scrollbar
    canvas.configure(yscrollcommand=scrollbar.set)

    # Create a frame to hold the content of the canvas
    content_frame = Frame(canvas, bg='#08C2FF')

    # Create a window in the canvas to hold the content frame
    canvas.create_window((0, 0), window=content_frame, anchor='nw')

    # Function to update the scroll region of the canvas when the content frame is resized
    def on_frame_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))  # Update the scroll region to encompass the new size

    content_frame.bind("<Configure>", on_frame_configure)  # Bind the resize event to the function

    # Add labels for the headers in the content frame
    Label(content_frame, text='Customer Name', font=('Times New Roman', 15, 'bold'), background='#006BFF', fg='white', relief='raised', width=20).grid(row=0, column=0, pady=10)
    Label(content_frame, text='Ticket ID', font=('Times New Roman', 15, 'bold'), background='#006BFF', fg='white', relief='raised', width=20).grid(row=0, column=1, pady=10)
    Label(content_frame, text='Event Name', font=('Times New Roman', 15, 'bold'), background='#006BFF', fg='white', relief='raised', width=20).grid(row=0, column=2, pady=10)
    Label(content_frame, text='Event Date', font=('Times New Roman', 15, 'bold'), background='#006BFF', fg='white', relief='raised', width=20).grid(row=0, column=3, pady=10)

    # Function to delete a ticket based on the ticket ID
    def delete_rows(ticket_id):
        delete_status = DeleteTicket(ticket_id)  # Call the function to delete the ticket
        if delete_status == 'Success':
            show_message('Success', 'Ticket deleted successfully')  # Show success message
            return
        else:
            show_message('Error', delete_status)  # Show error message if deletion fails
            return

    # Add ticket details to the content frame
    for i in range(len(TicketDetails()[7])):  # Loop through the ticket details
        # Create labels for each ticket detail
        Label(content_frame, text=TicketDetails()[7][i][0], width=20, wraplength=100, bg='#08C2FF').grid(row=i+1, column=0)  # Customer Name
        Label(content_frame, text=TicketDetails()[7][i][1], width=20, wraplength=100, bg='#08C2FF').grid(row=i+1, padx=10, column=1)  # Ticket ID
        Label(content_frame, text=TicketDetails()[7][i][2], width=20, wraplength=100, bg='#08C2FF').grid(row=i+1, padx=10, column=2)  # Event Name
        Label(content_frame, text=TicketDetails()[7][i][4], width=20, wraplength=100, bg='#08C2FF').grid(row=i+1, padx=10, column=3)  # Event Date
        
        # Create a delete button for each ticket that calls the delete_rows function with the corresponding ticket ID
        Button(content_frame, text='Delete', font=('Arial', 10, 'bold'), background='red', fg='white', 
               command=lambda current_id=TicketDetails()[7][i][1]: delete_rows(current_id)).grid(row=i+1, column=4)

    top3.mainloop()  # Start the GUI event loop to display the window and wait for user interaction