import csv
import os
import tkinter as tk
from tkinter.filedialog import askopenfilename

filename = askopenfilename() 
print(filename)


if os.path.exists("output.txt"):
  os.remove("output.txt")

outputFile = "output.txt";
out = open("output.txt", "a");

with open(filename, "r") as csv_file:
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
            out.write("\n\n")
        line += 1;
        
out.close;
csv_file.close;