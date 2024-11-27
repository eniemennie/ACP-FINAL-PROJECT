# “무대마스터 (StageMaster): Concert Event Management System”
Advanced Computer Programming - First Semester Final Project
![Untitled design (3)](https://github.com/user-attachments/assets/75419f6e-5d6b-45fe-b7bf-4742bdbdc6c8)

# I. A brief project overview
무대마스터 (StageMaster): Concert Event Management System
- this system is designed to facilitate the management of concert events and ticket bookings, providing a user-friendly interface for both event organizers and attendees. It integrates various functionalities to ensure a smooth operation, from creating events to booking tickets and managing them efficiently.

# II. Explanation of how Python concepts, libraries, etc. were applied
# Main.py
- The application's main entry point is the concert event management system, which features a greeting window, buttons for various functionalities like Book Ticket, Create Event, View Tickets, Cancel Ticket, and Quit App, each linked to corresponding functions that open new windows for each function.
# Book.py
- This module handles the ticket booking process.
- It fetches available ticket IDs and event names/types from the database using TicketDetails() and EventDetails().
- The user can enter their name, and the system generates a new ticket ID using the random_id() function.
# CreateEvent.py
- This module allows users to create new events.
- It generates a unique event ID using the random_id() function and collects details such as event name, date, time, duration, and type.
# ViewTickets.py
- This module would likely handle the functionality for viewing booked tickets. It would fetch ticket details from the database and display them in a user-friendly format.
# ViewEvent.py
- This module would likely handle the functionality for viewing available events. It would retrieve event details from the database and display them to the user.
# CancelTicket.py
- This module would likely allow users to cancel previously booked tickets. It would involve fetching the user's booked tickets and providing an option to cancel them, updating the database accordingly.
# DataBase.py
- This module contains functions for interacting with the database. It likely includes:
- TicketDetails(): Fetches current ticket IDs and details.
- EventDetails(): Fetches available event names, types, and other relevant details.
- BookTicket(customer_name, ticket_id, event_name): Books a ticket for the customer.
- CreateNewEvent(event_name, event_id, event_date, event_time, event_duration, event_type): Creates a new event in the database.
# GenerateNewCode.py
- This module is responsible for generating unique identifiers for tickets and events. The random_id() function is likely implemented here to ensure that each ID is unique and not already in use.
# Message.py
- This module contains the show_message function, which is used to display message boxes for success or error notifications throughout the application. This enhances user experience by providing immediate feedback on their actions.

# III. Details of the chosen SDG and its integration into the project
# SDG 8: Decent Work and Economic Growth
- Concert Event Management System can create jobs in event planning, production, security, and hospitality sectors.
- Promotes fair labor practices and ethical working conditions.

# SDG 9: Industry, Innovation, and Infrastructure
- Can enhance efficiency, reduce waste, and enhance attendees' experience.
- Contributes to the development of event venues and supporting infrastructure.


# IV. Instructions for running the program
# Main.py
-  The main window of the application. Here, users can access various functionalities through dedicated buttons like "Book Ticket," "Create New Event," "View Events," "View Tickets," and "Cancel Ticket."
# Book.py
- The users can enter their name, which needs to be at least 5 characters long. A unique ticket ID is automatically generated. They can then select an event from the dropdown menu and click "Confirm" to finalize the booking.
# CreateNewEvent.py
-  In this module, they can enter details like event name (again, with a minimum length requirement) to create new events, select the date using the calendar widget, specify time, duration, and event type. Clicking "Submit" adds the event to the system.
# ViewTickets.py and ViewEvents.py
-  This is where we can view all existing events in a table format. This displays details like event name, ID, date, time, duration, and type.
Similarly, users can view their booked tickets for a specific event by selecting it from the dropdown menu. Here, it shows details like customer name, ticket ID, event information (name, date, time, and duration).
# CancelTicket.py
- Users can manage their bookings by canceling tickets. This window shows a list of their tickets with details like customer name, ticket ID, event name, and date. Clicking the "Delete" button next to a specific ticket removes it from the system. Cancellation successes and failures are indicated through messages.
# Database.py
connecting to functions)
This system utilizes a SQLite database to store all event and ticket information. Functions are defined to manage this data:
- EventDetails: retrieves event information from the database.
- TicketDetails: retrieves booked tickets.
- BookTicket: adds a new booking to the database.
- CreateNewEvent: creates a new event record in the database.
- DeleteTicket: removes a ticket from the database.
# GenerateNewCode.py
- The system uses Python's random module to generate unique 8-digit ticket IDs, ensuring proper identification of each booking.
# Message.py
- The system relies on Tkinter's message dialog function to display informative error messages when necessary. This helps users understand and address any issues with data entry or actions within the application.
