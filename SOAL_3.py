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
