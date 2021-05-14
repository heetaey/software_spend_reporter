# Software Send Reporter

A console application that reads in software spend data and outputs a report summarizing that data.

## Description

The input file is a comma separated values (CSV) file that contains a list of software spend transactions. It has four columns: 
•	Transaction Date: When the purchase was made
•	Vendor: The vendor that was paid in this transaction
•	Product: The software product that was purchased
•	Amount: The amount, in US Dollars, that was spent in this transaction

## Getting Started

### Dependencies

* The code was written in Python3 with the included csv library
* csv file needs to have four follwing head-columns for the application to run properly:
    - Transaction Date
    - Vendor
    - Product
    - Amount

### Installing

* You can run this program by downloading the zip file or clone this repository on the local machine. No modification is needed to run this program.

### Executing program

* To run the program, navigate to the folder where the .py file is located. Type the code provided below with the proper file path name given on the Terminal/Bash
```
python3 ./software_spend_reporter.py /path/to/inputfile.csv
```

## Authors

Heetae Yang

## Version History

* 0.1
    * Initial Release