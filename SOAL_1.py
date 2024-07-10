def main():
    mahasiswa = []

    while True:
        nim = input("Masukkan NIM: ")
        nama = input("Masukkan Nama: ")
        mahasiswa.append({"NIM": nim, "Nama": nama})

        tambah_lagi = input("Ingin tambah lagi? (Y/N): ").strip().upper()
        if tambah_lagi != 'Y':
            break

    print("\nData Mahasiswa:")
    for data in mahasiswa:
        print(f"NIM: {data['NIM']}, Nama: {data['Nama']}")

if __name__ == "__main__":
    main()
