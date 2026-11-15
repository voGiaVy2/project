import os
import sys
import zipfile
import subprocess
import pcbnew

if sys.stdout:
    sys.stdout.reconfigure(encoding='utf-8')
if sys.stderr:
    sys.stderr.reconfigure(encoding='utf-8')

def build_complete_safe_board():
    board = pcbnew.BOARD()
    
    # Board dimensions: 110 x 80 mm
    OX = 40.0
    OY = 40.0
    WIDTH = 110.0
    HEIGHT = 80.0
    
    b_cu = pcbnew.B_Cu
    f_cu = pcbnew.F_Cu
    f_silk = pcbnew.F_SilkS
    b_silk = pcbnew.B_SilkS
    edge_cuts = pcbnew.Edge_Cuts
    
    # 1. Edge cuts
    p0 = pcbnew.VECTOR2I(pcbnew.FromMM(OX), pcbnew.FromMM(OY))
    p1 = pcbnew.VECTOR2I(pcbnew.FromMM(OX + WIDTH), pcbnew.FromMM(OY))
    p2 = pcbnew.VECTOR2I(pcbnew.FromMM(OX + WIDTH), pcbnew.FromMM(OY + HEIGHT))
    p3 = pcbnew.VECTOR2I(pcbnew.FromMM(OX), pcbnew.FromMM(OY + HEIGHT))
    
    for s, e in [(p0, p1), (p1, p2), (p2, p3), (p3, p0)]:
        seg = pcbnew.PCB_SHAPE(board)
        seg.SetShape(pcbnew.SHAPE_T_SEGMENT)
        seg.SetStart(s)
        seg.SetEnd(e)
        seg.SetLayer(edge_cuts)
        seg.SetWidth(pcbnew.FromMM(0.25))
        board.Add(seg)
        
    # 2. 4 Mounting Holes M3
    for mx, my in [(4.5, 4.5), (WIDTH - 4.5, 4.5), (4.5, HEIGHT - 4.5), (WIDTH - 4.5, HEIGHT - 4.5)]:
        fp = pcbnew.FOOTPRINT(board)
        fp.SetReference("H")
        fp.SetValue("MountingHole_M3")
        fp.SetPosition(pcbnew.VECTOR2I(pcbnew.FromMM(OX + mx), pcbnew.FromMM(OY + my)))
        pad = pcbnew.PAD(fp)
        pad.SetNumber("1")
        pad.SetShape(pcbnew.PAD_SHAPE_CIRCLE)
        pad.SetSize(pcbnew.VECTOR2I(pcbnew.FromMM(6.0), pcbnew.FromMM(6.0)))
        pad.SetDrillSize(pcbnew.VECTOR2I(pcbnew.FromMM(3.2), pcbnew.FromMM(3.2)))
        pad.SetAttribute(pcbnew.PAD_ATTRIB_NPTH)
        pad.SetFPRelativePosition(pcbnew.VECTOR2I(0, 0))
        fp.Add(pad)
        board.Add(fp)

    # 3. Nets Definition
    nets = {}
    net_list = [
        "GND", "+5V", "+3V3", "VBAT", "V_SW", "ADC_BAT",
        "GPIO5_BUZ", "GPIO6_VIB", "GPIO7_SOS", "GPIO15_E18",
        "GPIO16_TRIG", "GPIO17_ECHO", "ECHO_5V", "GPIO18_LED",
        "I2C_SDA", "I2C_SCL", "MOTOR_DRAIN", "BUZ_DRIVE"
    ]
    for n in net_list:
        net_item = pcbnew.NETINFO_ITEM(board, n)
        board.Add(net_item)
        nets[n] = net_item

    # Pad helper
    def add_pad(fp, num, rx, ry, net_name=None, size=(2.4, 2.4), drill=1.0, shape=pcbnew.PAD_SHAPE_CIRCLE):
        pad = pcbnew.PAD(fp)
        pad.SetNumber(str(num))
        pad.SetFPRelativePosition(pcbnew.VECTOR2I(pcbnew.FromMM(rx), pcbnew.FromMM(ry)))
        pad.SetShape(shape)
        pad.SetSize(pcbnew.VECTOR2I(pcbnew.FromMM(size[0]), pcbnew.FromMM(size[1])))
        pad.SetDrillSize(pcbnew.VECTOR2I(pcbnew.FromMM(drill), pcbnew.FromMM(drill)))
        pad.SetAttribute(pcbnew.PAD_ATTRIB_PTH)
        if net_name and net_name in nets:
            pad.SetNet(nets[net_name])
        fp.Add(pad)
        return pad

    def add_silk_text(txt, pos, layer=f_silk, size=1.3):
        t = pcbnew.PCB_TEXT(board)
        t.SetText(txt)
        t.SetPosition(pcbnew.VECTOR2I(pcbnew.FromMM(pos[0]), pcbnew.FromMM(pos[1])))
        t.SetLayer(layer)
        t.SetTextSize(pcbnew.VECTOR2I(pcbnew.FromMM(size), pcbnew.FromMM(size)))
        t.SetTextThickness(pcbnew.FromMM(0.25))
        board.Add(t)

    def add_silk_line(p1, p2, layer=f_silk, width=0.2):
        seg = pcbnew.PCB_SHAPE(board)
        seg.SetShape(pcbnew.SHAPE_T_SEGMENT)
        seg.SetStart(pcbnew.VECTOR2I(pcbnew.FromMM(p1[0]), pcbnew.FromMM(p1[1])))
        seg.SetEnd(pcbnew.VECTOR2I(pcbnew.FromMM(p2[0]), p2_mm=pcbnew.FromMM(p2[1]))) if False else seg.SetEnd(pcbnew.VECTOR2I(pcbnew.FromMM(p2[0]), pcbnew.FromMM(p2[1])))
        seg.SetLayer(layer)
        seg.SetWidth(pcbnew.FromMM(width))
        board.Add(seg)

    def add_track_seg(p1, p2, net_name=None, layer=b_cu, width=0.85):
        net_item = nets.get(net_name, None)
        t = pcbnew.PCB_TRACK(board)
        t.SetStart(pcbnew.VECTOR2I(pcbnew.FromMM(p1[0]), pcbnew.FromMM(p1[1])))
        t.SetEnd(pcbnew.VECTOR2I(pcbnew.FromMM(p2[0]), pcbnew.FromMM(p2[1])))
        t.SetWidth(pcbnew.FromMM(width))
        t.SetLayer(layer)
        if net_item:
            t.SetNet(net_item)
        board.Add(t)

    def add_route(pts, net_name=None, layer=b_cu, width=0.85):
        for i in range(len(pts) - 1):
            add_track_seg(pts[i], pts[i+1], net_name=net_name, layer=layer, width=width)

    def add_via(pos, net_name=None, size=1.4, drill=0.7):
        net_item = nets.get(net_name, None)
        v = pcbnew.PCB_VIA(board)
        v.SetPosition(pcbnew.VECTOR2I(pcbnew.FromMM(pos[0]), pcbnew.FromMM(pos[1])))
        v.SetWidth(pcbnew.FromMM(size))
        v.SetDrill(pcbnew.FromMM(drill))
        v.SetTopLayer(f_cu)
        v.SetBottomLayer(b_cu)
        if net_item:
            v.SetNet(net_item)
        board.Add(v)

    # 4. ESP32-S3 DevKitC (2x 1x22 Pin Headers, row spacing 22.86mm / 900 mil)
    esp_lx = OX + 65.0
    esp_rx = esp_lx + 22.86
    esp_sy = OY + 14.0

    fp_el = pcbnew.FOOTPRINT(board)
    fp_el.SetReference("U1_L")
    fp_el.SetValue("ESP32-S3_L")
    fp_el.SetPosition(pcbnew.VECTOR2I(pcbnew.FromMM(esp_lx), pcbnew.FromMM(esp_sy)))

    fp_er = pcbnew.FOOTPRINT(board)
    fp_er.SetReference("U1_R")
    fp_er.SetValue("ESP32-S3_R")
    fp_er.SetPosition(pcbnew.VECTOR2I(pcbnew.FromMM(esp_rx), pcbnew.FromMM(esp_sy)))

    left_nets = {
        1: "+3V3", 2: "+3V3",
        4: "ADC_BAT", 5: "GPIO5_BUZ", 6: "GPIO6_VIB", 7: "GPIO7_SOS",
        8: "GPIO15_E18", 9: "GPIO16_TRIG", 10: "GPIO17_ECHO", 11: "GPIO18_LED",
        12: "I2C_SDA", 13: "I2C_SCL",
        22: "GND"
    }
    pins_l = {}
    for i in range(22):
        py = i * 2.54
        net_n = left_nets.get(i + 1, None)
        shape = pcbnew.PAD_SHAPE_RECT if i == 0 else pcbnew.PAD_SHAPE_CIRCLE
        add_pad(fp_el, i + 1, 0, py, net_name=net_n, shape=shape)
        pins_l[i + 1] = (esp_lx, esp_sy + py)

    right_nets = {23: "GND", 43: "+5V", 44: "+5V"}
    pins_r = {}
    for i in range(22):
        py = i * 2.54
        pnum = i + 23
        net_n = right_nets.get(pnum, None)
        add_pad(fp_er, pnum, 0, py, net_name=net_n)
        pins_r[pnum] = (esp_rx, esp_sy + py)

    board.Add(fp_el)
    board.Add(fp_er)

    # Outline silkscreen
    add_silk_line((esp_lx - 2.5, esp_sy - 3.0), (esp_rx + 2.5, esp_sy - 3.0))
    add_silk_line((esp_rx + 2.5, esp_sy - 3.0), (esp_rx + 2.5, esp_sy + 21 * 2.54 + 3.0))
    add_silk_line((esp_rx + 2.5, esp_sy + 21 * 2.54 + 3.0), (esp_lx - 2.5, esp_sy + 21 * 2.54 + 3.0))
    add_silk_line((esp_lx - 2.5, esp_sy + 21 * 2.54 + 3.0), (esp_lx - 2.5, esp_sy - 3.0))
    add_silk_text("ESP32-S3 DEVKITC N16R8", (esp_lx + 1.5, esp_sy + 27.0), size=1.5)

    # 5. Power Section (Left Side)
    # J_BATT KF301-2P (5.0mm pitch)
    fp_bat = pcbnew.FOOTPRINT(board)
    fp_bat.SetReference("J_BATT")
    fp_bat.SetValue("KF301 (PIN 18650)")
    fp_bat.SetPosition(pcbnew.VECTOR2I(pcbnew.FromMM(OX + 8.0), pcbnew.FromMM(OY + 12.0)))
    add_pad(fp_bat, 1, 0, 0, net_name="VBAT", size=(3.2, 3.2), drill=1.3, shape=pcbnew.PAD_SHAPE_RECT)
    add_pad(fp_bat, 2, 5.0, 0, net_name="GND", size=(3.2, 3.2), drill=1.3)
    board.Add(fp_bat)
    bat_loc = [(OX + 8.0, OY + 12.0), (OX + 13.0, OY + 12.0)]
    add_silk_text("+ BAT -", (OX + 8.0, OY + 8.0), size=1.2)

    # TP4056 Type-C Module (B+, B-, OUT+, OUT-)
    fp_tp = pcbnew.FOOTPRINT(board)
    fp_tp.SetReference("MOD_TP4056")
    fp_tp.SetValue("TP4056")
    fp_tp.SetPosition(pcbnew.VECTOR2I(pcbnew.FromMM(OX + 8.0), pcbnew.FromMM(OY + 20.0)))
    add_pad(fp_tp, 1, 0, 0, net_name="VBAT")
    add_pad(fp_tp, 2, 2.54, 0, net_name="GND")
    add_pad(fp_tp, 3, 5.08, 0, net_name="VBAT")
    add_pad(fp_tp, 4, 7.62, 0, net_name="GND")
    board.Add(fp_tp)
    tp_loc = [(OX + 8.0 + i*2.54, OY + 20.0) for i in range(4)]
    add_silk_text("TP4056", (OX + 8.0, OY + 16.5), size=1.1)

    # SPDT Power Switch
    fp_sw = pcbnew.FOOTPRINT(board)
    fp_sw.SetReference("SW_PWR")
    fp_sw.SetValue("SPDT ON/OFF")
    fp_sw.SetPosition(pcbnew.VECTOR2I(pcbnew.FromMM(OX + 8.0), pcbnew.FromMM(OY + 28.0)))
    add_pad(fp_sw, 1, 0, 0, net_name="VBAT")
    add_pad(fp_sw, 2, 2.54, 0, net_name="V_SW")
    add_pad(fp_sw, 3, 5.08, 0, net_name=None)
    board.Add(fp_sw)
    sw_loc = [(OX + 8.0 + i*2.54, OY + 28.0) for i in range(3)]
    add_silk_text("PWR SW", (OX + 8.0, OY + 25.0), size=1.1)

    # Mini Boost 5V
    fp_bst = pcbnew.FOOTPRINT(board)
    fp_bst.SetReference("MOD_BOOST")
    fp_bst.SetValue("Boost 5V")
    fp_bst.SetPosition(pcbnew.VECTOR2I(pcbnew.FromMM(OX + 8.0), pcbnew.FromMM(OY + 36.0)))
    add_pad(fp_bst, 1, 0, 0, net_name="V_SW")
    add_pad(fp_bst, 2, 2.54, 0, net_name="GND")
    add_pad(fp_bst, 3, 5.08, 0, net_name="+5V")
    add_pad(fp_bst, 4, 7.62, 0, net_name="GND")
    board.Add(fp_bst)
    bst_loc = [(OX + 8.0 + i*2.54, OY + 36.0) for i in range(4)]
    add_silk_text("BOOST 5V", (OX + 8.0, OY + 33.0), size=1.1)

    # 6. Battery ADC Divider (R1, R2, C_DIV)
    fp_r1 = pcbnew.FOOTPRINT(board)
    fp_r1.SetReference("R_DIV1")
    fp_r1.SetValue("10k")
    fp_r1.SetPosition(pcbnew.VECTOR2I(pcbnew.FromMM(OX + 24.0), pcbnew.FromMM(OY + 14.0)))
    add_pad(fp_r1, 1, 0, 0, net_name="VBAT")
    add_pad(fp_r1, 2, 0, 7.62, net_name="ADC_BAT")
    board.Add(fp_r1)
    r1_loc = [(OX + 24.0, OY + 14.0), (OX + 24.0, OY + 21.62)]

    fp_r2 = pcbnew.FOOTPRINT(board)
    fp_r2.SetReference("R_DIV2")
    fp_r2.SetValue("10k")
    fp_r2.SetPosition(pcbnew.VECTOR2I(pcbnew.FromMM(OX + 28.0), pcbnew.FromMM(OY + 14.0)))
    add_pad(fp_r2, 1, 0, 0, net_name="ADC_BAT")
    add_pad(fp_r2, 2, 0, 7.62, net_name="GND")
    board.Add(fp_r2)
    r2_loc = [(OX + 28.0, OY + 14.0), (OX + 28.0, OY + 21.62)]

    fp_cdiv = pcbnew.FOOTPRINT(board)
    fp_cdiv.SetReference("C_DIV")
    fp_cdiv.SetValue("100nF")
    fp_cdiv.SetPosition(pcbnew.VECTOR2I(pcbnew.FromMM(OX + 32.0), pcbnew.FromMM(OY + 14.0)))
    add_pad(fp_cdiv, 1, 0, 0, net_name="ADC_BAT")
    add_pad(fp_cdiv, 2, 0, 5.08, net_name="GND")
    board.Add(fp_cdiv)
    cdiv_loc = [(OX + 32.0, OY + 14.0), (OX + 32.0, OY + 19.08)]
    add_silk_text("R1/R2/C BAT", (OX + 23.0, OY + 10.5), size=1.0)

    # 7. Buzzer Active 5V + Transistor Driver Q2 (NPN S8050)
    fp_bz = pcbnew.FOOTPRINT(board)
    fp_bz.SetReference("BZ1")
    fp_bz.SetValue("Active Buzzer")
    fp_bz.SetPosition(pcbnew.VECTOR2I(pcbnew.FromMM(OX + 24.0), pcbnew.FromMM(OY + 28.0)))
    add_pad(fp_bz, 1, 0, 0, net_name="+5V", size=(2.8, 2.8), drill=1.1)
    add_pad(fp_bz, 2, 7.62, 0, net_name="BUZ_DRIVE", size=(2.8, 2.8), drill=1.1)
    board.Add(fp_bz)
    bz_loc = [(OX + 24.0, OY + 28.0), (OX + 31.62, OY + 28.0)]
    add_silk_text("+ BUZZER -", (OX + 24.0, OY + 25.0), size=1.1)

    fp_q2 = pcbnew.FOOTPRINT(board)
    fp_q2.SetReference("Q2")
    fp_q2.SetValue("S8050")
    fp_q2.SetPosition(pcbnew.VECTOR2I(pcbnew.FromMM(OX + 38.0), pcbnew.FromMM(OY + 26.0)))
    add_pad(fp_q2, 1, 0, 0, net_name="GND")
    add_pad(fp_q2, 2, 2.54, 0, net_name="GPIO5_BUZ")
    add_pad(fp_q2, 3, 5.08, 0, net_name="BUZ_DRIVE")
    board.Add(fp_q2)
    q2_loc = [(OX + 38.0 + i*2.54, OY + 26.0) for i in range(3)]
    add_silk_text("Q2 S8050", (OX + 38.0, OY + 23.5), size=1.0)

    # 8. Vibration Motor MOSFET Q1 (AOD4184) + Flyback Diode 1N4007 + Resistors
    fp_q1 = pcbnew.FOOTPRINT(board)
    fp_q1.SetReference("Q1")
    fp_q1.SetValue("AOD4184")
    fp_q1.SetPosition(pcbnew.VECTOR2I(pcbnew.FromMM(OX + 24.0), pcbnew.FromMM(OY + 38.0)))
    add_pad(fp_q1, 1, 0, 0, net_name="GPIO6_VIB")
    add_pad(fp_q1, 2, 2.54, 0, net_name="MOTOR_DRAIN")
    add_pad(fp_q1, 3, 5.08, 0, net_name="GND")
    board.Add(fp_q1)
    q1_loc = [(OX + 24.0 + i*2.54, OY + 38.0) for i in range(3)]
    add_silk_text("Q1 (G D S)", (OX + 24.0, OY + 35.0), size=1.0)

    fp_rg = pcbnew.FOOTPRINT(board)
    fp_rg.SetReference("R_GATE")
    fp_rg.SetValue("1k")
    fp_rg.SetPosition(pcbnew.VECTOR2I(pcbnew.FromMM(OX + 34.0), pcbnew.FromMM(OY + 36.0)))
    add_pad(fp_rg, 1, 0, 0, net_name="GPIO6_VIB")
    add_pad(fp_rg, 2, 0, 7.62, net_name="GPIO6_VIB")
    board.Add(fp_rg)
    rg_loc = [(OX + 34.0, OY + 36.0), (OX + 34.0, OY + 43.62)]

    fp_rpd = pcbnew.FOOTPRINT(board)
    fp_rpd.SetReference("R_PD")
    fp_rpd.SetValue("10k")
    fp_rpd.SetPosition(pcbnew.VECTOR2I(pcbnew.FromMM(OX + 38.0), pcbnew.FromMM(OY + 36.0)))
    add_pad(fp_rpd, 1, 0, 0, net_name="GPIO6_VIB")
    add_pad(fp_rpd, 2, 0, 7.62, net_name="GND")
    board.Add(fp_rpd)
    rpd_loc = [(OX + 38.0, OY + 36.0), (OX + 38.0, OY + 43.62)]

    fp_d1 = pcbnew.FOOTPRINT(board)
    fp_d1.SetReference("D1")
    fp_d1.SetValue("1N4007")
    fp_d1.SetPosition(pcbnew.VECTOR2I(pcbnew.FromMM(OX + 44.0), pcbnew.FromMM(OY + 36.0)))
    add_pad(fp_d1, 1, 0, 0, net_name="+5V")
    add_pad(fp_d1, 2, 0, 7.62, net_name="MOTOR_DRAIN")
    board.Add(fp_d1)
    d1_loc = [(OX + 44.0, OY + 36.0), (OX + 44.0, OY + 43.62)]
    add_silk_text("D1 1N4007", (OX + 44.0, OY + 33.5), size=1.0)

    fp_jmot = pcbnew.FOOTPRINT(board)
    fp_jmot.SetReference("J_MOTOR")
    fp_jmot.SetValue("Motor Rung")
    fp_jmot.SetPosition(pcbnew.VECTOR2I(pcbnew.FromMM(OX + 8.0), pcbnew.FromMM(OY + 46.0)))
    add_pad(fp_jmot, 1, 0, 0, net_name="+5V")
    add_pad(fp_jmot, 2, 2.54, 0, net_name="MOTOR_DRAIN")
    board.Add(fp_jmot)
    jmot_loc = [(OX + 8.0, OY + 46.0), (OX + 10.54, OY + 46.0)]
    add_silk_text("MOTOR (+ -)", (OX + 8.0, OY + 43.5), size=1.0)

    # 9. Sensors & Peripheral Headers (Lower Left & Bottom)
    # J_MPU6050 (1=+3V3, 2=GND, 3=SCL, 4=SDA)
    fp_mpu = pcbnew.FOOTPRINT(board)
    fp_mpu.SetReference("J_MPU6050")
    fp_mpu.SetValue("GY-521")
    fp_mpu.SetPosition(pcbnew.VECTOR2I(pcbnew.FromMM(OX + 8.0), pcbnew.FromMM(OY + 54.0)))
    add_pad(fp_mpu, 1, 0, 0, net_name="+3V3")
    add_pad(fp_mpu, 2, 2.54, 0, net_name="GND")
    add_pad(fp_mpu, 3, 5.08, 0, net_name="I2C_SCL")
    add_pad(fp_mpu, 4, 7.62, 0, net_name="I2C_SDA")
    board.Add(fp_mpu)
    mpu_loc = [(OX + 8.0 + i*2.54, OY + 54.0) for i in range(4)]
    add_silk_text("MPU6050", (OX + 8.0, OY + 51.5), size=1.1)

    # J_HCSR04 (1=+5V, 2=Trig, 3=ECHO_5V, 4=GND)
    fp_hc = pcbnew.FOOTPRINT(board)
    fp_hc.SetReference("J_HCSR04")
    fp_hc.SetValue("HC-SR04")
    fp_hc.SetPosition(pcbnew.VECTOR2I(pcbnew.FromMM(OX + 8.0), pcbnew.FromMM(OY + 62.0)))
    add_pad(fp_hc, 1, 0, 0, net_name="+5V")
    add_pad(fp_hc, 2, 2.54, 0, net_name="GPIO16_TRIG")
    add_pad(fp_hc, 3, 5.08, 0, net_name="ECHO_5V")
    add_pad(fp_hc, 4, 7.62, 0, net_name="GND")
    board.Add(fp_hc)
    hc_loc = [(OX + 8.0 + i*2.54, OY + 62.0) for i in range(4)]
    add_silk_text("HC-SR04", (OX + 8.0, OY + 59.5), size=1.1)

    # Echo divider: R_EC1 (1k) + R_EC2 (2k)
    fp_rec1 = pcbnew.FOOTPRINT(board)
    fp_rec1.SetReference("R_EC1")
    fp_rec1.SetValue("1k")
    fp_rec1.SetPosition(pcbnew.VECTOR2I(pcbnew.FromMM(OX + 24.0), pcbnew.FromMM(OY + 60.0)))
    add_pad(fp_rec1, 1, 0, 0, net_name="ECHO_5V")
    add_pad(fp_rec1, 2, 0, 7.62, net_name="GPIO17_ECHO")
    board.Add(fp_rec1)
    rec1_loc = [(OX + 24.0, OY + 60.0), (OX + 24.0, OY + 67.62)]

    fp_rec2 = pcbnew.FOOTPRINT(board)
    fp_rec2.SetReference("R_EC2")
    fp_rec2.SetValue("2k")
    fp_rec2.SetPosition(pcbnew.VECTOR2I(pcbnew.FromMM(OX + 28.0), pcbnew.FromMM(OY + 60.0)))
    add_pad(fp_rec2, 1, 0, 0, net_name="GPIO17_ECHO")
    add_pad(fp_rec2, 2, 0, 7.62, net_name="GND")
    board.Add(fp_rec2)
    rec2_loc = [(OX + 28.0, OY + 60.0), (OX + 28.0, OY + 67.62)]
    add_silk_text("ECHO DIV", (OX + 23.0, OY + 57.5), size=1.0)

    # J_E18 (1=+5V, 2=GND, 3=GPIO15_E18)
    fp_e18 = pcbnew.FOOTPRINT(board)
    fp_e18.SetReference("J_E18")
    fp_e18.SetValue("E18-D50NK")
    fp_e18.SetPosition(pcbnew.VECTOR2I(pcbnew.FromMM(OX + 8.0), pcbnew.FromMM(OY + 72.0)))
    add_pad(fp_e18, 1, 0, 0, net_name="+5V")
    add_pad(fp_e18, 2, 2.54, 0, net_name="GND")
    add_pad(fp_e18, 3, 5.08, 0, net_name="GPIO15_E18")
    board.Add(fp_e18)
    e18_loc = [(OX + 8.0 + i*2.54, OY + 72.0) for i in range(3)]
    add_silk_text("E18 SENSOR", (OX + 8.0, OY + 69.5), size=1.1)

    # R_E18 (10k pull-up to 3.3V)
    fp_re18 = pcbnew.FOOTPRINT(board)
    fp_re18.SetReference("R_E18")
    fp_re18.SetValue("10k")
    fp_re18.SetPosition(pcbnew.VECTOR2I(pcbnew.FromMM(OX + 24.0), pcbnew.FromMM(OY + 72.0)))
    add_pad(fp_re18, 1, 0, 0, net_name="+3V3")
    add_pad(fp_re18, 2, 5.08, 0, net_name="GPIO15_E18")
    board.Add(fp_re18)
    re18_loc = [(OX + 24.0, OY + 72.0), (OX + 29.08, OY + 72.0)]

    # SW_SOS
    fp_sos = pcbnew.FOOTPRINT(board)
    fp_sos.SetReference("SW_SOS")
    fp_sos.SetValue("SOS Button")
    fp_sos.SetPosition(pcbnew.VECTOR2I(pcbnew.FromMM(OX + 36.0), pcbnew.FromMM(OY + 54.0)))
    add_pad(fp_sos, 1, 0, 0, net_name="GPIO7_SOS")
    add_pad(fp_sos, 2, 2.54, 0, net_name="GND")
    board.Add(fp_sos)
    sos_loc = [(OX + 36.0, OY + 54.0), (OX + 38.54, OY + 54.0)]
    add_silk_text("SOS BTN", (OX + 36.0, OY + 51.5), size=1.1)

    # LED1 + R_LED (220R)
    fp_led = pcbnew.FOOTPRINT(board)
    fp_led.SetReference("LED1")
    fp_led.SetValue("LED 5mm")
    fp_led.SetPosition(pcbnew.VECTOR2I(pcbnew.FromMM(OX + 36.0), pcbnew.FromMM(OY + 64.0)))
    add_pad(fp_led, 1, 0, 0, net_name="GPIO18_LED")
    add_pad(fp_led, 2, 2.54, 0, net_name="GND")
    board.Add(fp_led)
    led_loc = [(OX + 36.0, OY + 64.0), (OX + 38.54, OY + 64.0)]

    fp_rled = pcbnew.FOOTPRINT(board)
    fp_rled.SetReference("R_LED")
    fp_rled.SetValue("220R")
    fp_rled.SetPosition(pcbnew.VECTOR2I(pcbnew.FromMM(OX + 44.0), pcbnew.FromMM(OY + 64.0)))
    add_pad(fp_rled, 1, 0, 0, net_name="GPIO18_LED")
    add_pad(fp_rled, 2, 5.08, 0, net_name="GPIO18_LED")
    board.Add(fp_rled)
    rled_loc = [(OX + 44.0, OY + 64.0), (OX + 49.08, OY + 64.0)]
    add_silk_text("LED + 220R", (OX + 36.0, OY + 61.5), size=1.0)

    # 10. CLEAN DUAL-LAYER ROUTING (No short circuits, wide tracks for DIY & factory)
    W_PWR = 1.3
    W_SIG = 0.85
    W_GND = 1.5

    # Power:
    add_route([bat_loc[0], tp_loc[0]], net_name="VBAT", layer=b_cu, width=W_PWR)
    add_route([tp_loc[2], sw_loc[0]], net_name="VBAT", layer=b_cu, width=W_PWR)
    add_route([tp_loc[2], r1_loc[0]], net_name="VBAT", layer=b_cu, width=W_SIG)

    add_route([sw_loc[1], bst_loc[0]], net_name="V_SW", layer=b_cu, width=W_PWR)

    # 5V distribution (Boost OUT+ -> Buzzer, Diode D1, Motor, HC-SR04, E18, ESP32 VIN)
    add_route([bst_loc[2], (OX + 18.0, bst_loc[2][1]), (OX + 18.0, bz_loc[0][1]), bz_loc[0]], net_name="+5V", layer=b_cu, width=W_PWR)
    add_route([bz_loc[0], (OX + 18.0, bz_loc[0][1]), (OX + 18.0, d1_loc[0][1]), d1_loc[0]], net_name="+5V", layer=b_cu, width=W_PWR)
    add_route([d1_loc[0], (OX + 18.0, d1_loc[0][1]), (OX + 18.0, jmot_loc[0][1]), jmot_loc[0]], net_name="+5V", layer=b_cu, width=W_PWR)
    add_route([jmot_loc[0], (OX + 4.0, jmot_loc[0][1]), (OX + 4.0, hc_loc[0][1]), hc_loc[0]], net_name="+5V", layer=b_cu, width=W_PWR)
    add_route([hc_loc[0], (OX + 4.0, hc_loc[0][1]), (OX + 4.0, e18_loc[0][1]), e18_loc[0]], net_name="+5V", layer=b_cu, width=W_PWR)
    # 5V to ESP32 Right Header Pin 43 & 44 (via Top Copper F.Cu bridge)
    add_route([bz_loc[0], (bz_loc[0][0], OY + 6.0), (esp_rx + 5.0, OY + 6.0), (esp_rx + 5.0, pins_r[44][1]), pins_r[44]], net_name="+5V", layer=f_cu, width=W_PWR)
    add_route([pins_r[44], pins_r[43]], net_name="+5V", layer=b_cu, width=W_PWR)

    # 3.3V (ESP32 Pin 1 -> MPU6050 & R_E18 via F.Cu bridge)
    add_route([pins_l[1], (pins_l[1][0] - 6.0, pins_l[1][1]), (pins_l[1][0] - 6.0, OY + 50.0), (OX + 20.0, OY + 50.0), (OX + 20.0, mpu_loc[0][1]), mpu_loc[0]], net_name="+3V3", layer=f_cu, width=1.0)
    add_route([mpu_loc[0], (OX + 20.0, mpu_loc[0][1]), (OX + 20.0, re18_loc[0][1]), re18_loc[0]], net_name="+3V3", layer=b_cu, width=W_SIG)

    # ADC_BAT: R1 pin 2 -> R2 pin 1 -> C_DIV pin 1 -> ESP32 Pin 4
    add_route([r1_loc[1], r2_loc[0]], net_name="ADC_BAT", layer=b_cu, width=W_SIG)
    add_route([r2_loc[0], cdiv_loc[0]], net_name="ADC_BAT", layer=b_cu, width=W_SIG)
    add_route([cdiv_loc[0], (cdiv_loc[0][0], pins_l[4][1]), pins_l[4]], net_name="ADC_BAT", layer=b_cu, width=W_SIG)

    # GPIO5_BUZ: ESP32 Pin 5 -> Q2 Base
    add_route([pins_l[5], (q2_loc[1][0], pins_l[5][1]), q2_loc[1]], net_name="GPIO5_BUZ", layer=b_cu, width=W_SIG)
    add_route([q2_loc[2], (q2_loc[2][0], bz_loc[1][1]), bz_loc[1]], net_name="BUZ_DRIVE", layer=b_cu, width=W_SIG)

    # GPIO6_VIB: ESP32 Pin 6 -> R_GATE -> Q1 Gate
    add_route([pins_l[6], (rg_loc[0][0], pins_l[6][1]), rg_loc[0]], net_name="GPIO6_VIB", layer=b_cu, width=W_SIG)
    add_route([rg_loc[1], q1_loc[0]], net_name="GPIO6_VIB", layer=b_cu, width=W_SIG)
    add_route([q1_loc[0], rpd_loc[0]], net_name="GPIO6_VIB", layer=b_cu, width=W_SIG)
    # MOTOR_DRAIN: Q1 Drain -> D1 Anode & J_MOTOR (-)
    add_route([q1_loc[1], (q1_loc[1][0], d1_loc[1][1]), d1_loc[1]], net_name="MOTOR_DRAIN", layer=b_cu, width=W_PWR)
    add_route([q1_loc[1], (q1_loc[1][0], jmot_loc[1][1]), jmot_loc[1]], net_name="MOTOR_DRAIN", layer=b_cu, width=W_PWR)

    # GPIO7_SOS: ESP32 Pin 7 -> SW_SOS (F.Cu bridge)
    add_route([pins_l[7], (pins_l[7][0] - 10.0, pins_l[7][1]), (pins_l[7][0] - 10.0, sos_loc[0][1]), sos_loc[0]], net_name="GPIO7_SOS", layer=f_cu, width=W_SIG)

    # GPIO15_E18: ESP32 Pin 8 -> E18 Pin 3 & R_E18 (F.Cu bridge)
    add_route([pins_l[8], (pins_l[8][0] - 12.0, pins_l[8][1]), (pins_l[8][0] - 12.0, e18_loc[2][1]), e18_loc[2]], net_name="GPIO15_E18", layer=f_cu, width=W_SIG)
    add_route([e18_loc[2], re18_loc[1]], net_name="GPIO15_E18", layer=b_cu, width=W_SIG)

    # GPIO16_TRIG: ESP32 Pin 9 -> HC-SR04 Trig (F.Cu bridge)
    add_route([pins_l[9], (pins_l[9][0] - 14.0, pins_l[9][1]), (pins_l[9][0] - 14.0, hc_loc[1][1]), hc_loc[1]], net_name="GPIO16_TRIG", layer=f_cu, width=W_SIG)

    # ECHO_5V & GPIO17_ECHO: HC-SR04 Echo 5V -> R_EC1 1k -> GPIO17_ECHO 3.3V -> ESP32 Pin 10
    add_route([hc_loc[2], rec1_loc[0]], net_name="ECHO_5V", layer=b_cu, width=W_SIG)
    add_route([rec1_loc[1], rec2_loc[0]], net_name="GPIO17_ECHO", layer=b_cu, width=W_SIG)
    add_route([rec1_loc[1], (rec1_loc[1][0], pins_l[10][1]), pins_l[10]], net_name="GPIO17_ECHO", layer=b_cu, width=W_SIG)

    # GPIO18_LED: ESP32 Pin 11 -> R_LED -> LED1
    add_route([pins_l[11], (rled_loc[1][0], pins_l[11][1]), rled_loc[1]], net_name="GPIO18_LED", layer=b_cu, width=W_SIG)
    add_route([rled_loc[0], led_loc[0]], net_name="GPIO18_LED", layer=b_cu, width=W_SIG)

    # I2C: GPIO8 -> SDA, GPIO9 -> SCL (F.Cu bridge)
    add_route([pins_l[12], (pins_l[12][0] - 16.0, pins_l[12][1]), (pins_l[12][0] - 16.0, mpu_loc[3][1]), mpu_loc[3]], net_name="I2C_SDA", layer=f_cu, width=W_SIG)
    add_route([pins_l[13], (pins_l[13][0] - 18.0, pins_l[13][1]), (pins_l[13][0] - 18.0, mpu_loc[2][1]), mpu_loc[2]], net_name="I2C_SCL", layer=f_cu, width=W_SIG)

    # Ground Network:
    add_route([bat_loc[1], tp_loc[1]], net_name="GND", layer=b_cu, width=W_GND)
    add_route([tp_loc[1], tp_loc[3]], net_name="GND", layer=b_cu, width=W_GND)
    add_route([tp_loc[3], bst_loc[1]], net_name="GND", layer=b_cu, width=W_GND)
    add_route([bst_loc[1], bst_loc[3]], net_name="GND", layer=b_cu, width=W_GND)

    add_route([r2_loc[1], cdiv_loc[1]], net_name="GND", layer=b_cu, width=1.0)
    add_route([r2_loc[1], (r2_loc[1][0], bst_loc[3][1]), bst_loc[3]], net_name="GND", layer=b_cu, width=W_GND)

    add_route([q2_loc[0], (q2_loc[0][0], q1_loc[2][1]), q1_loc[2]], net_name="GND", layer=b_cu, width=W_GND)
    add_route([q1_loc[2], rpd_loc[1]], net_name="GND", layer=b_cu, width=W_GND)
    add_route([rpd_loc[1], (rpd_loc[1][0], bst_loc[3][1]), bst_loc[3]], net_name="GND", layer=b_cu, width=W_GND)

    add_route([mpu_loc[1], hc_loc[3]], net_name="GND", layer=b_cu, width=W_GND)
    add_route([hc_loc[3], e18_loc[1]], net_name="GND", layer=b_cu, width=W_GND)
    add_route([hc_loc[3], rec2_loc[1]], net_name="GND", layer=b_cu, width=1.0)
    add_route([sos_loc[1], led_loc[1]], net_name="GND", layer=b_cu, width=1.0)
    add_route([led_loc[1], (led_loc[1][0], OY + HEIGHT - 4.0), (OX + 15.0, OY + HEIGHT - 4.0), e18_loc[1]], net_name="GND", layer=b_cu, width=W_GND)

    add_route([pins_l[22], (pins_l[22][0], OY + HEIGHT - 4.0), (OX + 15.0, OY + HEIGHT - 4.0)], net_name="GND", layer=b_cu, width=W_GND)
    add_route([pins_l[22], (pins_l[22][0], OY + HEIGHT - 4.0), (pins_r[23][0], OY + HEIGHT - 4.0), pins_r[23]], net_name="GND", layer=b_cu, width=W_GND)

    add_silk_text("GAY THONG MINH - CARRIER BOARD", (OX + 15.0, OY + 5.0), size=1.8)
    add_silk_text("REV 3.1 - INDUSTRIAL SAFE DUAL-LAYER / DIY JUMPER", (OX + 15.0, OY + 76.0), size=1.2)

    return board

if __name__ == '__main__':
    out_dir = r"d:\doan\SmartCane_PCB"
    os.makedirs(out_dir, exist_ok=True)
    b = build_complete_safe_board()
    pcb_path = os.path.join(out_dir, "SmartCane_PCB.kicad_pcb")
    b.Save(pcb_path)
    print(f"Board saved successfully: {pcb_path}")
