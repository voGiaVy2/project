import os
import sys
import uuid
import json
import zipfile
import subprocess

if sys.stdout:
    sys.stdout.reconfigure(encoding='utf-8')
if sys.stderr:
    sys.stderr.reconfigure(encoding='utf-8')

PROJECT_DIR = r"d:\doan\SmartCane_PCB"
os.makedirs(PROJECT_DIR, exist_ok=True)

# 1. Generate SmartCane_PCB.kicad_pro
pro_data = {
    "board": {
        "design_settings": {
            "defaults": {
                "board_outline_line_width": 0.25,
                "copper_line_width": 0.8,
                "copper_text_size_h": 1.5,
                "copper_text_size_v": 1.5
            }
        }
    },
    "meta": {
        "filename": "SmartCane_PCB.kicad_pro",
        "version": 1
    },
    "schematic": {
        "annotate_start_num": 1,
        "drawing": {
            "default_line_thickness": 0.1524,
            "default_text_size": 1.27
        }
    },
    "sheets": [
        [
            "11111111-2222-3333-4444-555555555555",
            ""
        ]
    ]
}

pro_path = os.path.join(PROJECT_DIR, "SmartCane_PCB.kicad_pro")
with open(pro_path, "w", encoding="utf-8") as f:
    json.dump(pro_data, f, indent=2)
print("Saved SmartCane_PCB.kicad_pro")

# 2. Build SmartCane_PCB.kicad_sch
def make_uuid():
    return str(uuid.uuid4())

sch_lines = []
sch_lines.append('(kicad_sch')
sch_lines.append('\t(version 20250610)')
sch_lines.append('\t(generator "eeschema")')
sch_lines.append('\t(generator_version "10.0")')
sch_lines.append('\t(uuid "11111111-2222-3333-4444-555555555555")')
sch_lines.append('\t(paper "A3")')
sch_lines.append('\t(title_block')
sch_lines.append('\t\t(title "HE THONG GAY THONG MINH HO TRO NGUOI KHIEM THI")')
sch_lines.append('\t\t(date "2026-10-25")')
sch_lines.append('\t\t(rev "1.0")')
sch_lines.append('\t\t(company "DO AN TOT NGHIEP")')
sch_lines.append('\t\t(comment 1 "Mach Carrier Board 1 Lop (Single-sided B.Cu) cho ESP32-S3")')
sch_lines.append('\t)')

# Helper to add simple symbol instance
# KiCad 10 schematic symbol structure
def add_symbol_instance(ref, val, pos_xy, fp_name="", unit=1):
    u = make_uuid()
    x, y = pos_xy
    sym_str = f'''\t(symbol
\t\t(lib_id "Device:R")
\t\t(at {x} {y} 0)
\t\t(unit {unit})
\t\t(exclude_from_sim no)
\t\t(in_bom yes)
\t\t(on_board yes)
\t\t(dnp no)
\t\t(uuid "{u}")
\t\t(property "Reference" "{ref}"
\t\t\t(at {x} {y - 2.54} 0)
\t\t\t(effects
\t\t\t\t(font (size 1.27 1.27))
\t\t\t)
\t\t)
\t\t(property "Value" "{val}"
\t\t\t(at {x} {y + 2.54} 0)
\t\t\t(effects
\t\t\t\t(font (size 1.27 1.27))
\t\t\t)
\t\t)
\t\t(property "Footprint" "{fp_name}"
\t\t\t(at {x} {y} 0)
\t\t\t(effects
\t\t\t\t(font (size 1.27 1.27))
\t\t\t\t(hide yes)
\t\t\t)
\t\t)
\t)'''
    return sym_str

# Text labels on schematic
def add_sch_text(text_str, pos_xy, size=2.0):
    u = make_uuid()
    x, y = pos_xy
    return f'''\t(text "{text_str}"
\t\t(exclude_from_sim no)
\t\t(at {x} {y} 0)
\t\t(effects
\t\t\t(font
\t\t\t\t(size {size} {size})
\t\t\t\t(bold yes)
\t\t\t)
\t\t\t(justify left bottom)
\t\t)
\t\t(uuid "{u}")
\t)'''

# Net label on schematic
def add_sch_label(name, pos_xy):
    u = make_uuid()
    x, y = pos_xy
    return f'''\t(label "{name}"
\t\t(at {x} {y} 0)
\t\t(fields_autoplaced yes)
\t\t(effects
\t\t\t(font
\t\t\t\t(size 1.27 1.27)
\t\t\t)
\t\t\t(justify left)
\t\t)
\t\t(uuid "{u}")
\t)'''

def add_sch_wire(pt1, pt2):
    u = make_uuid()
    return f'''\t(wire
\t\t(pts
\t\t\t(xy {pt1[0]} {pt1[1]}) (xy {pt2[0]} {pt2[1]})
\t\t)
\t\t(stroke
\t\t\t(width 0)
\t\t\t(type solid)
\t\t)
\t\t(uuid "{u}")
\t)'''

