# -*- coding: utf-8 -*-
import docx
import shutil
import os
import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

# Đảm bảo đường dẫn import
sys.path.append(r'd:\doan\_tools')

from content_front import build_front
from content_ch1 import build_ch1
from content_ch2 import build_ch2
from content_ch3 import build_ch3
from content_ch4 import build_ch4
from content_conclusion_app import build_conclusion_app

SRC_FILE = r'd:\doan\baocao_GayThongMinh.docx'
BACKUP_FILE = r'd:\doan\baocao_GayThongMinh_backup.docx'
OUT_FILE = r'd:\doan\baocao_GayThongMinh.docx'

def main():
    print("=== BẮT ĐẦU QUÁ TRÌNH TẠO BÁO CÁO TOÀN DIỆN KHÓA LUẬN TỐT NGHIỆP ===")

    # 1. Sao lưu file gốc nếu chưa có bản sao lưu
    if not os.path.exists(BACKUP_FILE):
        print(f"[1/7] Tạo bản sao lưu file gốc: {BACKUP_FILE} ...")
        shutil.copyfile(SRC_FILE, BACKUP_FILE)
    else:
        print(f"[1/7] Bản sao lưu {BACKUP_FILE} đã tồn tại.")

    # 2. Mở file tài liệu từ backup nguyên bản
    print(f"[2/7] Mở tài liệu gốc từ {BACKUP_FILE} ...")
    doc = docx.Document(BACKUP_FILE)

    # 3. Cắt bỏ nội dung cũ từ sau đoạn Lời cảm ơn (sau index 92)
    # Đoạn 92 là dòng trắng kết thúc phần đầu (Bìa, Nhận xét GVHD/GVPB, Lời cảm ơn)
    print(f"Tổng số đoạn văn bản ban đầu: {len(doc.paragraphs)}")
    print(f"Tổng số bảng ban đầu: {len(doc.tables)}")

    p_cutoff = doc.paragraphs[92]._element
    parent = p_cutoff.getparent()
    found = False
    to_remove = []
    for child in list(parent):
        if child == p_cutoff:
            found = True
            continue
        if found:
            # Giữ lại sectPr cuối body nếu có
            if not child.tag.endswith('sectPr'):
                to_remove.append(child)

    print(f"[3/7] Cắt bỏ {len(to_remove)} phần tử XML cũ từ sau Lời cảm ơn...")
    for child in to_remove:
        parent.remove(child)

    print(f"Số đoạn văn bản sau khi cắt: {len(doc.paragraphs)}")

    # 4. Thêm ngắt trang để bắt đầu MỤC LỤC
    doc.add_page_break()

    # 5. Xây dựng phần đầu (Mục lục, Danh mục hình, Danh mục bảng, Danh mục từ viết tắt, Mở đầu)
    print("[4/7] Đang tạo phần đầu (Mục lục, Danh mục, Mở đầu)...")
    build_front(doc)

    # 6. Xây dựng Chương 1 & Chương 2
    print("[5/7] Đang tạo Chương 1 (Tổng quan) và Chương 2 (Cơ sở lý thuyết)...")
    build_ch1(doc)
    build_ch2(doc)

    # 7. Xây dựng Chương 3 & Chương 4
    print("[6/7] Đang tạo Chương 3 (Thiết kế hệ thống) và Chương 4 (Thực nghiệm đánh giá)...")
    build_ch3(doc)
    build_ch4(doc)

    # 8. Xây dựng Kết luận, Hướng phát triển, Tài liệu tham khảo, Phụ lục mã nguồn
    print("[7/7] Đang tạo Kết luận, Hướng phát triển, Tài liệu tham khảo và Phụ lục mã nguồn...")
    build_conclusion_app(doc)

    # 9. Lưu tài liệu hoàn chỉnh
    print(f"Đang lưu tài liệu hoàn chỉnh vào {OUT_FILE} ...")
    saved_path = OUT_FILE
    try:
        doc.save(OUT_FILE)
    except PermissionError as e:
        alt_path = r'd:\doan\baocao_GayThongMinh_HoanChinh.docx'
        print(f"Cảnh báo: Không thể ghi đè trực tiếp lên {OUT_FILE} (có thể do WPS/Word đang mở).")
        print(f"Đang lưu tài liệu vào file thay thế: {alt_path} ...")
        doc.save(alt_path)
        saved_path = alt_path

    file_size_mb = os.path.getsize(saved_path) / (1024 * 1024)
    print("=== HOÀN TẤT THÀNH CÔNG! ===")
    print(f"• File đã lưu tại: {saved_path}")
    print(f"• Tổng số đoạn văn bản (paragraphs): {len(doc.paragraphs)}")
    print(f"• Tổng số bảng biểu (tables): {len(doc.tables)}")
    print(f"• Kích thước file báo cáo: {file_size_mb:.2f} MB")

if __name__ == '__main__':
    main()
