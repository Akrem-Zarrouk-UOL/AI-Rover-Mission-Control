# scripts/validate_preprocessed.py
from pathlib import Path
from PIL import Image
import numpy as np

imgs = list(Path("data/processed/hirise_128").glob("*.png"))
print("Images found:", len(imgs))
if imgs:
    im = Image.open(imgs[0])
    print("Shape:", np.array(im).shape, "mode:", im.mode)
