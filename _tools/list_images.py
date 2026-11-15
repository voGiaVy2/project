import os
from PIL import Image

def scan_dir(p):
    res = []
    for root, dirs, files in os.walk(p):
        for f in files:
            if f.lower().endswith(('.png', '.jpg', '.jpeg')):
                full = os.path.join(root, f)
                try:
                    with Image.open(full) as img:
                        res.append((full, img.size, os.path.getsize(full)))
                except Exception as e:
                    pass
    return res

media = scan_dir('d:/doan/_tools/tpl_x/word/media')
print(f'Total media images in docx: {len(media)}')
for path, size, bytesize in media[:40]:
    print(f'{os.path.basename(path)}: {size}, {bytesize//1024}KB')

anh = scan_dir('d:/doan/anh')
print(f'\nTotal in anh: {len(anh)}')
for path, size, bytesize in anh:
    rel = os.path.relpath(path, 'd:/doan')
    print(f'{rel}: {size}, {bytesize//1024}KB')

