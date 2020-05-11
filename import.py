import csv
import os
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

os.environ["DATABASE_URL"] ="postgres://hcltwivjzhqgxy:458fc2856e29de6a0e1690166b7014ab620cd1291c8d6de457c6412569106977@ec2-46-137-113-157.eu-west-1.compute.amazonaws.com:5432/d66c21bt7mpp2r"
DATABASE_URL = os.environ["DATABASE_URL"]
conn = psycopg2.connect(DATABASE_URL, sslmode='require')

# Check for environment variables
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def main():
    f = open("books1.csv")
    reader = csv.reader(f)
    for isbn, title, author, year in reader:
        db.execute("INSERT INTO books (isbn, title, author, year) VALUES (:isbn, :title, :author, :year)",
                    {"isbn": isbn,"title": title,"author": author, "year": year})
    db.commit()

if __name__ == "__main__":
    main()