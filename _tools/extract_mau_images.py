import os
from pptx import Presentation

prs = Presentation('mau.pptx')
os.makedirs('_tools/mau_extracted_images', exist_ok=True)
count = 0
for idx, slide in enumerate(prs.slides):
    for s_idx, shape in enumerate(slide.shapes):
        if shape.shape_type == 13: # picture
            image = shape.image
            ext = image.ext
            filename = f"_tools/mau_extracted_images/slide{idx+1}_pic{s_idx+1}_{shape.name}.{ext}"
            with open(filename, 'wb') as f:
                f.write(image.blob)
            print(f"Saved: {filename} ({len(image.blob)} bytes)")
            count += 1
print(f"Total extracted from mau.pptx: {count}")

