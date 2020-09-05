import csv

with open('C:\\Users\owner\\Desktop\\skywill_2020_1_program\\review_marge_after\\review_all.csv',encoding="utf-8_sig") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)