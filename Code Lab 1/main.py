import re
import csv

with open('/fb_sub.csv') as fb_file:
    rd_csv = csv.reader(fb_file, delimiter=',')
    for i in rd_csv:
        txt = re.findall("[A-Z]+ INC", str(i))

with open('company.txt','w') as cmpy:
    cmpy.write(str(txt))