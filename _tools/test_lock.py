import os, time

p = r"d:\doan\baocao_GayThongMinh.docx"
print("File:", p)
print("Modified time:", time.ctime(os.path.getmtime(p)))
print("Size:", os.path.getsize(p), "bytes")
