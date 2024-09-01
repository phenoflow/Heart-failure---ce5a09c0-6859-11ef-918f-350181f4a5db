# phekb, 2024.

import sys, csv, re

codes = [{"code":"428.21","system":"icduncat"},{"code":"428.23","system":"icduncat"},{"code":"428.31","system":"icduncat"},{"code":"428.33","system":"icduncat"},{"code":"I50.21","system":"icduncat"},{"code":"I50.23","system":"icduncat"},{"code":"I50.31","system":"icduncat"},{"code":"I50.33","system":"icduncat"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('heart-failure-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["acute-heart-failure---icduncat-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["acute-heart-failure---icduncat-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["acute-heart-failure---icduncat-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
