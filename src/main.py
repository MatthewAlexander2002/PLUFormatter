import csv
import os
from pypdf import PdfWriter
import tkinter as tk
from tkinter.filedialog import askopenfilename

filename = askopenfilename() 

if os.path.exists("output.html"):
  os.remove("output.html")

outputFile = "output.html";
out = open("output.html", "a");

with open(filename, "r") as csv_file:
    csv_reader= csv.reader(csv_file, delimiter=',');
    line = 0;
    out.write("<!DOCTYPE html>\n <html>\n <style>\n p {font-family:arial; font-size:16px;}\n </style>\n <body>\n <p>\n")
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
            out.write("\n<br>")
        line += 1;
    out.write(" </p>\n </body>\n </html>")
        
out.close;
csv_file.close;