def pp(p, l):
    hasil = p * l
    print("\t", p, " x ", l, " = ", hasil)
    menu()

def ling(r):
    if (r % 7) == 0:
        hasil = (22 * r * r) / 7
        print("\t", "(22/7)", " x ", r, " x ", r, " = ", hasil)
    else:
        hasil = (3.14) * r * r
        print("\t", "(3.14)", " x ", r, " x ", r, " = ", hasil)
    menu()

def seg(a, b, c):
    hasil = (a * b * c) / 2
    print("\t", "\t(", a, "x", b, "x", c, ")", " /2", " = ", hasil)
    menu()

def menu():
    print("============Menu Luas 2D============")
    print("\t1 Dimensi Persegi Panjang\t2 Dimensi Lingkaran")
    print("\t3 Dimensi Segitiga\t4 Keluar")
    print("====================================")
    try:
        menu = int(input("<Menu> : "))
        if menu == 1:
              x = int(input("Masukkan panjang : "))
              y = int(input("Masukkan lebar : "))
              pp(x, y)
        elif menu == 2:
              x = int(input("Masukkan jari-jari lingkaran : "))
              ling(x)
        elif menu == 3:
              x = int(input("Masukkan panjang sisi 1 : "))
              y = int(input("Masukkan panjang sisi 2 : "))
              z = int(input("Masukkan panjang sisi 3 : "))
              seg(x, y, z)
        elif menu == 4:
              input("<enter>")
        else:
              print("Bermasalah!!")
              input("<enter>")
    except:
        input("Anda tidak memasukkan angka dengan benar<enter untuk keluar>")

menu()
