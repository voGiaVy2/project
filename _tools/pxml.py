import sys, re, io, docx
from lxml import etree
d = docx.Document(r'd:\doan\_tools\tpl_plain.docx')
body = d.element.body
W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
paras = [e for e in body.iterchildren() if e.tag == W + 'p']
a, b = int(sys.argv[1]), int(sys.argv[2])
maxlen = int(sys.argv[3]) if len(sys.argv) > 3 else 1800
for i in range(a, b + 1):
    s = etree.tostring(paras[i], encoding='unicode')
    s = re.sub(r' xmlns:\w+="[^"]+"', '', s)
    s = re.sub(r'<w:rFonts[^>]*/>', '', s)
    print(f'--- P{i}\n' + s[:maxlen])
