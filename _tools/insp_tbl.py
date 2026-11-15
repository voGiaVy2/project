import re, docx
from lxml import etree
d = docx.Document(r'd:\doan\_tools\tpl_plain.docx')
t = d.tables[3]
s = etree.tostring(t._tbl, encoding='unicode')
s = re.sub(r' xmlns:\w+="[^"]+"', '', s)
s = re.sub(r' w:rsid\w*="[^"]+"', '', s)
s = re.sub(r' w14:\w+="[^"]+"', '', s)
with open(r'd:\doan\_tools\tbl3.txt', 'w', encoding='utf-8') as f:
    f.write(s[:6500])
# paragraph before table & caption para + next
W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
body = d.element.body
kids = list(body.iterchildren())
idx = kids.index(t._tbl)
with open(r'd:\doan\_tools\tbl3.txt', 'a', encoding='utf-8') as f:
    for k in (idx - 1, idx + 1):
        s2 = etree.tostring(kids[k], encoding='unicode')
        s2 = re.sub(r' xmlns:\w+="[^"]+"', '', s2)
        s2 = re.sub(r' w:rsid\w*="[^"]+"', '', s2)
        f.write('\n\n--- neighbor %d\n' % k + s2[:1800])
# footer
import zipfile
z = zipfile.ZipFile(r'd:\doan\baocao_GayThongMinh.docx')
open(r'd:\doan\_tools\footer_mine.txt', 'w', encoding='utf-8').write(z.read('word/footer1.xml').decode('utf8'))
open(r'd:\doan\_tools\settings_mine.txt', 'w', encoding='utf-8').write(z.read('word/settings.xml').decode('utf8'))
print('ok')
