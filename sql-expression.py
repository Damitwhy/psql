from sqlalchemy import(
    create_engine, Table, Column, Float, ForeignKey, Integer, MetaData, String
)

# executing the instrucitions from our local host "chinook" database
db = create_engine("postgresql:///chinook")
# connecting to the database

meta = MetaData(db)

#create vaariable for artist table
artist_table = Table(
   "Artist", meta,
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String)
)

#create variable for album table
album_table = Table(
    "Album", meta,
    Column("AlbumId", Integer, primary_key=True),
    Column("Title", String),
    Column("ArtistId", Integer, ForeignKey("Artist.ArtistId"))
)

#create variable for track table
track_table = Table(
    "Track", meta,
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey("Album.AlbumId")),
    Column("MediaTypeId", Integer, primary_key=False),
    Column("GenreId", Integer, primary_key=False),
    Column("Composer", String),
    Column("Milliseconds", Integer),
    Column("Bytes", Integer),
    Column("UnitPrice", Float)
)

# make connection to the database
with db.connect() as connection:
    #query 1 - select all records from the "artist" table
    #select_query = artist_table.select()
    #query 2 - select only the "name" column from the "artist" table
    #select_query = artist_table.select().with_only_columns([artist_table.c.Name])
    #query 3 - select only 'queen' from the "artist" table
    #select_query = artist_table.select().where(artist_table.c.Name == "Queen")
    #query 4 - select only by "artistid" from the "artist" table
    #select_query = artist_table.select().where(artist_table.c.ArtistId == 51)
    #query 5 - select only the "name" column from the "artist" table
    #
    #query 6
    #select_query = track_table.select().where(track_table.c.Name == "My Generation")
    select_query = track_table.select().where(track_table.c.Composer == "Queen")

    #execute the query
    results = connection.execute(select_query)
    #print the results
    for result in results:
        print(result)
    #query 2 - select only the "name" column from the "artist" table


  