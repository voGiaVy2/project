import io, msoffcrypto, zipfile, sys
f = open(r'd:\doan\PL2_Huynh_Luan.docx', 'rb')
o = msoffcrypto.OfficeFile(f); o.load_key(password='2026')
out = open(r'd:\doan\_tools\tpl_plain.docx', 'wb'); o.decrypt(out); out.close()
z = zipfile.ZipFile(r'd:\doan\_tools\tpl_plain.docx')
z.extractall(r'd:\doan\_tools\tpl_x')
print([ (i.filename, i.file_size) for i in z.infolist() if not i.filename.startswith('word/media')])
