from Modul import RestaurantQueue

if __name__ == "__main__":
    rq = RestaurantQueue()
    while True:
        print("\nMenu:")
        print("1. Tambah Pesanan")
        print("2. Hapus Pesanan4")
        print("3. Tampilkan Antrian")
        print("4. Keluar")

        choice = input("Pilih opsi: ")

        if choice == '1':
            order = input("Masukkan nama pesanan: ")
            rq.enqueue(order)
        elif choice == '2':
            rq.dequeue()
        elif choice == '3':
            rq.display()
        elif choice == '4':
            print("Terima kasih!")
            break
        else:
            print("Opsi tidak valid.")
