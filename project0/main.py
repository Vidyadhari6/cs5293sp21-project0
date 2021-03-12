import argparse

from data import *


def main(url):
    # Download data
    data = fetchIncidentsData(url)

    # Extract Data
    incidents_df = extractIncidentsData(data)

    # Create Datbase
    db = createdb("normanpd.db")

    # Insert Data
    populatedb(db, incidents_df)

    # Print Status
    getStatus(db)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--incidents", type=str, required=True,
                        help="Incident summary url.")

    args = parser.parse_args()
    if args.incidents:
        main(args.incidents)
