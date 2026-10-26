print("Enter the barcode among the following options: s399, s499, s599, s699, s799, s899, s999")
enter_barcode=input("Enter the barcode: ")
quantity=int(input("Enter the quantity: "))
valid_barcodes=["s399","s499","s599","s699","s799","s899","s999"]
customer_name=input("Enter customer name: ")
customer_no=input("Enter customer number: ")

if enter_barcode in valid_barcodes:
    if enter_barcode=="s399":
        price=399
        article_name="shirt"
    elif enter_barcode=="s499":
        price=499
        article_name="shirt"
    elif enter_barcode=="s599":
        price=599
        article_name="shirt"
    elif enter_barcode=="s699":
        price=699
        article_name="shirt"
    elif enter_barcode=="s799":
        price=799
        article_name="shirt"
    elif enter_barcode=="s899":
        price=899
        article_name="shirt"
    elif enter_barcode=="s999":
        price=999
        article_name="shirt"

    print("----------Bill Details-----------")
    print(f"Customer Name: {customer_name}")
    print(f"Customer Number: {customer_no}")
    print(f"Article Name: {article_name}")
    print(f"Price: {price}")
    print(f"Quantity: {quantity}")  
    total_price=price*quantity
    print(f"Total price for {quantity} {article_name} is: {total_price}") 