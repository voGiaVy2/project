import os
import zipfile

os.makedirs('d:/doan/_tools/report_media', exist_ok=True)
count = 0
with zipfile.ZipFile('d:/doan/baocao_GayThongMinh.docx', 'r') as z:
    for name in z.namelist():
        if name.startswith('word/media/'):
            base = os.path.basename(name)
            out_path = os.path.join('d:/doan/_tools/report_media', base)
            with open(out_path, 'wb') as f:
                f.write(z.read(name))
            count += 1
print(f"Extracted {count} images from baocao_GayThongMinh.docx to _tools/report_media")

