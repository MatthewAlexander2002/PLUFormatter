import csv
import os
# import tkinter as tk
# from tkinter.filedialog import askopenfilename

# # tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
# filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
# print(filename)


if os.path.exists("output.txt"):
  os.remove("output.txt")

outputFile = "output.txt";
out = open("output.txt", "a");

with open("testFiles\Shop_PLUs.txt", "r") as csv_file:
    csv_reader= csv.reader(csv_file, delimiter=',');
    line = 0;
    for row in csv_reader:
        if line == 0:
            line += 1;
        else:
            for column in range(20):
                if column == 0:
                    out.write(row[column]);
                    out.write("\t")
                else:
                    out.write(row[column]);
                    out.write(" ")
            out.write("\n")
        line += 1;
        
out.close;
csv_file.close;