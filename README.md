
# 🚀 Big Data Technology – Praktikum 1

**Setup Environment & Git Workflow**
Prodi Teknologi Informasi – UIN Antasari
Lecturer: Muhayat, M.IT

---

## 📌 Deskripsi Project

Praktikum ini membangun **fondasi environment Data Engineer modern** menggunakan stack industri:

* Python
* PySpark
* MongoDB Atlas (Cloud)
* Git & GitHub
* VS Code + PowerShell

Project ini mensimulasikan workflow profesional:
Local Development → Distributed Processing → Cloud Database → Version Control

---

## 🏗️ Technology Stack

### 💻 VS Code

Development environment utama untuk coding dan integrasi terminal.

### 🐍 Python 3.10+

Bahasa utama untuk pemrosesan data dan PySpark.

### ⚡ PySpark

Engine distributed processing berbasis Apache Spark.

### ☁️ MongoDB Atlas

Cloud NoSQL database (Free Tier M0).

### 🔁 Git & GitHub

Version control dan repository online.

---

## 📂 Struktur Project

```
bigdata-project/
│
├── data/
├── cloud_storage/
├── scripts/
│   ├── simple_job.py
│   └── test_mongo.py
├── notebooks/
├── reports/
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Environment

### 1️⃣ Install Dependency

```bash
pip install pyspark
pip install pymongo
```

Buat file `requirements.txt`:

```
pyspark
pymongo
```

Install sekaligus:

```bash
pip install -r requirements.txt
```

---

## 🔥 Menjalankan Spark Job

File: `scripts/simple_job.py`

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("SimpleJob") \
    .getOrCreate()

data = [("A", 10), ("B", 20), ("A", 30)]
columns = ["category", "value"]

df = spark.createDataFrame(data, columns)
df.groupBy("category").sum("value").show()

spark.stop()
```

Jalankan:

```bash
python scripts/simple_job.py
```

Output yang diharapkan:

```
+--------+----------+
|category|sum(value)|
+--------+----------+
|       A|        40|
|       B|        20|
+--------+----------+
```

---

## ☁️ Setup MongoDB Atlas

1. Buat cluster M0 Free Tier
2. Tambahkan Database User
3. Allow IP Address (0.0.0.0/0)
4. Ambil connection string
5. Test koneksi dengan:

```bash
python scripts/test_mongo.py
```

Jika berhasil, akan muncul:

```
Koneksi berhasil!
```

---

## 🔁 Git Workflow

Inisialisasi repository:

```bash
git init
git add .
git commit -m "initial project setup"
```

Hubungkan ke GitHub:

```bash
git remote add origin <URL_REPOSITORY>
git branch -M main
git push -u origin main
```

---

## 📸 Output Wajib Praktikum

Mahasiswa wajib mengumpulkan:

* Screenshot Spark berjalan
* Screenshot MongoDB Atlas (Status ACTIVE)
* Screenshot GitHub Repository
* File `simple_job.py`
* Screenshot hasil eksekusi Spark

---

## 🧠 Insight Praktikum

Praktikum ini bukan tentang analitik.

Tapi tentang:

* Environment reproducibility
* Cloud readiness
* Distributed computing mindset
* Professional Git workflow

Ini adalah fondasi sebelum masuk ke:

* ETL Pipeline
* Data Warehouse
* Streaming
* Machine Learning

---

## 🎯 Status

✅ PySpark Installed
✅ MongoDB Connected
✅ Git Initialized
✅ Spark Job Running

---

## 👩‍💻 Author

Mahmudah-TI23A
230104040220
Big Data Technology Track

