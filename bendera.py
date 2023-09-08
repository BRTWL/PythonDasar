import turtle

# Inisialisasi objek turtle
flag = turtle.Turtle()

# Fungsi untuk menggambar persegi panjang dengan warna tertentu
def draw_rectangle(color, width, height):
    flag.begin_fill()
    flag.fillcolor(color)
    for _ in range(2):
        flag.forward(width)
        flag.right(90)
        flag.forward(height)
        flag.right(90)
    flag.end_fill()

# Atur ukuran layar turtle
screen = turtle.Screen()
screen.setup(width=600, height=400)

# Gambar warna merah pada bagian atas bendera
flag.penup()
flag.goto(-300, 200)
flag.pendown()
draw_rectangle("red", 600, 200)

# Gambar warna putih pada bagian bawah bendera
flag.penup()
flag.goto(-300, 0)
flag.pendown()
draw_rectangle("white", 600, 200)

# Matikan turtle saat selesai
flag.hideturtle()

# Tahan tampilan bendera
turtle.done()