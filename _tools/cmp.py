import zipfile, re, sys
out = open(r'd:\doan\_tools\cmp.txt', 'w', encoding='utf-8')
def P(*a):
    print(*a, file=out)
for n, p in [('mine', r'd:\doan\baocao_GayThongMinh.docx'), ('tpl', r'd:\doan\_tools\tpl_plain.docx')]:
    z = zipfile.ZipFile(p)
    P(n, [(i.filename, i.file_size) for i in z.infolist() if 'media' not in i.filename and 'fonts' not in i.filename and 'customXml' not in i.filename])
    s = z.read('word/styles.xml').decode('utf8')
    P(sorted(set(re.findall(r'w:styleId="([^"]+)"', s))))
    d = z.read('word/document.xml').decode('utf8')
    P('sectPr', len(re.findall('<w:sectPr', d)), 'instrText', len(re.findall('w:instrText', d)), 'fldSimple', len(re.findall('fldSimple', d)))
    P(re.findall(r'<w:instrText[^>]*>([^<]*)', d)[:20])
    for m in re.findall(r'<w:sectPr.*?</w:sectPr>', d, flags=re.S)[:4]:
        P(m)
    # style definitions of key styles
    for sid in ['Content', 'Heading1', 'Heading2', 'Heading3', 'Heading4', 'Heading1N', 'Caption', 'Normal', 'tableoffigures']:
        m = re.search(r'<w:style [^>]*w:styleId="%s".*?</w:style>' % sid, s, flags=re.S)
        P(sid, m.group(0) if m else None)
    P('=======')
print('ok')
