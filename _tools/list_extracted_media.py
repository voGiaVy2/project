import os
import re

files = os.listdir('d:/doan/_tools/report_media')
print(f"Files in report_media: {len(files)}")
files.sort(key=lambda x: [int(c) if c.isdigit() else c for c in re.split(r'(\d+)', x)])
for f in files:
    full = os.path.join('d:/doan/_tools/report_media', f)
    print(f"{f}: {os.path.getsize(full)} bytes")

