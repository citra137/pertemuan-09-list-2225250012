# Input: membuat list nilai mahasiswa
nilai = [75, 55, 80, 60, 45, 90]

# Proses: menyiapkan list kosong untuk nilai yang lulus
lulus = []

# Proses: memilih nilai yang lebih besar atau sama dengan 60
for x in nilai:
    if x >= 60:
        lulus.append(x)

# Output: menampilkan nilai lulus dan jumlah mahasiswa yang lulus
print(f"Nilai lulus = {lulus}")
print(f"Jumlah lulus = {len(lulus)}")