import turtle

# Membuat jendela untuk menggambar
window = turtle.Screen()
window.title("Gambar Gabungan Menggunakan Turtle")

# Membuat objek turtle
pen = turtle.Turtle()

# Menggambar jajar genjang

pen.forward(100)  # Sisi pertama
pen.left(45)      # Belok 45 derajat ke kiri
pen.forward(150)  # Sisi kedua
pen.left(135)     # Belok 135 derajat ke kiri
pen.forward(100)  # Sisi ketiga
pen.left(45)      # Belok 45 derajat ke kiri
pen.forward(150)  # Sisi keempat

# Pindah ke posisi baru untuk menggambar belah ketupat
pen.penup()       # Angkat pena
pen.goto(200, 0)  # Pindah ke posisi baru
pen.pendown()     # Turunkan pena

# Menggambar belah ketupat
for _ in range(2):
    pen.left(45)      # Belok 45 derajat ke kiri
    pen.forward(100)  # Sisi pertama
    pen.left(135)     # Belok 135 derajat ke kiri
    pen.forward(100)  # Sisi kedua
    pen.left(45)      # Belok 45 derajat ke kiri
    pen.forward(100)  # Sisi ketiga
    pen.left(135)     # Belok 135 derajat ke kiri
    pen.forward(100)  # Sisi keempat

# Pindah ke posisi baru untuk menggambar segitiga
pen.penup()       # Angkat pena
pen.goto(-200, 0)  # Pindah ke posisi baru
pen.pendown()     # Turunkan pena

# Menggambar segitiga
for _ in range(3):
    pen.forward(100)  # Menggambar sisi segitiga
    pen.left(120)     # Belok 120 derajat ke kiri

# Pindah ke posisi baru untuk menggambar persegi panjang
pen.penup()       # Angkat pena
pen.goto(-200, 150)  # Pindah ke posisi baru
pen.pendown()     # Turunkan pena

# Menggambar persegi panjang
for _ in range(2):
    pen.forward(200)  # Menggambar sisi panjang
    pen.left(90)      # Belok 90 derajat
    pen.forward(100)  # Menggambar sisi pendek
    pen.left(90)      # Belok lagi 90 derajat

# Pindah ke posisi baru untuk menggambar trapesium
pen.penup()       # Angkat pena
pen.goto(0, 200)  # Pindah ke posisi baru
pen.pendown()     # Turunkan pena

# Menggambar trapesium
pen.forward(100)
pen.left(45)
pen.forward(50)
pen.left(135)
pen.forward(100)
pen.left(45)
pen.forward(50)

# Menutup jendela saat di-klik
window.exitonclick()