class CLI:
    def show_menu(self):
        print("\n=== SISTEM MANAJEMEN PRODUK ===")
        print("1. Tambah Produk")
        print("2. Lihat Produk")
        print("3. Cari Produk")
        print("4. Update Produk")
        print("5. Hapus Produk")
        print("6. Keluar")

    def get_input(self, message):
        return input(message)