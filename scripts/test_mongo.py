from pymongo import MongoClient

# Ganti teks di dalam tanda kutip di bawah ini dengan Connection String Anda
# Contoh: "mongodb+srv://mudah123:mudah123@cluster0.abcde.mongodb.net/"
uri = "mongodb+srv://mudah123:mudah321@cluster0.un0rblk.mongodb.net/"

try:
    client = MongoClient(uri)
    print("Koneksi berhasil!")
    # Menampilkan daftar database yang ada di MongoDB Atlas
    print(client.list_database_names())
except Exception as e:
    print(f"Koneksi gagal: {e}")