import PySimpleGUI as sg

sg.theme_background_color("#ADD8E6")  # Biru muda
sg.theme_text_element_background_color("#ADD8E6")  # Biru muda

layout = [
    [sg.Text("DATA SISWA BARU", background_color="white", text_color="black", size=(20,1), justification="center")],
    [sg.Text("Nama Siswa", size=(15,1)), sg.Input(key="-NAMA_SISWA-")],
    [sg.Text("Tanggal Lahir", size=(15,1)), sg.Input(key="-TANGGAL_LAHIR-")],
    [sg.Text("Asal Sekolah", size=(15,1)), sg.Input(key="-ASAL_SEKOLAH-")],
    [sg.Text("Nama Ayah", size=(15,1)), sg.Input(key="-NAMA_AYAH-")],
    [sg.Text("Nama Ibu", size=(15,1)), sg.Input(key="-NAMA_IBU-")],
    [sg.Text("Nomor Telepon / HP", size=(15,1)), sg.Input(key="-NOMOR_TELEPON-")],
    [sg.Text("Alamat", size=(15,1)), sg.Input(key="-ALAMAT-")],
    [sg.Button("Hapus", button_color=("white", "orange")), sg.Button("Simpan", button_color=("white", "orange"))]
]

window = sg.Window("MainWindow", layout)

while True:
    event, values = window.read()
    if event == "Simpan":
        # Simpan data siswa baru
        sg.popup('Tersimpan')
        pass
    elif event == "Hapus":
        # Hapus data yang telah dimasukkan
        window["-NAMA_SISWA-"].update("")
        window["-TANGGAL_LAHIR-"].update("")
        window["-ASAL_SEKOLAH-"].update("")
        window["-NAMA_AYAH-"].update("")
        window["-NAMA_IBU-"].update("")
        window["-NOMOR_TELEPON-"].update("")
        window["-ALAMAT-"].update("")
    elif event == sg.WIN_CLOSED:
        break

window.close()