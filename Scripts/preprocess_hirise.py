# scripts/preprocess_hirise.py
import os
import zipfile
from PIL import Image
from pathlib import Path

RAW = Path("data/raw")
OUT = Path("data/processed/hirise_128")
OUT.mkdir(parents=True, exist_ok=True)

def extract_and_resize(zip_path, out_dir, size=(128,128), max_images=2000):
    with zipfile.ZipFile(zip_path, 'r') as z:
        names = [n for n in z.namelist() if n.lower().endswith(('.jpg','.png','.jpeg','.tif'))]
        count = 0
        for n in names:
            if count >= max_images:
                break
            try:
                with z.open(n) as f:
                    img = Image.open(f).convert("L")  # grayscale
                    img = img.resize(size)
                    img.save(out_dir / f"img_{count:05d}.png")
                    count += 1
            except Exception as e:
                print("skip", n, e)
    print("Saved", count, "images to", out_dir)

if __name__ == "__main__":
    zipfile_path = RAW / "hirise_landmarks_v3.zip"
    if not zipfile_path.exists():
        print("ERROR: download the zip into", zipfile_path)
    else:
        extract_and_resize(zipfile_path, OUT)
        print("✅ Preprocessing complete.")