import pandas as pd

data = {
    "Mahasiswa": ["Mahasiswa 1", "Mahasiswa 2", "Mahasiswa 3"],
    "Algoritma dan Struktur Data 2": [90, 50, 65],
    "Matematika Diskrit": [80, 60, 70]
}

df = pd.DataFrame(data).set_index("Mahasiswa")

print("Data Mahasiswa:\n", df.to_string(), "\n")

rata_rata_mata_kuliah = df.mean(axis=0)
print("Rata-rata nilai untuk setiap mata kuliah:\n", rata_rata_mata_kuliah.to_string(), "\n")

rata_rata_mahasiswa = df.mean(axis=1)
df['Rata-rata'] = rata_rata_mahasiswa
print("Rata-rata nilai untuk setiap mahasiswa:\n", df.to_string(), "\n")