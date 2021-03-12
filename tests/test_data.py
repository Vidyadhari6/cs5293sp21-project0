import sqlite3
from project0 import data
import pandas as pd

incidents_url = " https://www.normanok.gov/sites/default/files/documents/2021-03/2021-03-02_daily_incident_summary.pdf"
db = "normanpd.db"

def test_fetchincidents():
    assert data.fetchIncidentsData(incidents_url).read() is not None

def test_extractincidents():
    assert len(data.extractIncidentsData(data.fetchIncidentsData(incidents_url)).index) == 376

def test_createdb():
    dbname = data.createdb(db)
    assert dbname==db
def test_populatedb():
    df = pd.DataFrame({'incident_time': ['3/1/2021 0:02'],
                       'incident_number': ['001'],
                       'incident_location': ['USA'],
                       'nature': ['test'],
                       'incident_ori': ['test']})
    result = data.populatedb(db, df)
    assert result is True