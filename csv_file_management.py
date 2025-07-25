
import csv


with open('bestseller.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader) # Skip the header row
    max_sales = 0
    best_selling_book = None
    
    for row in reader:
        sales = float(row[4])  # Assuming the sales data is in the 5th column
        if sales > max_sales:
            max_sales = sales
            best_selling_book = row
            
with open('best_selling_book.csv', 'w', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Book', 'Author', 'Sales in Millions'])
    writer.writerow([best_selling_book[0], best_selling_book[1], best_selling_book[4]])
print(f"The best-selling book is '{best_selling_book[0]}' by {best_selling_book[1]} with sales of {best_selling_book[4]} million.")
