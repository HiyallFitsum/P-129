import csv

data = []

with open("", 'r')as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        data.append(row)

headers = data[0]
star_data = data[1:]

for data_point in star_data:
    data_point[2] = data_point[2].lower()

star_data.sort(key=lambda star_data: star_data[2])
with open("", "a+")as f:
    csv_write = csv.writer(f)
    csv_write.writerow(headers)
    csv_write.writerows(star_data)