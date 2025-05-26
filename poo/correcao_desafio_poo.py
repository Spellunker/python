from datetime import datetime
from loja import Client, Salesperson, Sale


def main():
    client = Client("Maria Lima", 44)
    salesperson = Salesperson("Pedro Garrido", 36, 5000)
    sale1 = Sale(client, datetime.now(), 512)
    sale2 = Sale(client, datetime(2018, 6, 4), 256)
    client.register_sale(sale1)
    client.register_sale(sale2)
    print(f"Client: {client}", "(Adult)" if client.is_adult() else "")
    print(f"Salesperson: {salesperson}")

    total_value = client.sales_total()
    qty_sales = len(client.sales)
    print(f"Total: {total_value} in {qty_sales} sales")
    print(f"Last sale: {client.get_last_sale_date()}")


if __name__ == "__main__":
    main()
