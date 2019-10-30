def inputkan():
    x = input("Masukkan Angka yang mau di cek : ")
    cek_prima(x)

def cek_prima(angka):
    try:
        agk = int(angka)
        if agk > 1:
            for i in range(2, agk):
                if(agk % i) == 0:
                    print("\t", agk," bukan bilangan prima")
                    print("\t", i, " kali ", agk//i, " = ", agk)
                    break
            else:
                print("\t", agk, " adalah bilagan prima")
        elif agk == 1:
            print("\t", agk, "bukan bilangn prima")
        else:
            print("\tNegatif tidak termasuk")
        print("\n")
        inputkan()
    except:
        print("\tterjadi masalah!!!!")

inputkan()
