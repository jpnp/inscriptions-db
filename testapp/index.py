
import csv

# id
# region
# city
# location
# reference
# reference_num
# bib_url
# date_from
# date_to
# description
# phi_url
# phi_id
# doc_type
# authority
# activity
# purpose
# context
# denomination
# notes


def index_csv(filename):
    with open(filename, 'r') as infile:
        entries=csv.DictReader(infile)
        print(next(entries))
        for r in entries:
            city=(r["CITY"])
            if city:
                print(city)
        print("Remaining Entries: "+str(len(list(entries))))

