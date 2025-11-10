# scripts/preprocess_dem.py
import rasterio
from rasterio.enums import Resampling
from pathlib import Path

src = Path("data/raw/jezero_tile.tif")
out = Path("data/processed/jezero_256.tif")
if not src.exists():
    print("Put a small DEM tile at", src)
else:
    with rasterio.open(src) as dataset:
        scale_factor = 0.1  # downsample by factor (example)
        new_width = int(dataset.width * scale_factor)
        new_height = int(dataset.height * scale_factor)
        data = dataset.read(
            out_shape=(dataset.count, new_height, new_width),
            resampling=Resampling.bilinear
        )
        profile = dataset.profile
        profile.update({
            'height': new_height,
            'width': new_width,
            'transform': dataset.transform * dataset.transform.scale(
                (dataset.width / new_width),
                (dataset.height / new_height)
            )
        })
        out.parent.mkdir(parents=True, exist_ok=True)
        with rasterio.open(out, 'w', **profile) as dst:
            dst.write(data)
    print("Downsampled DEM saved to", out)
    print("✅ Preprocessing complete.")