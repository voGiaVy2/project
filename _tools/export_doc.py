# -*- coding: utf-8 -*-
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

doc = docx.Document()

# Margin 2cm
for s in doc.sections:
    s.top_margin = Inches(0.8)
    s.bottom_margin = Inches(0.8)
    s.left_margin = Inches(0.8)
    s.right_margin = Inches(0.8)

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

# Tiêu đề
p_title = doc.add_paragraph()
p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
run_title = p_title.add_run('BẢNG TRA CỨU SƠ ĐỒ ĐẤU CHÂN ESP32-S3 ĐỂ LÀM MẠCH IN PCB')
run_title.font.name = 'Arial'
run_title.font.size = Pt(16)
run_title.font.bold = True
run_title.font.color.rgb = RGBColor(15, 23, 42)

p_sub = doc.add_paragraph()
p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
run_sub = p_sub.add_run('DỰ ÁN: GẬY THÔNG MINH HỖ TRỢ NGƯỜI CAO TUỔI (SMART CANE IoT)\nĐộ chính xác: 100% chuẩn tuyệt đối theo mã nguồn vi điều khiển thực tế')
run_sub.font.name = 'Arial'
run_sub.font.size = Pt(10.5)
run_sub.font.italic = True
run_sub.font.color.rgb = RGBColor(71, 85, 105)

doc.add_paragraph()

# BẢNG TỔNG HỢP NHANH CÁC CHÂN
h1 = doc.add_paragraph()
r_h1 = h1.add_run('I. BẢNG TỔNG HỢP CÁC CHÂN ESP32-S3 CẦN ĐI DÂY TRÊN PCB')
r_h1.font.name = 'Arial'
r_h1.font.size = Pt(12)
r_h1.font.bold = True
r_h1.font.color.rgb = RGBColor(30, 58, 138)

table = doc.add_table(rows=1, cols=4)
table.alignment = WD_TABLE_ALIGNMENT.CENTER
hdr_cells = table.rows[0].cells
headers = ['STT', 'Chân trên ESP32-S3', 'Thiết bị ngoại vi kết nối', 'Chức năng kỹ thuật theo Code']

for i, title in enumerate(headers):
    hdr_cells[i].text = title
    set_cell_background(hdr_cells[i], '1E3A8A')
    set_cell_margins(hdr_cells[i], 120, 120, 120, 120)
    for p in hdr_cells[i].paragraphs:
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in p.runs:
            r.font.name = 'Arial'
            r.font.size = Pt(9.5)
            r.font.bold = True
            r.font.color.rgb = RGBColor(255, 255, 255)

data = [
    ('1', 'GPIO 0', 'Nút bấm hủy ngã / Tắt còi (BOOT)', 'INPUT_PULLUP: Nhấn nối GND để hủy báo ngã & tắt còi tức thì'),
    ('2', 'GPIO 4', 'Còi chip báo động (Buzzer)', 'Active HIGH + Xung tone 2000Hz: HIGH = Kêu, LOW = Tắt. Sau 30s té ngã sẽ tự động hú'),
    ('3', 'GPIO 5', 'Cầu phân áp đo dung lượng Pin', 'ADC1_CH4: Đọc điện áp pin 18650 qua cầu chia 1:2 (100kΩ / 100kΩ)'),
    ('4', 'GPIO 6', 'Mạch kích Motor rung (MOSFET 075N03L)', 'PWM / Digital Out: Xuất HIGH kích rung khi gặp vật cản 3 - 80cm'),
    ('5', 'GPIO 7', 'Nút bấm khẩn cấp SOS trên tay cầm', 'INPUT_PULLUP: Bấm nút nối GND để chủ động gọi cứu hộ SOS ngay'),
    ('6', 'GPIO 8', 'Cảm biến té ngã MPU-6050 (SDA)', 'I2C Data: Đọc dữ liệu gia tốc 3 trục để nhận diện ngã'),
    ('7', 'GPIO 9', 'Cảm biến té ngã MPU-6050 (SCL)', 'I2C Clock: Xung nhịp truyền dữ liệu I2C'),
    ('8', 'GPIO 16', 'Cảm biến siêu âm HC-SR04 (TRIG)', 'Digital Output: Phát xung kích siêu âm 10µs dò vật cản'),
    ('9', 'GPIO 17', 'Cảm biến siêu âm HC-SR04 (ECHO)', 'Digital Input: Nhận xung phản hồi (qua cầu trở 1k/2k hạ về 3.3V)'),
    ('10', 'GPIO 18', 'Đèn pin LED rọi đường ban đêm', 'Digital Output: Nối qua trở 220Ω vào cực (+) bóng LED 5mm'),
    ('11', '5V (VIN)', 'Nguồn cấp 5V từ Module MH-CD42', 'Cấp nguồn nuôi toàn mạch: ESP32-S3, Còi, Siêu âm, Motor rung'),
    ('12', '3V3', 'Nguồn 3.3V cho cảm biến MPU-6050', 'Lấy từ chân 3V3 của ESP32 cấp cho chân VCC module GY-521'),
    ('13', 'GND', 'Mass chung toàn hệ thống (Ground)', 'Nối chung toàn bộ Mass: Pin, CD42, ESP32, MPU6050, Siêu âm, Còi, Rung, LED'),
]