# Build functional schematic blocks
# 1. Title Block & Block labels
sch_lines.append(add_sch_text("KHOI NGUON (POWER SUPPLY): PIN 18650 -> TP4056 -> CONG TAC -> BOOST 5V", (30, 30), size=2.5))
sch_lines.append(add_sch_text("KHOI CAM BIEN (SENSORS): MPU6050, HC-SR04, E18-D50NK", (180, 30), size=2.5))
sch_lines.append(add_sch_text("KHOI CANH BAO & DIEU KHIEN: ESP32-S3, BUZZER, MOTOR RUNG MOSFET, SOS, LED", (30, 110), size=2.5))

# Power labels & wires
sch_lines.append(add_sch_label("VBAT (+3.7V)", (30, 45)))
sch_lines.append(add_sch_wire((30, 45), (60, 45)))
sch_lines.append(add_sch_label("GND", (30, 55)))
sch_lines.append(add_sch_wire((30, 55), (60, 55)))

sch_lines.append(add_sch_label("VCC_5V (+5.0V BOOST)", (80, 45)))
sch_lines.append(add_sch_wire((80, 45), (130, 45)))

sch_lines.append(add_sch_label("VCC_3V3 (ESP32-S3 LDO)", (80, 55)))
sch_lines.append(add_sch_wire((80, 55), (130, 55)))

# Microcontroller pinout labels
esp_pins = [
    ("GPIO4 (ADC)", "DO DIEN AP PIN (R1=10k, R2=10k, C=100nF)"),
    ("GPIO5 (BUZZER)", "COI CHIP ACTIVE BUZZER 5V"),
    ("GPIO6 (VIB_PWM)", "MOTOR RUNG QUA MOSFET AOD4184 & DIODE 1N4007"),
    ("GPIO7 (SOS_BTN)", "NUT BAM KHAN CAP SOS (PULL-UP)"),
    ("GPIO15 (E18_IN)", "CAM BIEN HONG NGOAI E18-D50NK (VAT CAN TAM GAN)"),
    ("GPIO16 (TRIG)", "CAM BIEN SIEU AM HC-SR04 TRIGGER"),
    ("GPIO17 (ECHO)", "CAM BIEN SIEU AM HC-SR04 ECHO"),
    ("GPIO18 (LED_LIGHT)", "DEN LED ROI DUONG 5mm + R 220 OHM"),
    ("GPIO8 (I2C_SDA)", "GIAO TIEP I2C SDA CHO GY-521 MPU6050"),
    ("GPIO9 (I2C_SCL)", "GIAO TIEP I2C SCL CHO GY-521 MPU6050")
]

start_y = 125
for idx, (p_name, desc) in enumerate(esp_pins):
    y = start_y + idx * 10
    sch_lines.append(add_sch_label(p_name, (40, y)))
    sch_lines.append(add_sch_wire((40, y), (85, y)))
    sch_lines.append(add_sch_text(f"--> {desc}", (90, y), size=1.4))

# Close schematic
sch_lines.append('\t(sheet_instances')
sch_lines.append('\t\t(path "/"')
sch_lines.append('\t\t\t(page "1")')
sch_lines.append('\t\t)')
sch_lines.append('\t)')
sch_lines.append(')')

sch_path = os.path.join(PROJECT_DIR, "SmartCane_PCB.kicad_sch")
with open(sch_path, "w", encoding="utf-8") as f:
    f.write("\n".join(sch_lines))
print(f"Saved {sch_path}")

# 3. Export Schematic PDF
kicad_cli = r"C:\Program Files\KiCad\10.0\bin\kicad-cli.exe"
pdf_sch_out = os.path.join(PROJECT_DIR, "So_Do_Nguyen_Ly_Schematic.pdf")
cmd_sch = [
    kicad_cli, "sch", "export", "pdf",
    "-o", pdf_sch_out,
    sch_path
]
print("Exporting Schematic PDF...")
res = subprocess.run(cmd_sch, capture_output=True, text=True)
print("Schematic export output:", res.stdout, res.stderr)

# 4. Export Gerbers & Drill files
gerber_dir = os.path.join(PROJECT_DIR, "Gerber")
os.makedirs(gerber_dir, exist_ok=True)
pcb_path = os.path.join(PROJECT_DIR, "SmartCane_PCB.kicad_pcb")

print("Exporting Gerbers...")
cmd_gerber = [
    kicad_cli, "pcb", "export", "gerbers",
    "-o", gerber_dir,
    pcb_path
]
res_g = subprocess.run(cmd_gerber, capture_output=True, text=True)
print("Gerber output:", res_g.stdout, res_g.stderr)

print("Exporting Drills...")
cmd_drill = [
    kicad_cli, "pcb", "export", "drill",
    "-o", gerber_dir,
    pcb_path
]
res_d = subprocess.run(cmd_drill, capture_output=True, text=True)
print("Drill output:", res_d.stdout, res_d.stderr)

# 5. Zip Gerbers to Gerber_SmartCane.zip
zip_path = os.path.join(PROJECT_DIR, "Gerber_SmartCane.zip")
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(gerber_dir):
        for file in files:
            file_p = os.path.join(root, file)
            zipf.write(file_p, os.path.relpath(file_p, gerber_dir))
print(f"Generated Gerber zip: {zip_path}")
