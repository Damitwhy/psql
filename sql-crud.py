from sqlalchemy import (
    create_engine,Column,Integer,String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()


# create a class-based model for the "Programmer" table
class Programmer(base):
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)

# instead of connecting to the database directly, we will use a session
# create a new instance of sessionmaker, and point it to our db engine
Session = sessionmaker(db)
#open a session
session = Session()

# create the database using declarative_base subclass
base.metadata.create_all(db)

# create records on our Programmer table
# ada_lovelace = Programmer(    
#     first_name="Ada",
#     last_name="Lovelace",
#     gender="F",
#     nationality="British",
#     famous_for="First Programmer"
# )

# alan_turing = Programmer(
#     first_name="Alan",
#     last_name="Turing",
#     gender="M",
#     nationality="British",
#     famous_for="Modern Computing"
# )

# grace_hopper = Programmer(
#     first_name="Grace",
#     last_name="Hopper",
#     gender="F",
#     nationality="American",
#     famous_for="COBOL Language"
# )

# margaret_hamilton = Programmer(
#     first_name="Margaret",
#     last_name="Hamilton",
#     gender="F",
#     nationality="American", 
#     famous_for="Apollo 11"
# )



# add each instance of our programmers to our session
#session.add(ada_lovelace)
# session.add(grace_hopper)
# session.add(margaret_hamilton)
# session.add(alan_turing)


# commit the session records to the database
# session.commit()

# update a record
# programmer = session.query(Programmer).filter_by(id=1).first()
# programmer.famous_for = "Last Computer Programmer"
# session.commit()

#delete a record
# fname = input("Enter the first name of the programmer to delete: ")
# lname = input("Enter the last name of the programmer to delete: ")  
# programmer = session.query(Programmer).filter_by(first_name=fname, last_name=lname).first()
# # defensive programming
# if programmer is not None:
#     print("Programmer found: ", programmer.first_name, programmer.last_name)
#     confirmation = input("Are you sure you want to delete this record? (y/n): ")
#     if confirmation.lower() == "y":
#         session.delete(programmer)
#         session.commit()
#         print("Programmer record has been deleted")
#     else:
#         print("Programmer record was not deleted")
# else:
#     print("Programmer not found")

#Delete multiple records

programmers = session.query(Programmer)
for programmer in programmers:
    session.delete(programmer)
    session.commit()
    

#update multiple records
# people = session.query(Programmer)
# for person in people:
#     if person.gender == "F":
#         person.gender = "Female"
#     elif person.gender == "M":
#         person.gender = "Male"
#     else:
#         print("Gender not defined")

#     session.commit()


# query the database to find programmers
programmer = session.query(Programmer)
for programmer in programmer:
    print(
        programmer.id, 
        programmer.first_name +" "+ programmer.last_name,
        programmer.gender,
        programmer.nationality,
        programmer.famous_for, 
        sep=" | "
        )
