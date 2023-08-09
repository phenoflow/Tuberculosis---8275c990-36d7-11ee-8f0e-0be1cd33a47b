# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"A10..00","system":"readv2"},{"code":"A100.00","system":"readv2"},{"code":"A10z.00","system":"readv2"},{"code":"A114.00","system":"readv2"},{"code":"A115.00","system":"readv2"},{"code":"A116.00","system":"readv2"},{"code":"A117.00","system":"readv2"},{"code":"A120.00","system":"readv2"},{"code":"A120100","system":"readv2"},{"code":"A120200","system":"readv2"},{"code":"A120z00","system":"readv2"},{"code":"A123.00","system":"readv2"},{"code":"A130.00","system":"readv2"},{"code":"A130300","system":"readv2"},{"code":"A130z00","system":"readv2"},{"code":"A131.00","system":"readv2"},{"code":"A134.00","system":"readv2"},{"code":"A135.00","system":"readv2"},{"code":"A136000","system":"readv2"},{"code":"A15..11","system":"readv2"},{"code":"A15..13","system":"readv2"},{"code":"A153.00","system":"readv2"},{"code":"A154.00","system":"readv2"},{"code":"A160000","system":"readv2"},{"code":"A160200","system":"readv2"},{"code":"A166111","system":"readv2"},{"code":"A167000","system":"readv2"},{"code":"A167100","system":"readv2"},{"code":"A170.11","system":"readv2"},{"code":"A172100","system":"readv2"},{"code":"A172200","system":"readv2"},{"code":"A173000","system":"readv2"},{"code":"A173100","system":"readv2"},{"code":"A173300","system":"readv2"},{"code":"A173400","system":"readv2"},{"code":"Ayu1100","system":"readv2"},{"code":"F004.00","system":"readv2"},{"code":"F033311","system":"readv2"},{"code":"F040600","system":"readv2"},{"code":"F041300","system":"readv2"},{"code":"G520600","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('tuberculosis-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["tuberculosis-tuberculoma---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["tuberculosis-tuberculoma---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["tuberculosis-tuberculoma---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
