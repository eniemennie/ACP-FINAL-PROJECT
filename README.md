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
# DataBase.PY
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

IV. Instructions for running the program
