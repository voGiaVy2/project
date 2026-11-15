import os

images = [
    '_tools/mau_extracted_images/slide1_pic9_Picture 6.png',
    '_tools/mau_extracted_images/slide1_pic10_Picture 8.png',
    '_tools/tpl_x/word/media/image2.png',
    '_tools/tpl_x/word/media/image16.png',
    '_tools/tpl_x/word/media/image17.png',
    'DH/smart_cane_3d_design.jpg',
    '_tools/tpl_x/word/media/image18.jpg',
    '_tools/tpl_x/word/media/image8.png',
    '_tools/tpl_x/word/media/image19.png',
    '_tools/tpl_x/word/media/image20.png',
    '_tools/tpl_x/word/media/image22.png',
    '_tools/tpl_x/word/media/image23.png',
    '_tools/tpl_x/word/media/image24.png',
    '_tools/tpl_x/word/media/image27.png',
    '_tools/tpl_x/word/media/image28.png',
    '_tools/tpl_x/word/media/image29.png',
    '_tools/tpl_x/word/media/image31.png',
    '_tools/tpl_x/word/media/image32.png',
    '_tools/tpl_x/word/media/image33.png',
    '_tools/tpl_x/word/media/image34.png',
    '_tools/tpl_x/word/media/image35.png'
]

for img in images:
    exists = os.path.exists(img)
    size = os.path.getsize(img) if exists else 0
    print(f"{'FOUND' if exists else 'MISSING'}: {img} ({size} bytes)")

