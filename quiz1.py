# QUESTION 1

# Write a query that will display the results below (Note: some columns might be renamed 
# but use the column names above). It should only show 2020 data and order by driver
# points.

import pyodbc
from prettytable import PrettyTable
# Connect
connectDB = (
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=DESKTOP-UGJPDP0;"  
    "Database=RACE_CARS_DB;"   
    "Trusted_Connection=yes;"  #yes windows authentication
)

try:
    #testing connection
    connection = pyodbc.connect(connectDB)
    print("Connection successful!")
   
    CREATE_TABLE = """
    CREATE TABLE RACE (
        RACE_ID INT PRIMARY KEY,
        race_year VARCHAR(10),
        race_name VARCHAR(30),
        race_date VARCHAR(30),
        race_time VARCHAR(30),
        circuit_location VARCHAR(30),
        driver_name VARCHAR(20),
        driver_number VARCHAR(10),
        driver_nationality VARCHAR(15),
        team VARCHAR(30),
        grid VARCHAR(10),
        fastest_lap VARCHAR(20),
        points VARCHAR(10),
        created_date VARCHAR(10)
    );
    """
    #Create table
    connection.execute(CREATE_TABLE)
    print("Table created")

    INSERT_VALUES=""" INSERT INTO RACE(RACE_ID, race_year, race_name, race_date, race_time, circuit_location, driver_name, driver_number, driver_nationality, team, grid, fastest_lap, points, created_date)
 VALUES (1, '2020', 'Portuguese Grand Prix', '2020-10-25', '1:29:56.828', 'Portimão', 'Lewis Hamilton', '44', 'British', 'AlphaTauri', '1', '63', '26', '2020-10-25'),
        (2, '2020', 'Russian Grand Prix', '2020-09-27', '1:34:00.364', 'Sochi', 'Valtteri Bottas', '77', 'Finnish', 'Mercedes', '3', '51', '26', '2020-09-27'),   
        (3, '2020', 'Emilia Romagna Grand Prix', '2020-11-01', '1:28:32.430', 'Imola', 'Lewis Hamilton', '44', 'British', 'Mercedes', '2', '63', '16', '2020-11-01'),
        (4, '2020', 'Hungarian Grand Prix', '2020-07-19', '1:36:12.473', 'Budapest', 'Lewis Hamilton', '44', 'British', 'Mercedes', '1', '70', '36', '2020-07-19'),
        (5, '2020', 'Tuscan Grand Prix', '2020-09-13', '2:19:35.060', 'Mugello', 'Lewis Hamilton', '44', 'British', 'RedBull', '1', '58', '26', '2020-09-13'),
        (6, '2020', 'Sakhir Grand Prix', '2020-12-06', '1:31:15.114', 'Sakhir', 'Sergio Pérez', '11', 'Mexican', 'Racing Point', '5', '69', '15', '2020-12-06'),
        (7, '2020', 'Eifel Grand Prix', '2020-10-11', '1:35:49.641', 'Nürburg', 'Lewis Hamilton', '44', 'British', 'Mercedes', '2', '58', '18', '2020-10-11'),
        (8, '2015', 'Styrian Grand Prix', '2020-07-12', '1:22:50.683', 'Spielburg', 'Lewis Hamilton', '44', 'British', 'Mercedes', '1', '68', '25', '2020-07-12'),
        (9, '2020', 'Bahrain Grand Prix', '2020-11-29', '2:59:47.515', 'Sakhir', 'Lewis Hamilton', '44', 'British', 'Mercedes', '1', '38', '25', '2020-11-29'),
        (10, '2017', 'Portuguese Grand Prix', '2020-10-25', '1:29:56.828', 'Portimão', 'Lewis Hamilton', '44', 'British', 'Mercedes', '1', '63', '26', '2020-10-25'),
        (11, '2020', 'Russian Grand Prix', '2020-09-27', '1:34:00.364', 'Sochi', 'Valtteri Bottas', '77', 'Finnish', 'Mercedes', '3', '51', '26', '2020-09-27'),
        (12, '2016', 'Emilia Romagna Grand Prix', '2020-11-01', '1:28:32.430', 'Imola', 'Lewis Hamilton', '44', 'British', 'Mercedes', '2', '63', '26', '2020-11-01'),
        (13, '2019', 'Hungarian Grand Prix', '2020-07-19', '1:36:12.473', 'Budapest', 'Lewis Hamilton', '44', 'British', 'Mercedes', '1', '70', '26', '2020-07-19'),
        (14, '2020', 'Tuscan Grand Prix', '2020-09-13', '2:19:35.060', 'Mugello', 'Lewis Hamilton', '44', 'British', 'Mercedes', '1', '58', '46', '2020-09-13'),
        (15, '2019', 'Spanish Grand Prix', '2020-08-16', '1:31:45.279', 'Montmeló', 'Lewis Hamilton', '44', 'British', 'Mercedes', '1', '63', '35', '2020-08-16');

"""
    #insert
    connection.execute(INSERT_VALUES)

    #DROP_TABLE="""DROP TABLE RACE"""
    # connection.execute(DROP_TABLE)
    # print('table dropped')

    #querying db
    QUERY=connection.cursor()
    DISPLAY_ALL="""SELECT *FROM RACE WHERE race_year='2020'
                    ORDER BY points DESC"""
    
    TO_DISPLAY = QUERY.execute(DISPLAY_ALL).fetchall()

    displayTable = PrettyTable()
    displayTable.field_names = ["RACE_ID", "race_year", "race_name", "race_date", "race_time", "circuit_location","driver_name", "driver_number", "driver_nationality", "team", "grid", "fastest_lap", "points", "created_date"]                  
    
    for rows in TO_DISPLAY:
        displayTable.add_row(rows)        
    print(displayTable)

except pyodbc.Error as error:
    print("Database error:", error)

