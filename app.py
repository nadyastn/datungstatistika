import streamlit as st
import pandas as pd
import numpy as np


def main():
    st.sidebar.header(":green[Web Apps Pengolahan Data Tunggal dalam Statistika]")
    task = st.sidebar.selectbox("Pilih Menu", ("Home", "Materi", "Contoh Soal", "Kalkulator Pengolahan Data Tunggal Statistika"))

    if task == "Home":
        Welcome_to_webapps()
    elif task == "Materi":
        penjelasan_materi()
    elif task == "Contoh Soal":
        Contoh_Soal()
    elif task == "Kalkulator Pengolahan Data Tunggal Statistika":
        masukkan_dan_pengolahan_data()
        
def Welcome_to_webapps():
    st.header(":red[Hallo!:wave:]")
    st.subheader("Welcome to Web Apps Pengolahan Data Tunggal dalam Statistika")
    st.write("Silakan pilih menu 'Kalkulator Pengolahan Data Tunggal Statistika' untuk mencari Rata-rata, Median, Range, Simpangan Rata-rata, Ragam, dan Simpangan Baku.")
    st.write("Semoga Membantu!!:wink:")

def masukkan_dan_pengolahan_data():
    st.header(":green[Pengolahan Data Tunggal dalam Statistika]")
    st.subheader("Kalkulator Pengolahan Data Tunggal Statistika")

    # Masukkan Data
    st.subheader("Masukkan Data!")
    rows = st.number_input("Banyak Data (n):", min_value=1, value=1)

    data = []
    for i in range(rows):
        value = st.number_input(f"Data {i+1}", value=0.00, format="%.4f")
        data.append(value)

    df = pd.DataFrame(data)
    st.write("Data yang Dimasukkan:")
    st.write(df)

    # Pengolahan Data
    st.subheader("Hasil Pengolahan Data:memo:")
    st.write("Rata-rata: ", np.mean(data))
    st.write("Median: ", np.median(data))
    st.write("Range/Jangkauan: ", np.round(np.max(data) - np.min(data), 2))
    st.write("Simpangan Rata-rata: ", np.round(np.mean(np.abs(data - np.mean(data))), 2))
    st.write("Ragam/Variasi: ", np.round(np.var(data), 2))
    st.write("Simpangan Baku/Standar Deviasi: ", np.round(np.std(data), 2))

def penjelasan_materi():
    st.header(":green[Pengolahan Data Tunggal dalam Statistika]")
    st.subheader("Apa itu Pengolahan Data Tunggal dalam Statistika?")
    st.write("Pengolahan data tunggal adalah proses pengumpulan, pengorganisasian, dan analisis data tunggal untuk memahami karakteristik dan informasi yang terkandung dalam data tersebut.")
    st.write("Dalam statistika, terdapat beberapa metode pengolahan data tunggal yang umum digunakan seperti menghitung nilai rata-rata, median, modus, simpangan baku, dan lain sebagainya. Tapi, dalam aplikasi ini hanya tersedia 6 output pengolahan data tunggal yang akan ditampilkan yaitu rata-rata, median, range/jangkauan, simpangan rata-rata, ragam/variasi, dan simpangan baku/standar deviasi.")
    st.write("1. Rata-rata")
    st.write ("Rata-rata adalah suatu bilangan yang mewakili keseluruhan data pengamatan. Artinya, rata-rata merupakan perwakilan kuantitas dari sekelompok data. Besar kecilnya nilai rata-rata dipengaruhi oleh jumlah semua data dan banyaknya data. Nilai rata-rata yang diperoleh dari pembagian antara jumlah nilai keseluruhan dengan banyak data.")
    st.write("Rumus rata-rata : x̄ = ∑x / n")
    st.write("2. Median")
    st.write("Median atau nilai tengah adalah pemusatan data yang membagi suatu data menjadi setengah (50%) data terkecil dan terbesarnya.Median adalah bilangan sentral dari suatu kumpulan dalam ukuran pemusatan data. Dimana, pertengahan data dari yang terkecil hingga terbesar. Akan tetapi jika ada 2 angka di tengah, median adalah rata-rata dari 2 angka tersebut.")
    st.write("Rumus median data tunggal ganjil : X( n+1)/2")
    st.write("Rumus median data genap : X n/2 + X (n/2 + 1 ) / 2")
    st.write("3. Range/Jangkauan")
    st.write("Rentang (range) atau disebut juga dengan jangkauan adalah selisih antara data dengan nilai yang terbesar dengan data denga nilai yang terkecil tersebut.")
    st.write("Rumus range/jangkauan : R = Xmax - Xmin")
    st.write("4. Simpangan Rata-rata")
    st.write("Simpangan Rata-rata adalah jumlah semua nilai mutlak selisih setiap nilai (xi) dengan nilai rata-rata (x̄) dibagi dengan banyak data (n).")
    st.write("Rumus simpangan rata-rata : SR = Σ| xi - x̄ | / n")
    st.write("5. Ragam/Variasi")
    st.write("Ragam Varians adalah nilai yang menunjukkan seberapa jauh sebuah kumpulan bilangan tersebar dari suatu data. Nilai ragam diperoleh dari pembagian antara jumlah masing-masing kuadrat selisih data xi dikurang dengan rata rata terhadap banyak data.")
    st.write("Rumus ragam/variasi : S²  = ∑( xi - x̄ )² ∕ n")
    st.write("6. Simpangan Baku/Standar Deviasi")
    st.write("Standar deviasi adalah nilai akar kuadrat dari suatu varians yang menunjukkan tingkat penyebaran data terhadap nilai rata-rata data tersebut. Nilai simpangan baku dari kumpulan data bisa = 0, lebih besar, maupun lebih kecil dari nol. Jika sama dengan nol, maka semua nilai dalam himpunan tersebut adalah sama. Sementara itu,nilai simpangan baku yang lebih besar atau kecil dari nol menandakan bahwa titik data individu jauh dari nilai rata-rata.")
    st.write("Rumus simpangan baku : S = √(∑( xi - x̄ ) ∕ n-1)")
    
