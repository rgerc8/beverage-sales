from pathlib import Path
import shutil
import kagglehub

# Download to Kaggle cache
src_path = Path(kagglehub.dataset_download("sebastianwillmann/beverage-sales"))
print("Downloaded to cache:", src_path)

# Destination inside your project
#dst_dir = Path("/home/rgerc/Projects/beverage-sales/data/raw")
dst_dir = Path("C:/Users/m24810/Projects/beverage-sales/data/raw")
# If it is the first time, you may want to create the destination directory:
# dst_dir.mkdir(parents=True, exist_ok=True)

# Copy files from cache to project
for item in src_path.rglob("*"):
    if item.is_file():
        rel = item.relative_to(src_path)
        target = dst_dir / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(item, target)

print("Copied dataset to:", dst_dir)