for row_idx, row_data in enumerate(data):
    row_cells = table.add_row().cells
    bg = 'F8FAFC' if row_idx % 2 == 1 else 'FFFFFF'
    for c_idx, val in enumerate(row_data):
        row_cells[c_idx].text = val
        set_cell_background(row_cells[c_idx], bg)
        set_cell_margins(row_cells[c_idx], 80, 80, 100, 100)
        p = row_cells[c_idx].paragraphs[0]
        if c_idx == 0:
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in p.runs:
            r.font.name = 'Arial'
            r.font.size = Pt(9.0)
            if c_idx == 1:
                r.font.bold = True
                r.font.color.rgb = RGBColor(185, 28, 28)

doc.add_paragraph()

# CHI TIẾT 9 MỤC
h2 = doc.add_paragraph()
r_h2 = h2.add_run('II. HƯỚNG DẪN ĐẤU CHÂN CHI TIẾT TỪNG MODULE NGOẠI VI')
r_h2.font.name = 'Arial'
r_h2.font.size = Pt(12)
r_h2.font.bold = True
r_h2.font.color.rgb = RGBColor(30, 58, 138)

sections_data = [
    ('1. CẢM BIẾN TÉ NGÃ (MPU-6050 / GY-521)', [
        '• Chân SDA  --> Nối vào GPIO 8 của ESP32',
        '• Chân SCL  --> Nối vào GPIO 9 của ESP32',
        '• Chân VCC  --> Nối vào chân 3V3 của ESP32',
        '• Chân GND  --> Nối vào chân GND của ESP32',
    ]),
    ('2. CẢM BIẾN SIÊU ÂM DÒ VẬT CẢN (HC-SR04)', [
        '• Chân TRIG --> Nối vào GPIO 16 của ESP32',
        '• Chân ECHO --> Nối vào GPIO 17 của ESP32 (Lưu ý: qua cầu trở 1k/2k để bảo vệ chip)',
        '• Chân VCC  --> Nối vào nguồn 5V (VIN)',
        '• Chân GND  --> Nối vào GND chung',
    ]),
    ('3. CÒI BÁO ĐỘNG (ACTIVE / PASSIVE BUZZER)', [
        '• Chân I/O (Tín hiệu) --> Nối vào GPIO 4 của ESP32',
        '• Chân VCC            --> Nối nguồn 5V (để âm lượng to và vang nhất)',
        '• Chân GND            --> Nối vào GND chung',
        '• Cơ chế hoạt động: Kích mức CAO + Phát xung tần số 2000Hz (Active HIGH + tone(4, 2000): HIGH = Hú, LOW = Im lặng). Sau khi ngã 30 giây nếu người già không bấm tắt thì còi sẽ tự động hú liên tục.',
    ]),
    ('4. MẠCH KÍCH MOTOR RUNG (MODULE MOSFET 075N03L)', [
        '• Chân TRIG / PWM     --> Nối vào GPIO 6 của ESP32 (VIBRATOR_PIN)',
        '• Chân GND (cạnh TRIG)--> Nối vào GND của ESP32',
        '• Cọc Domino VIN (+)  --> Nối vào nguồn 5V (VIN)',
        '• Cọc Domino GND (-)  --> Nối vào GND chung',
        '• Cọc Domino ngõ ra (OUT+/OUT-): Đã vặn sẵn 2 dây ra cục rung tròn (giữ nguyên).',
        '• Cơ chế hoạt động: Khi vật cản trong cự ly 3cm - 80cm, ESP32 xuất HIGH ra GPIO 6 kích motor rung báo hiệu.',
    ]),
    ('5. MẠCH NGUỒN & SẠC PIN (MODULE MH-CD42 TÍCH HỢP 2-TRONG-1)', [
        '• Chân ngõ ra VO (5V OUT) --> Nối thẳng vào chân 5V (VIN) của ESP32 (dây trắng trong ảnh)',
        '• Chân ngõ ra GND         --> Nối vào chân GND của ESP32 (dây đen cạnh dây trắng)',
        '• Hai chân nguồn Pin      --> Nối trực tiếp vào 2 cực (+) và (-) của viên Pin 18650',
        '• Cổng sạc Type-C         --> Cắm sạc 5V ngoài khi hết pin (4 đèn LED đỏ hiển thị mức sạc: 25% - 50% - 75% - 100%)',
    ]),
    ('6. NÚT BẤM HỦY BÁO NGÃ & TẮT CÒI (NÚT BOOT)', [
        '• Chân nút 1 --> Nối vào GPIO 0 của ESP32 (hoặc dùng nút BOOT có sẵn trên bo)',
        '• Chân nút 2 --> Nối vào GND chung',
        '• Cơ chế hoạt động: Cấu hình INPUT_PULLUP, khi đang đếm lùi 30s hoặc còi đang hú, nhấn nút này sẽ tắt còi và hủy sự cố ngã ngay tức thì.',
    ]),
    ('7. CẦU PHÂN ÁP ĐO DUNG LƯỢNG PIN 18650 (BÁO % PIN LÊN APP)', [
        '• Điểm giữa 2 điện trở R1 và R2 --> Nối thẳng vào chân GPIO 5 của ESP32 (ADC1_CH4)',
        '• Đầu trên điện trở R1 (100kΩ)  --> Nối thẳng vào Cực dương (+) của Pin 18650 (chân BAT+/VIN trên CD42)',
        '• Đầu dưới điện trở R2 (100kΩ)  --> Nối vào GND chung',
        '• Tụ lọc gốm 100nF (104)        --> Mắc song song với R2 (1 chân nối GPIO 5, 1 chân nối GND) để triệt tiêu nhiễu ADC',
        '• Cơ chế an toàn 100%: Pin sạc đầy 4.2V qua cầu chia đôi còn 2.1V vào GPIO 5 (hoàn toàn an toàn cho ESP32). Trong code: Vpin = Vadc * 2.',
    ]),
    ('8. NÚT BẤM KHẨN CẤP SOS TRÊN TAY CẦM (BẤM TAY GỌI CỨU HỘ)', [
        '• Chân nút 1 --> Nối vào chân GPIO 7 của ESP32 (SOS_BUTTON_PIN)',
        '• Chân nút 2 --> Nối vào chân GND của ESP32',
        '• Cơ chế hoạt động: Cấu hình INPUT_PULLUP trong code (không cần trở ngoài). Khi người già cảm thấy chóng mặt, mệt tim và nhấn nút SOS này, ESP32 lập tức bắn tín hiệu khẩn cấp lên App điện thoại để định vị GPS, gửi SMS cứu hộ và đếm lùi 30s hú còi.',
    ]),
    ('9. ĐÈN PIN LED RỌI ĐƯỜNG BAN ĐÊM (FLASHLIGHT)', [
        '• Chân Dương (+) Anode của bóng LED --> Nối qua điện trở hạn dòng R = 220Ω (hoặc 330Ω) --> Vào chân GPIO 18 của ESP32',
        '• Chân Âm (-) Cathode của bóng LED  --> Nối vào chân GND của ESP32',
        '• Cơ chế hoạt động: Chân GPIO 18 xuất mức HIGH (3.3V) cấp dòng ~10mA qua trở 220Ω giúp bóng LED siêu sáng 5mm phát sáng ổn định, hỗ trợ người già đi lại ban đêm.',
    ]),
]

for sec_title, sec_bullets in sections_data:
    p_st = doc.add_paragraph()
    r_st = p_st.add_run(sec_title)
    r_st.font.name = 'Arial'
    r_st.font.size = Pt(10.5)
    r_st.font.bold = True
    r_st.font.color.rgb = RGBColor(15, 23, 42)
    p_st.paragraph_format.space_before = Pt(6)
    p_st.paragraph_format.space_after = Pt(2)
    
    for b in sec_bullets:
        p_b = doc.add_paragraph()
        r_b = p_b.add_run(b)
        r_b.font.name = 'Arial'
        r_b.font.size = Pt(9.5)
        r_b.font.color.rgb = RGBColor(51, 65, 85)
        p_b.paragraph_format.left_indent = Inches(0.2)
        p_b.paragraph_format.space_before = Pt(1)
        p_b.paragraph_format.space_after = Pt(1)

# Lưu cả 2 định dạng: so_do_chan.docx và so_do_chan.doc
doc.save(r'd:\doan\so_do_chan.docx')
doc.save(r'd:\doan\so_do_chan.doc')
print('Cập nhật thành công d:\\doan\\so_do_chan.doc và d:\\doan\\so_do_chan.docx!')
