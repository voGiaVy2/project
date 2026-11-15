import os, time

def check():
    docx_path = r"d:\doan\baocao_GayThongMinh.docx"
    print("DOCX:", time.ctime(os.path.getmtime(docx_path)), os.path.getsize(docx_path))
    fig_dir = r"d:\doan\_tools\fig"
    for f in sorted(os.listdir(fig_dir)):
        if f.endswith('.png'):
            fp = os.path.join(fig_dir, f)
            print(f"{f:22s} {time.ctime(os.path.getmtime(fp))} {os.path.getsize(fp)} bytes")

if __name__ == '__main__':
    check()
