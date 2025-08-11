# billing_system.py

# Function to read product details from file
def read_products(filename):
    products = {}
    try:
        with open(filename, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) != 3:
                    continue  # skip invalid lines
                product_id, product_name, price = parts
                products[product_id] = {
                    "name": product_name,
                    "price": float(price)
                }
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return None
    return products


# Function to take purchase details from the user
def take_purchases(products):
    purchases = []
    while True:
        product_id = input("Enter Product ID (or 'done' to finish): ").strip()
        if product_id.lower() == "done":
            break
        if product_id not in products:
            print("Invalid Product ID. Try again.")
            continue
        try:
            quantity = int(input("Enter quantity: "))
            if quantity <= 0:
                raise ValueError
        except ValueError:
            print("Invalid quantity. Please enter a positive integer.")
            continue

        purchases.append((product_id, quantity))
    return purchases


# Function to generate and save bill
def generate_bill(purchases, products, bill_filename):
    total_bill = 0
    try:
        with open(bill_filename, "w") as file:
            file.write("BILL SUMMARY\n")
            file.write("-----------------------------------\n")
            for product_id, quantity in purchases:
                product_name = products[product_id]["name"]
                unit_price = products[product_id]["price"]
                total = unit_price * quantity
                total_bill += total
                line = f"Product ID: {product_id}, Product Name: {product_name}, Quantity: {quantity}, Unit Price: {unit_price}, Total: {total}\n"
                file.write(line)
                print(line, end="")
            file.write("-----------------------------------\n")
            file.write(f"Total Bill: {total_bill}\n")
            print("-----------------------------------")
            print(f"Total Bill: {total_bill}")
    except Exception as e:
        print("Error writing bill:", e)


# Main function
def main():
    products = read_products("products.txt")
    if products is None:
        return

    purchases = take_purchases(products)

    if purchases:
        generate_bill(purchases, products, "bill.txt")
    else:
        print("No purchases made. Bill not generated.")


if __name__ == "__main__":
    main()
