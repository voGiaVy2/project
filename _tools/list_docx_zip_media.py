import os
import zipfile

with zipfile.ZipFile('d:/doan/baocao_GayThongMinh.docx', 'r') as z:
    for name in z.namelist():
        if name.startswith('word/media/'):
            print(f"{name}: {z.getinfo(name).file_size} bytes")