def Contoh_Soal():
    st.header(":green[Pengolahan Data Tunggal dalam Statistika]")
    st.subheader("Contoh Soal dan Pembahasan")
    st.write("Nilai perolehan Matematika dari 5 anak adalah sebagai berikut: 88, 70, 85, 67 dan 90")
    st.write("Berapakah nilai rata-rata, median, range, simpangan rata-rata, ragam, dan simpangan baku matematika kelima anak tersebut?")
    st.write("Jawab :")
    st.write("a. Rata-rata")
    st.write("x̄ = ∑x / n")
    st.write("x̄=88 + 70 + 85 + 67 + 90 / 5")
    st.write("x̄ = 80")
    st.write("Jadi, nilai rata-rata kelima anak tersebut adalah 80.")
    st.write("b. Median")
    st.write("Urutkan kelompok data data dari nilai terkecil nilai terbesar atau sebaliknya dan tentukan nilai tengahnya.")
    st.write("Data : 67, 70, 85, 88, 90")
    st.write("Me = X( n+1)/2")
    st.write("Me = X ( 5+1) / 2")
    st.write("Me = X (6)/ 2")
    st.write("Me = X₃")
    st.write("Data ke tiga adalah 85, maka mediannya adalah 85.")
    st.write("c. Range")
    st.write("Xmax =90 dan Xmin=67")
    st.write("R = Xmax − Xmin")
    st.write("R = 90 – 67")
    st.write("R = 23")
    st.write("Jadi, jangkauan atau ragam data tersebut adalah 23.")
    st.write("d. Simpangan Rata-rata")
    st.write("SR = Σ| xi - x̄ | / n")
    st.write("SR = Σ| 88 - 80 | + | 70 - 80 | + | 85 - 80 | + | 67 - 80 | + | 90 - 80 | / 5")
    st.write("SR = 8 + 10 + 5 + 13 + 10 / 5")
    st.write("SR = 9.2")
    st.write("Jadi, simpangan rata-rata data tersebut adalah 9,2.")
    st.write("e. Ragam")
    st.write("S²  = ∑( xi - x̄ )² ∕ n")
    st.write("S² = ( 88 - 80 )² + ( 70 - 80 )² + ( 85 - 80 )² + ( 67 - 80 )² + ( 90 - 80 )² / 5 ")
    st.write("S² = 91.6")
    st.write("Jadi, ragam data tersebut adalah 91,6.")
    st.write("f. Simpangan Baku")
    st.write("S = √(∑( xi - x̄ ) ∕ n-1)")
    st.write("S = √( 88 - 80 )² + ( 70 - 80 )² + ( 85 - 80 )² + ( 67 - 80 )² + ( 90 - 80 )² / 5")
    st.write("S = √458/5")
    st.write("S = 9..57")
    st.write("Jadi simpangan baku data tersebut adalah 9,57.")
    
if __name__ == '__main__':
    main()