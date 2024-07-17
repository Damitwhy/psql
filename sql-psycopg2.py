import psycopg2


# Connect to the database
connection = psycopg2.connect(database="chinook")

# Open a cursor to perform database operations
cursor = connection.cursor()

# Query 1 - select all the records from the "Artist" table
#cursor.execute('SELECT * FROM "Artist"')

# Query 2 - select only the "Name" column from the "Artist" table
#cursor.execute('SELECT "Name" FROM "Artist"')

# Query 3 - select only "Queen" from the "Artist" table
#cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ['Queen'])

# Query 4 - select only by "ArtistId" from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [22])

# Query 5 - select only the albums with "ArtistId" 22 from the "Album" table
#cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

# Query 6 - select all the tracks where the composer is "Queen" from the "Track" table
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ['Queen'])

# fetch all the data from the table
results = cursor.fetchall()

# fetch the result (single)
#results = cursor.fetchone()

connection.close()

# print the result
for result in results:
    print(result)