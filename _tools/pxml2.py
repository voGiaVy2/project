import sys, re, docx
from lxml import etree
path = sys.argv[1]; a = int(sys.argv[2]); b = int(sys.argv[3]); maxlen = int(sys.argv[4]); outp = sys.argv[5]
d = docx.Document(path)
W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
paras = [e for e in d.element.body.iterchildren() if e.tag == W + 'p']
with open(outp, 'w', encoding='utf-8') as f:
    for i in range(a, b + 1):
        s = etree.tostring(paras[i], encoding='unicode')
        s = re.sub(r' xmlns:\w+="[^"]+"', '', s)
        s = re.sub(r'<w:rFonts[^>]*/>', '', s)
        s = re.sub(r' w:rsid\w*="[^"]+"', '', s)
        s = re.sub(r' w14:\w+="[^"]+"', '', s)
        f.write(f'--- P{i}\n' + s[:maxlen] + '\n')
print('ok')
