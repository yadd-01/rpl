from services.product_service import ProductService
from ui.cli import CLI

def main():
    service = ProductService()
    cli = CLI()

    while True:
        cli.show_menu()
        choice = cli.get_input("Pilih: ")

        if choice == "1":
            name = cli.get_input("Nama: ")
            price = float(cli.get_input("Harga: "))
            stock = int(cli.get_input("Stok: "))
            service.create_product(name, price, stock)

        elif choice == "2":
            products = service.list_products()
            for product in products:
                print(product)

        elif choice == "3":
            name = cli.get_input("Nama: ")
            product = service.search_product(name)
            print(product if product else "Tidak ditemukan")

        elif choice == "4":
            name = cli.get_input("Nama: ")
            price = float(cli.get_input("Harga baru: "))
            stock = int(cli.get_input("Stok baru: "))
            updated = service.update_product(name, price, stock)
            print("Berhasil" if updated else "Gagal")

        elif choice == "5":
            name = cli.get_input("Nama: ")
            deleted = service.delete_product(name)
            print("Berhasil" if deleted else "Gagal")

        elif choice == "6":
            break

if __name__ == "__main__":
    main()