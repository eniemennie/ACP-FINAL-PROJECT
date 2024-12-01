import sqlite3  # Import the sqlite3 library to interact with SQLite databases

def EventDetails():
    # Connect to the event database
    conn = sqlite3.connect('event_database.db')
    cursor = conn.cursor()

    # Create the event_details table if it does not exist
    cursor.execute("CREATE TABLE IF NOT EXISTS event_details (event_name TEXT, event_id TEXT PRIMARY KEY, event_date TEXT, event_time TEXT, event_duration Text, event_type TEXT)")

    # Retrieve all records from the event_details table
    cursor.execute('SELECT * FROM event_details')
    event_details = cursor.fetchall()  # Fetch all results

    # Initialize lists to store event details
    event_names = []
    event_ids = []
    event_dates = []
    event_times = []
    event_durations = []
    event_types = []
    conn.close()  # Close the database connection
    
    # Populate the lists with data from the fetched records
    for i in event_details:
        event_names.append(i[0])  # Event name
        event_ids.append(i[1])     # Event ID
        event_dates.append(i[2])   # Event date
        event_times.append(i[3])   # Event time
        event_durations.append(i[4])  # Event duration
        
    return event_names, event_ids, event_dates, event_times, event_durations, event_details, event_types  # Return event details

def TicketDetails():
    # Connect to the event database
    conn = sqlite3.connect('event_database.db')
    cursor = conn.cursor()

    # Create the ticket_details table if it does not exist
    cursor.execute("CREATE TABLE IF NOT EXISTS ticket_details (customer_name TEXT, ticket_id TEXT PRIMARY KEY, event_name TEXT, event_id TEXT, event_date TEXT, event_time TEXT, duration Text, event_type TEXT)")

    # Retrieve all records from the ticket_details table
    cursor.execute('SELECT * FROM ticket_details')
    ticket_details = cursor.fetchall()  # Fetch all results
    
    # Initialize lists to store ticket details
    customer_names = []
    ticket_ids = []
    event_names = []
    event_ids = []
    event_dates = []
    event_times = []
    event_durations = []
        
    conn.close()  # Close the database connection
    
    # Populate the lists with data from the fetched records
    for i in ticket_details:
        customer_names.append(i[0])  # Customer name
        ticket_ids.append(i[1])       # Ticket ID
        event_names.append(i[2])      # Event name
        event_ids.append(i[3])        # Event ID
        event_dates.append(i[4])      # Event date
        event_times.append(i[5])      # Event time
        event_durations.append(i[6])   # Event duration
        
    return customer_names, ticket_ids, event_names, event_ids, event_dates, event_times, event_durations, ticket_details  # Return ticket details

def BookTicket(customer_name, ticket_id, event_name):
    # Retrieve event details to find the corresponding event information
    event_names = EventDetails()[0]
    event_ids = EventDetails()[1]
    event_dates = EventDetails()[2]
    event_times = EventDetails()[3]
    event_durations = EventDetails()[4]
    
    # Find the index of the event name to get other details
    event_index = event_names.index(event_name)
    event_id = event_ids[event_index]
    event_date = event_dates[event_index]
    event_time = event_times[event_index]
    event_duration = event_durations[event_index]
    
    try:
        # Connect to the event database
        conn = sqlite3.connect("event_database.db")
        cursor = conn.cursor()
        # Insert a new ticket into the ticket_details table
        cursor.execute("INSERT INTO ticket_details (customer_name, ticket_id, event_name, event_id, event_date, event_time, duration) VALUES (?, ?, ?, ?, ?, ?, ?)", (customer_name, ticket_id, event_name, event_id, event_date, event_time, event_duration))
        conn.commit()  # Commit the transaction
        conn.close()  # Close the database connection
        return 'Success'  # Return success message
    except sqlite3.Error as e:
        return e  # Return any error that occurs
    finally:
        conn.close()  # Ensure the connection is closed

def CreateNewEvent(event_name, event_id, event_date, event_time, event_duration, event_type):
    try:
        # Connect to the event database
        conn = sqlite3.connect("event_database.db")
        cursor = conn.cursor()
        # Insert a new event into the event_details table
        cursor.execute("INSERT INTO event_details (event_name, event_id, event_date, event_time, event_duration, event_type) VALUES (?, ?, ?, ?, ?, ?)", (event_name, event_id, event_date, event_time, event_duration, event_type))
        conn.commit()  # Commit the transaction
        conn.close()  # Close the database connection
        return 'Success'  # Return success message
    except sqlite3.Error as e:
        return e  # Return any error that occurs
    finally:
        conn.close()  # Ensure the connection is closed

def DeleteTicket(ticket_id):
    try:
        # Connect to the event database
        conn = sqlite3.connect("event_database.db")
        cursor = conn.cursor()
        # Delete the ticket from the ticket_details table based on ticket_id
        cursor.execute("DELETE FROM ticket_details WHERE ticket_id = ?", (ticket_id,))
        conn.commit()  # Commit the transaction
        conn.close()  # Close the database connection
        return 'Success'  # Return success message
    except sqlite3.Error as e:
        return e  # Return any error that occurs
    finally:
        conn.close()  # Ensure the connection is closed