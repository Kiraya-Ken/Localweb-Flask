import random
import string
from flask import Flask

app = Flask(__name__)

facts_list = [
    "Sebagian besar orang yang menderita kecanduan teknologi mengalami stres saat tidak membawa ponsel.",
    "Menurut sebuah studi, lebih dari 50% remaja menghabiskan lebih dari 3 jam sehari di media sosial.",
    "Studi tentang ketergantungan teknologi adalah salah satu bidang penelitian modern yang paling relevan."
]

@app.route("/")
def home():
    return '''
        <h1>Selamat Datang di Web Ketergantungan Teknologi!</h1>
        <p><a href="/random_fact">View a random fact!</a></p>
        <p><a href="/rahasia"> Masuk ke Halaman Rahasia (Lempar Koin)</a></p>
        <p><a href="/pass"> Masuk ke Halaman Rahasia (Generator Kata Sandi)</a></p>
    '''

@app.route("/random_fact")
def random_fact():
    return f'''
        <h1>Fakta Unik:</h1>
        <p>{random.choice(facts_list)}</p>
        <a href="/random_fact">Lihat fakta lain</a> | <a href="/">Kembali ke Beranda</a>
    '''

@app.route("/rahasia")
def secret_coin():
    hasil = random.choice(["Kepala ", "Ekor "])
    return f'''
        <h1> Halaman Rahasia: Lempar Koin!</h1>
        <h2>Hasil Lemparan: {hasil}</h2>
        <a href="/rahasia">Lempar Koin Lagi</a> | <a href="/">Kembali ke Beranda</a>
    '''

@app.route("/pass")
def generate_password():
    karakter = string.ascii_letters + string.digits + "!@#$%^&*"
    kata_sandi = "".join(random.choice(karakter) for _ in range(12))
    return f'''
        <h1> Generator Kata Sandi Rahasia</h1>
        <p>Kata sandi acak milikmu: <code><b>{kata_sandi}</b></code></p>
        <a href="/pass">Buat Kata Sandi Baru</a> | <a href="/">Kembali ke Beranda</a>
    '''

if __name__ == "__main__":
    app.run(debug=True)