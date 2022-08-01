import psycopg2
import os
import csv
from dotenv import load_dotenv

DATA_FOLDER = "../1 Download Files"

# Edit the .env file and add your database credentials
load_dotenv()

connection = psycopg2.connect(
    database = os.getenv("POSTGRES_DB"),
    user = os.getenv("POSTGRES_USR"),
    password = os.getenv("POSTGRES_PWD"),
    host = "localhost",
    port = 5432,
    options = "-c search_path=happiness"
)

cursor = connection.cursor()

# remove all data from the database (using the DELETE command)
cursor.execute("DELETE FROM country;")
connection.commit()

# reads the countries of the world.csv file
# populate the database with new data (using the INSERT command)
with open(DATA_FOLDER + "/countries of the world.csv", 'r') as f:
    csvreader = csv.reader(f)
    next(csvreader)
    i = 0
    for row in csvreader:
        rcountry = row[0].strip().replace("'", "")
        rpop = int(row[2])
        rarea = int(row[3])
        rinfant_mortality = 0 if row[7] == '' else float(row[7].replace(",", "."))
        rgdp_per_capita = 0 if row[8] == '' else float(row[8].replace(",", "."))
        rliteracy = 0 if row[9] == '' else float(row[9].replace(",", "."))
        cursor.execute("INSERT INTO country (name, population, area, infant_mortality, gdp, literacy) VALUES (%s, %s, %s, %s, %s, %s);", 
                        (rcountry, rpop, rarea, rinfant_mortality, rgdp_per_capita, rliteracy))
        i += 1

connection.commit()

print(f"{i} countries loaded to the database successfully!")

cursor.close()
connection.close()