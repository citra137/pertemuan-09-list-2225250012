# Proses: membuat fungsi untuk menghitung rata-rata
def rata_rata(data):
    # Jika list kosong, fungsi mengembalikan nilai 0
    if len(data) == 0:
        return 0
    return sum(data) / len(data)


# Input: membuat list nilai mahasiswa
nilai = [75, 80, 65, 90, 88]

# Proses: menghitung rata-rata menggunakan fungsi
hasil = rata_rata(nilai)

# Output: menampilkan hasil rata-rata
print(f"Rata-rata = {hasil:.2f}")