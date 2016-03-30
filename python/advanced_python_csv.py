PLACE YOUR CODE HERE
import csv

f = open("/home/yashas/Documents/faculty.csv", "r")

faculty = list(csv.reader(f))
data = faculty[1:]

emails = []
for row in data:
    emails.append(row[3].strip())
    
with open("dsp/python/emails.csv", "w") as f:
    writer = csv.writer(f, lineterminator = '\n')
    for email in emails:
        writer.writerow([email])
