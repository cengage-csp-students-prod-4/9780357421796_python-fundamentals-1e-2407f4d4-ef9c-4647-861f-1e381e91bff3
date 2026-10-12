import csv
import os

base = os.path.dirname(os.path.abspath(__file__))
in_path = os.path.join(base, "employees.csv")
out_path = os.path.join(base, "wages.csv")

with open(in_path, "r") as infile, open(out_path, "w", newline="") as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    next(reader)
    writer.writerow(["name", "wages"])  # match Figure 8.6

    for row in reader:
        writer.writerow([row[0], int(row[1]) * 15])