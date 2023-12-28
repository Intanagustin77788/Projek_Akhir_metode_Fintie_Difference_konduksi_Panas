import numpy as np
import matplotlib.pyplot as plt

# Mendefinisikan Variabel
a = 500  # Koefisien Difusivitas Termal [m^2/s]
panjang = 2.5  # Panjang plat [m]
waktu = 1.5  # Waktu Simulasi [s]
node = 50  # Jumlah titik grid

dx = panjang / node  # Jarak antar titik grid [m]
dt = 0.5 * dx**2 / a  # Ukuran waktu simulasi [s]
t_n = int(waktu / dt)  # Jumlah iterasi simulasi
u = np.zeros(node)  # Suhu awal plat [degC]

# Kondisi Awal dan Batas
u[0] = 0  # Suhu ujung kiri plat [degC]
u[-1] = 100  # Suhu ujung kanan plat [degC]

# Inisialisasi array untuk menyimpan suhu rata-rata pada setiap iterasi waktu
suhu_rata_rata = []

# Visualisasi
fig, ax = plt.subplots()
ax.set_xlabel("x (cm)")
pcm = ax.pcolormesh([u], cmap=plt.cm.jet, vmin=0, vmax=100)  # Plot distribusi suhu
plt.colorbar(pcm, ax=ax)
ax.set_ylim([-2, 3])  # Batas skala y
counter = 0

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
        u[i] = (dt * a * (w[i - 1] - 2 * w[i] + w[i + 1]) / dx**2) + w[i]  # Perhitungan suhu baru berdasarkan persamaan difusi panas

    counter += dt  # Menambahkan waktu simulasi
    suhu_rata_rata.append(np.mean(u))  # Menyimpan suhu rata-rata pada setiap iterasi waktu
    print("t: {:.3f} s, suhu rata - rata: {:.2f} Celcius".format(counter, np.mean(u)))  # Menampilkan waktu dan suhu rata - rata

    # Memperbarui plot distribusi suhu
    pcm.set_array([u])
    ax.set_title("Distribusi Suhu pada t: {:.3f} s".format(counter))

    # Memperbarui plot suhu rata-rata terhadap waktu
    line.set_data(np.linspace(0, counter, len(suhu_rata_rata)), suhu_rata_rata)
    ax2.set_xlim(0, waktu)
    ax2.set_ylim(min(suhu_rata_rata) - 1, max(suhu_rata_rata) + 1)
    plt.pause(0.01)  # Menunda plot untuk animasi

# Menampilkan grafik suhu rata-rata terhadap waktu setelah simulasi selesai
plt.show()
