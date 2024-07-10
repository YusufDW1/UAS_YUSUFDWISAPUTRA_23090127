class RestaurantQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, order):
        """Menambahkan pesanan baru ke dalam antrian"""
        self.queue.append(order)
        print(f"Pesanan '{order}' telah ditambahkan ke dalam antrian.")

    def dequeue(self):
        """Menghapus antrian dari depan"""
        if len(self.queue) > 0:
            order = self.queue.pop(0)
            print(f"Pesanan '{order}' telah dihapus dari antrian.")
            return order
        else:
            print("Antrian kosong. Tidak ada pesanan untuk dihapus.")
            return None

    def display(self):
        """Menampilkan seluruh antrian"""
        if len(self.queue) > 0:
            print("Daftar Antrian Pesanan:")
            for index, order in enumerate(self.queue):
                print(f"{index + 1}. {order}")
        else:
            print("Antrian kosong.")


if __name__ == "__main__":
    rq = RestaurantQueue()
    while True:
        print("\nMenu:")
        print("1. Tambah Pesanan")
        print("2. Hapus Pesanan")
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
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Opsi tidak valid. Silakan pilih antara 1-4.")
