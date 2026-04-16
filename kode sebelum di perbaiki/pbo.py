class A:
    def __init__(self):
        self.d = []

    def a(self, n, p, s):
        self.d.append({"n": n, "p": p, "s": s})

    def b(self):
        for i in self.d:
            print(i)

    def c(self, n):
        for i in self.d:
            if i["n"] == n:
                return i

    def dlt(self, n):
        for i in self.d:
            if i["n"] == n:
                self.d.remove(i)

    def upd(self, n, p, s):
        for i in self.d:
            if i["n"] == n:
                i["p"] = p
                i["s"] = s


x = A()

while True:
    print("1.Tambah 2.Lihat 3.Cari 4.Hapus 5.Update 6.Keluar")
    c = input("Pilih: ")

    if c == "1":
        n = input("Nama: ")
        p = int(input("Harga: "))
        s = int(input("Stok: "))
        x.a(n, p, s)

    elif c == "2":
        x.b()

    elif c == "3":
        n = input("Nama: ")
        print(x.c(n))

    elif c == "4":
        n = input("Nama: ")
        x.dlt(n)

    elif c == "5":
        n = input("Nama: ")
        p = int(input("Harga baru: "))
        s = int(input("Stok baru: "))
        x.upd(n, p, s)

    elif c == "6":
        break