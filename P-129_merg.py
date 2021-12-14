import csv

data1 = []
data2 = []

with open("", "r")as f:
    csv_writer = csv.writer(f)
    for row in csv_writer:
        data1.append(row)

with open("", "r")as f:
    csv_writer = csv.writer(f)
    for row in csv_writer:
        data2.append(row)

header1 = data1[0]
star_data1 = data1[1:]

header2 = data2[0]
star_data2 = data2[1:]

headers = header1 + header2
star_data = []

for index, data_row in enumerate[star_data]:
    star_data.append(star_data1[index] + star_data2[index])

with open('P-final.csv', 'a+')as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerow(star_data)

