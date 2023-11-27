# csv comma separated file
# library for working with csv file
# pandas
# openpyxl
# google sheets python api

import csv
# open file
data = open('example.csv', encoding='utf-8')
# csv reader
csv_reader = csv.reader(data)
# reformat csv file into python object list of lists
data_lines = list(csv_reader)
print(data_lines)

for line in data_lines:
    print(line)

#get the row
print(data_lines[3])

#get the column
all_email = []
for line in data_lines:
    all_email.append(line[3])

print(all_email)
data.close()

#write
file_to_output = open('save_to_file.csv', mode='w', newline='')
csv_writer = csv.writer(file_to_output, delimiter=',')
csv_writer.writerows([all_email[1:]])
file_to_output.close()


# working with PDF
# PyPDF2

import PyPDF2
f = open
