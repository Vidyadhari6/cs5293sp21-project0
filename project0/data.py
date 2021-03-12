import tempfile
import urllib.request
from PyPDF2 import PdfFileReader
import pandas as pd
import sqlite3

pd.set_option("display.max_rows", None, "display.max_columns", None)

def divide_chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]


def fetchIncidentsData(url):
    headers = {}
    headers[
        'User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    data = urllib.request.urlopen(urllib.request.Request(url, headers=headers))
    return data


def extractIncidentsData(data):
    fp = tempfile.TemporaryFile()

    # Write the pdf data to a temp file
    fp.write(data.read())

    # Set the curser of the file back to the begining
    fp.seek(0)

    # Read the PDF
    pdfReader = PdfFileReader(fp)

    # Using pdfreader to extract the text
    final_df = pd.DataFrame([])
    for i in range(pdfReader.getNumPages()):
        page = pdfReader.getPage(i).extractText().replace(' \n', ' ')
        incidents = list(divide_chunks(page.splitlines(), 5))
        incidents_df = pd.DataFrame(incidents)
        final_df = final_df.append(incidents_df, ignore_index=True)
    header = ['incident_time', 'incident_number', 'incident_location', 'nature', 'incident_ori']
    final_df = final_df[1:]
    final_df.columns = header
    final_df = final_df[final_df.incident_ori.notnull()]
    return final_df


def createdb(db):
    sql = sqlite3.connect(db)
    cur = sql.cursor()
    drop_query = "drop table if exists incidents"
    cur.execute(drop_query)
    query = """CREATE TABLE IF NOT EXISTS incidents (
    incident_time TEXT,
    incident_number TEXT,
    incident_location TEXT,
    nature TEXT,
    incident_ori TEXT)"""
    cur.execute(query)

    return 'normanpd.db'


def populatedb(db, incidents_df):
    sql_conn = sqlite3.connect(db)
    c = sql_conn.cursor()
    try:
        incidents_df.to_sql('incidents', sql_conn, if_exists='replace', index = False)
        return True
    except Exception:
        return False



def getStatus(db):
    sql_conn = sqlite3.connect(db)
    c = sql_conn.cursor()
    s = c.execute("select nature, count(*) from incidents group by 1 order by 1 asc")
    for r in s.fetchall():
        print("".join(str(r[0]).split()), '|', r[1])
    sql_conn.close()
