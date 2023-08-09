# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"A17","system":"icd10"},{"code":"A18","system":"icd10"},{"code":"A19","system":"icd10"},{"code":"B20.0","system":"icd10"},{"code":"B90","system":"icd10"},{"code":"J65","system":"icd10"},{"code":"K23.0","system":"icd10"},{"code":"K67.3","system":"icd10"},{"code":"K93.0","system":"icd10"},{"code":"M01.1","system":"icd10"},{"code":"M49.0","system":"icd10"},{"code":"M90.0","system":"icd10"},{"code":"N33.0","system":"icd10"},{"code":"N74.0","system":"icd10"},{"code":"N74.1","system":"icd10"},{"code":"P37.0","system":"icd10"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('tuberculosis-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["tuberculosis---secondary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["tuberculosis---secondary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["tuberculosis---secondary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
