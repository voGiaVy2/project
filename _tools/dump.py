import sys, io, docx, msoffcrypto
src, out = sys.argv[1], sys.argv[2]
pw = sys.argv[3] if len(sys.argv) > 3 else None
if pw:
    f = open(src, 'rb'); o = msoffcrypto.OfficeFile(f); o.load_key(password=pw)
    b = io.BytesIO(); o.decrypt(b); d = docx.Document(b)
else:
    d = docx.Document(src)
from docx.oxml.ns import qn
body = d.element.body
pi = 0
ti = 0
with open(out, 'w', encoding='utf-8') as w:
    paras = {p._p: p for p in d.paragraphs}
    tabs = {t._tbl: t for t in d.tables}
    for el in body.iterchildren():
        if el.tag == qn('w:p'):
            p = paras[el]
            extra = ''
            if el.findall('.//' + qn('w:drawing')) or el.findall('.//' + qn('w:pict')):
                extra += ' [IMG]'
            if el.findall('.//' + qn('w:sectPr')):
                extra += ' [SECT]'
            if el.findall('.//' + qn('w:br')):
                for br in el.findall('.//' + qn('w:br')):
                    if br.get(qn('w:type')) == 'page':
                        extra += ' [PAGEBREAK]'
            w.write(f'P{pi} <{p.style.name}> {p.text}{extra}\n')
            pi += 1
        elif el.tag == qn('w:tbl'):
            t = tabs[el]
            w.write(f'TABLE{ti} rows={len(t.rows)}\n')
            for r in t.rows:
                w.write('   | ' + ' | '.join(c.text.replace('\n', ' / ') for c in r.cells) + '\n')
            ti += 1
print('done', pi, ti)
