import csv
import requests
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = ROOT / "data" / "gbif" / "Ageratum" / "multimedia.txt"
IMAGE_FOLDER = ROOT / "data" / "gbif" / "Ageratum" / "images"
LIMIT = 500  # Misal kita set 5 untuk contoh

# Buat folder
IMAGE_FOLDER.mkdir(exist_ok=True)

existing = 0
print(f"📁 Mengecek folder... Gambar yang sudah ada: {existing}")
print(f"🚀 Memulai proses unduhan (Target: {LIMIT} gambar baru)\n")
print("-" * 50)

count = existing

with open(DATA_FILE, encoding="utf-8") as f:
    reader = csv.DictReader(f, delimiter="\t")

    for i, row in enumerate(reader):

        if i < existing:
            continue

        if row.get("type") != "StillImage":
            continue

        url = row.get("identifier")

        if not url:
            continue

        if not url.lower().endswith((".jpg", ".jpeg", ".png")):
            continue

        try:
            r = requests.get(url, timeout=10)

            if r.status_code != 200:
                # Log opsional kalau linknya mati/error 404
                print(f"❌ [Baris {i}] Link mati atau tidak bisa diakses: {url}")
                continue

            filename = IMAGE_FOLDER / f"img_{count}.jpg"

            with open(filename, "wb") as img:
                img.write(r.content)

            count += 1
            
            # ✅ LOG BARU YANG LEBIH JELAS
            print(f"✅ [{count}/{LIMIT}] Berhasil diunduh: {filename.name}")

            if count >= LIMIT:
                break

        except requests.exceptions.RequestException as e:
            # ✅ LOG KALAU TIMEOUT ATAU KONEKSI PUTUS
            print(f"⚠️ [{count}/{LIMIT}] Gagal mengunduh baris {i}: KONEKSI ERROR")
            pass

print("-" * 50)
print(f"✨ Proses selesai! Total gambar saat ini: {count}")