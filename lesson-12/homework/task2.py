# Task 2: Scraping fake jobs and storing in SQLite
import requests
from bs4 import BeautifulSoup
import sqlite3
import csv

url = "https://realpython.github.io/fake-jobs"
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")

conn = sqlite3.connect("jobs.db")
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS jobs (
    title TEXT,
    company TEXT,
    location TEXT,
    description TEXT,
    link TEXT,
    UNIQUE(title, company, location)
)
""")

job_elements = soup.find_all("div", class_="card-content")

for job in job_elements:
    title = job.find("h2", class_="title").text.strip()
    company = job.find("h3", class_="company").text.strip()
    location = job.find("p", class_="location").text.strip()
    description = job.find("div", class_="content").text.strip()
    link = job.find("a", string="Apply")["href"]

    cur.execute("SELECT description, link FROM jobs WHERE title=? AND company=? AND location=?", (title, company, location))
    existing = cur.fetchone()

    if existing:
        if existing[0] != description or existing[1] != link:
            cur.execute("UPDATE jobs SET description=?, link=? WHERE title=? AND company=? AND location=?", (description, link, title, company, location))
    else:
        cur.execute("INSERT OR IGNORE INTO jobs (title, company, location, description, link) VALUES (?, ?, ?, ?, ?)", (title, company, location, description, link))

conn.commit()

def filter_and_export(filter_by=None, value=None, filename="filtered_jobs.csv"):
    query = "SELECT * FROM jobs"
    params = ()
    if filter_by and value:
        query += f" WHERE {filter_by} = ?"
        params = (value,)
    cur.execute(query, params)
    rows = cur.fetchall()

    with open(filename, "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Title", "Company", "Location", "Description", "Link"])
        writer.writerows(rows)

filter_and_export("location", "Remote", "remote_jobs.csv")
conn.close()
