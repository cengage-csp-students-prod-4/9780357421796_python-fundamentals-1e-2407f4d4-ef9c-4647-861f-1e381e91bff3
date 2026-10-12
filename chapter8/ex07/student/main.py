import csv

with open("employees.csv", "r") as infile, open("wages.csv", "w", newline="") as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    next(reader)                        # skip the input header row
    writer.writerow(["name", "wages"])  # output header — match Figure 8.6

    for row in reader:
        name = row[0]
        hours = int(row[1])             # CSV values are strings, so convert
        writer.writerow([name, hours * 15])