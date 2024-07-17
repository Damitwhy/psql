from sqlalchemy import(
    create_engine, Table, Column, Float, ForeignKey, Integer, MetaData, String
)

# executing the instrucitions from our local host "chinook" database
db = create_engine("postgresql:///chinook")
# connecting to the database

meta = MetaData(db)

#create vaariable for artist table


# make connection to the database
with db.connect() as connection:
  