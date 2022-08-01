import sys
import psycopg2
import os
import csv
from dotenv import load_dotenv

DATA_FOLDER = "../1 Download Files"

if len(sys.argv) < 3:
    print("Arguments 'year' and 'file' were not specified.")
    sys.exit()

if not sys.argv[1].isnumeric():
    print("Please insert a valid year.")
    sys.exit()

if not os.path.isfile(DATA_FOLDER + f'./{sys.argv[2]}'):
    print("Could not find the specified file.")
    sys.exit()

# Edit the .env file and add your database credentials
load_dotenv()

#conect to de database
connection = psycopg2.connect(
    database = os.getenv("POSTGRES_DB"),
    user = os.getenv("POSTGRES_USR"),
    password = os.getenv("POSTGRES_PWD"),
    host = "localhost",
    port = 5432,
    options = "-c search_path=happiness"
)


cursor = connection.cursor()

#definir ano
ano = int(sys.argv[1])

#definir arquivo
arquivo = DATA_FOLDER + f'./{sys.argv[2]}'

# remove all data from the database (using the DELETE command)
cursor.execute("DELETE FROM score_year WHERE year = %s;", (ano,))
connection.commit()

countries_to_exclude = ['Bosnia and Herzegovina', 'Central African Republic', 'Congo (Brazzaville)', 'Congo (Kinshasa)', 'Gambia', 'Hong Kong S.A.R., China', 'Ivory Coast', 'Kosovo', 'Montenegro', 'Myanmar', 'North Cyprus', 'North Macedonia', 'Northern Cyprus', 'Palestinian Territories', 'Somaliland Region', 'Somaliland region', 'South Korea', 'South Sudan', 'Taiwan Province of China', 'Trinidad and Tobago']
# reads the countries of the world.csv file
# populate the database with new data (using the INSERT command)

with open(arquivo, 'r') as f:
    csvreader = csv.reader(f)
    next(csvreader)
    i = 0
    for row in csvreader:
        if ano in [2015, 2016]:
            rcountry = row[0].strip()
            if rcountry in countries_to_exclude:
                pass
            else:
                rscore = 0 if row[3] == '' else float(row[3].replace(",", "."))
                cursor.execute("INSERT INTO score_year (country, score, year) VALUES (%s, %s, %s)", (rcountry, rscore, ano))
        elif ano == 2017:
            rcountry = row[0].strip()
            if rcountry in countries_to_exclude:
                pass
            else:
                rscore = 0 if row[2] == '' else float(row[2].replace(",", "."))
                cursor.execute("INSERT INTO score_year (country, score, year) VALUES (%s, %s, %s)", (rcountry, rscore, ano))
        else:
            rcountry = row[1].strip()
            if rcountry in countries_to_exclude:
                pass
            else:
                rscore = 0 if row[2] == '' else float(row[2].replace(",", "."))
                cursor.execute("INSERT INTO score_year (country, score, year) VALUES (%s, %s, %s)", (rcountry, rscore, ano))  
        i += 1

connection.commit()

print(f"[INFO] data loaded: {i} countries for the year {ano} loaded to the database successfully!")

cursor.close()
connection.close()
