import numpy as np
import matplotlib.pyplot as plt

# Mendefinisikan Variabel
a = 50  # Koefisien Difusivitas Termal
s = 0.5  # Panjang sisi [m]
waktu = 1.5  # Waktu simulasi [s]
node = 50  # Jumlah titik grid
dx = s / (node - 1)  # Jarak antar titik grid pada x
dy = s / (node - 1)  # Jarak antar titik grid pada y
dt = min(dx**2 / (4 * a), dy**2 / (4 * a))  # Ukuran langkah waktu [s] (pilih yang lebih kecil agar stabil)
t_nodes = int(waktu / dt)  # Jumlah iterasi simulasi
u = np.zeros((node, node)) + 20  # Suhu awal plat [degC] (2 dimensi)

# Kondisi batas
u[0, :] = 0  # Suhu tepi kiri
u[-1, :] = 100  # Suhu tepi kanan
u[:, 0] = np.linspace(0, 100, node)  # Suhu tepi bawah (variasi linear)
u[:, -1] = np.linspace(0, 100, node)  # Suhu tepi atas (variasi linear)

# Visualisasi distribusi suhu awal
fig, ax = plt.subplots()
ax.set_ylabel("y (cm)")
ax.set_xlabel("x (cm)")
pcm = ax.pcolormesh(u, cmap=plt.cm.jet, vmin=0, vmax=100)
plt.colorbar(pcm, ax=ax)

# Simulasi
counter = 0
suhu_rata_rata = []  # Inisialisasi array untuk menyimpan suhu rata-rata pada setiap iterasi waktu

# Inisialisasi plot untuk suhu rata-rata terhadap waktu
fig2, ax2 = plt.subplots()
line, = ax2.plot([], [], marker='o')
ax2.set_xlabel("Waktu (s)")
ax2.set_ylabel("Suhu Rata-Rata (Celcius)")
ax2.set_title("Grafik Suhu Rata-Rata terhadap Waktu")
ax2.grid(True)

while counter < waktu:
    w = u.copy()  # Menyalin data suhu untuk perhitungan

    for i in range(1, node - 1):  # Melooping setiap titik grid kecuali batas
        for j in range(1, node - 1):
            # Menghitung perubahan suhu berdasarkan persamaan Laplace 2D
            dd_ux = (w[i - 1, j] - 2 * w[i, j] + w[i + 1, j]) / dx**2
            dd_uy = (w[i, j - 1] - 2 * w[i, j] + w[i, j + 1]) / dy**2
            u[i, j] = dt * a * (dd_ux + dd_uy) + w[i, j]  # Suhu baru dihitung dan ditambahkan ke suhu lama

    pcm.set_array(u)  # Memperbarui plot distribusi suhu
    t_mean = np.mean(u)
    counter += dt  # Menambah waktu simulasi
    print(f"t: {counter:.3f} s, Suhu rata-rata: {t_mean:.2f} Celcius")
    ax.set_title(f"Distribusi Suhu t: {counter:.3f} s, suhu rata-rata={t_mean:.3f}")

    # Menyimpan suhu rata-rata pada setiap iterasi waktu
    suhu_rata_rata.append(t_mean)

    # Memperbarui plot suhu rata-rata terhadap waktu
    line.set_data(np.linspace(0, counter, len(suhu_rata_rata)), suhu_rata_rata)
    ax2.set_xlim(0, waktu)
    ax2.set_ylim(min(suhu_rata_rata) - 1, max(suhu_rata_rata) + 1)
    plt.pause(0.01)  # Menunda plot untuk animasi

# Menampilkan grafik suhu rata-rata terhadap waktu setelah simulasi selesai
plt.show()
