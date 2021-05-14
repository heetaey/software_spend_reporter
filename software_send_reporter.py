import csv
import sys


"""Reads the csv file path provided from the user.
Args:
    filepath (str): The csv file path

Returns:
    dictionary: a dictionary that is processed from the csv file with
                header values of vendor, product, and amount.
"""
def read_data(filepath):
    fileinput = filepath
    with open(fileinput, 'r') as file:
        reader = csv.DictReader(file)
        data_dict = {}

        for row in reader:
            vendor = str(row["Vendor"])
            prod = str(row["Product"])
            amount = int(row["Amount"])

            datum = data_dict.get(vendor, dict())
            datum[prod] = amount + datum.get(prod, 0)

            data_dict[vendor] = datum
        
        data_dict = sorted(data_dict.items())
    
    return data_dict


"""Reformats the amount to a readable dollar values.
Args:
    num (int): The amount value

Returns:
    Formatted num value
"""
def currency_format(num):
    return "${:,.2f}".format(num)


"""Processes the data from the read_data function.
Args:
    data(dictionary): The processed data from the target .csv file

"""
def process_data(data):
    for items in data:
        output = []
        vendor = items[0]
        product = items[1]
        total_amount = 0

        for amount in product.keys():
            total_amount += product[amount]
            output.append((amount, product[amount]))
        
        print(vendor, currency_format(total_amount))

        for products in sorted(output):
            print(" ", products[0], currency_format(products[1]))


if __name__ == "__main__":
    path = sys.argv[1]
    print()
    db = read_data(path)
    process_data(db)
    print()