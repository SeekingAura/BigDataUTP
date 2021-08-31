from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Connect to db
motor=create_engine('mysql+pymysql://admin:Bigdata-2020@localhost:3306/sqlejemplo')

# Definition about sesion
Session = sessionmaker(bind=motor)

# Login to database
session = Session()

# Definition about library base
Base=declarative_base()
