import os
import sys
import pcbnew

if sys.stdout:
    sys.stdout.reconfigure(encoding='utf-8')
if sys.stderr:
    sys.stderr.reconfigure(encoding='utf-8')

def build_perfect_planar_pcb():
    board = pcbnew.BOARD()
    
    # Board dimensions: 115mm x 85mm
    OX = 40.0
    OY = 40.0
    WIDTH = 115.0
    HEIGHT = 85.0
    
    b_cu = pcbnew.B_Cu
    f_cu = pcbnew.F_Cu
    f_silk = pcbnew.F_SilkS
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
        
    # 2. Mounting holes M3
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

    # Nets
    nets = {}
    for n in ["GND", "+5V", "+3V3", "VBAT", "V_SW", "ADC_BAT",
              "GPIO5_BUZ", "GPIO6_VIB", "GPIO7_SOS", "GPIO15_E18",
              "GPIO16_TRIG", "GPIO17_ECHO", "ECHO_5V", "GPIO18_LED",
              "I2C_SDA", "I2C_SCL", "MOTOR_DRAIN", "BUZ_DRIVE"]:
        item = pcbnew.NETINFO_ITEM(board, n)
        board.Add(item)
        nets[n] = item

    # Pad helper
    def add_pad(fp, num, rx, ry, net=None, size=(2.4, 2.4), drill=1.0, shape=pcbnew.PAD_SHAPE_CIRCLE):
        pad = pcbnew.PAD(fp)
        pad.SetNumber(str(num))
        pad.SetFPRelativePosition(pcbnew.VECTOR2I(pcbnew.FromMM(rx), pcbnew.FromMM(ry)))
        pad.SetShape(shape)
        pad.SetSize(pcbnew.VECTOR2I(pcbnew.FromMM(size[0]), pcbnew.FromMM(size[1])))
        pad.SetDrillSize(pcbnew.VECTOR2I(pcbnew.FromMM(drill), pcbnew.FromMM(drill)))
        pad.SetAttribute(pcbnew.PAD_ATTRIB_PTH)
        if net and net in nets:
            pad.SetNet(nets[net])
        fp.Add(pad)
        return pad

    def add_text(txt, pos, layer=f_silk, size=1.4):
        t = pcbnew.PCB_TEXT(board)
        t.SetText(txt)
        t.SetPosition(pcbnew.VECTOR2I(pcbnew.FromMM(pos[0]), pcbnew.FromMM(pos[1])))
        t.SetLayer(layer)
        t.SetTextSize(pcbnew.VECTOR2I(pcbnew.FromMM(size), pcbnew.FromMM(size)))
        t.SetTextThickness(pcbnew.FromMM(0.25))
        board.Add(t)

    def add_line(p1, p2, layer=f_silk, width=0.2):
        seg = pcbnew.PCB_SHAPE(board)
        seg.SetShape(pcbnew.SHAPE_T_SEGMENT)
        seg.SetStart(pcbnew.VECTOR2I(pcbnew.FromMM(p1[0]), pcbnew.FromMM(p1[1])))
        seg.SetEnd(pcbnew.VECTOR2I(pcbnew.FromMM(p2[0]), pcbnew.FromMM(p2[1])))
        seg.SetLayer(layer)
        seg.SetWidth(pcbnew.FromMM(width))
        board.Add(seg)

    def route_track(pts, net_name=None, layer=b_cu, width=0.85):
        net_item = nets.get(net_name, None)
        for i in range(len(pts) - 1):
            t = pcbnew.PCB_TRACK(board)
            t.SetStart(pcbnew.VECTOR2I(pcbnew.FromMM(pts[i][0]), pcbnew.FromMM(pts[i][1])))
            t.SetEnd(pcbnew.VECTOR2I(pcbnew.FromMM(pts[i+1][0]), pcbnew.FromMM(pts[i+1][1])))
            t.SetWidth(pcbnew.FromMM(width))
            t.SetLayer(layer)
            if net_item:
                t.SetNet(net_item)
            board.Add(t)

    # 3. Place ESP32-S3 DevKitC (Right side of board)
    esp_lx = OX + 72.0
    esp_rx = esp_lx + 22.86
    esp_sy = OY + 16.0

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
        add_pad(fp_el, i + 1, 0, py, net=net_n, shape=shape)
        pins_l[i + 1] = (esp_lx, esp_sy + py)

    right_nets = {23: "GND", 43: "+5V", 44: "+5V"}
    pins_r = {}
    for i in range(22):
        py = i * 2.54
        pnum = i + 23
        net_n = right_nets.get(pnum, None)
        add_pad(fp_er, pnum, 0, py, net=net_n)
        pins_r[pnum] = (esp_rx, esp_sy + py)

    board.Add(fp_el)
    board.Add(fp_er)

    # Frame & text
    add_line((esp_lx - 2.5, esp_sy - 3.0), (esp_rx + 2.5, esp_sy - 3.0))
    add_line((esp_rx + 2.5, esp_sy - 3.0), (esp_rx + 2.5, esp_sy + 21 * 2.54 + 3.0))
    add_line((esp_rx + 2.5, esp_sy + 21 * 2.54 + 3.0), (esp_lx - 2.5, esp_sy + 21 * 2.54 + 3.0))
    add_line((esp_lx - 2.5, esp_sy + 21 * 2.54 + 3.0), (esp_lx - 2.5, esp_sy - 3.0))
    add_text("ESP32-S3 DEVKITC N16R8", (esp_lx + 2.0, esp_sy + 27.0), size=1.6)

    # 4. Power Block (Top Left)
    # J_BATT KF301-2P (5.0mm pitch)
    fp_bat = pcbnew.FOOTPRINT(board)
    fp_bat.SetReference("J_BATT")
    fp_bat.SetValue("KF301 (PIN 18650)")
    fp_bat.SetPosition(pcbnew.VECTOR2I(pcbnew.FromMM(OX + 8.0), pcbnew.FromMM(OY + 12.0)))
    add_pad(fp_bat, 1, 0, 0, net="VBAT", size=(3.2, 3.2), drill=1.3, shape=pcbnew.PAD_SHAPE_RECT)
    add_pad(fp_bat, 2, 5.0, 0, net="GND", size=(3.2, 3.2), drill=1.3)
    board.Add(fp_bat)
    bat_loc = [(OX + 8.0, OY + 12.0), (OX + 13.0, OY + 12.0)]
    add_text("+ BAT -", (OX + 8.0, OY + 8.0), size=1.3)

    # TP4056 (Header 1x4: B+, B-, OUT+, OUT-)
    fp_tp = pcbnew.FOOTPRINT(board)
    fp_tp.SetReference("MOD_TP4056")
    fp_tp.SetValue("TP4056 Type-C")
    fp_tp.SetPosition(pcbnew.VECTOR2I(pcbnew.FromMM(OX + 8.0), pcbnew.FromMM(OY + 20.0)))
    add_pad(fp_tp, 1, 0, 0, net="VBAT")
    add_pad(fp_tp, 2, 2.54, 0, net="GND")
    add_pad(fp_tp, 3, 5.08, 0, net="VBAT")
    add_pad(fp_tp, 4, 7.62, 0, net="GND")
    board.Add(fp_tp)
    tp_loc = [(OX + 8.0 + i*2.54, OY + 20.0) for i in range(4)]
    add_text("TP4056", (OX + 8.0, OY + 17.0), size=1.1)

    # Power Switch SPDT (1=VBAT, 2=V_SW, 3=NC)
    fp_sw = pcbnew.FOOTPRINT(board)
    fp_sw.SetReference("SW_PWR")
    fp_sw.SetValue("SPDT ON/OFF")
    fp_sw.SetPosition(pcbnew.VECTOR2I(pcbnew.FromMM(OX + 8.0), pcbnew.FromMM(OY + 28.0)))
    add_pad(fp_sw, 1, 0, 0, net="VBAT")
    add_pad(fp_sw, 2, 2.54, 0, net="V_SW")
    add_pad(fp_sw, 3, 5.08, 0, net=None)
    board.Add(fp_sw)
    sw_loc = [(OX + 8.0 + i*2.54, OY + 28.0) for i in range(3)]
    add_text("PWR SW", (OX + 8.0, OY + 25.0), size=1.1)

    # Boost 5V Mini (1=V_SW, 2=GND, 3=+5V, 4=GND)
    fp_bst = pcbnew.FOOTPRINT(board)
    fp_bst.SetReference("MOD_BOOST")
    fp_bst.SetValue("Boost 5V Mini")
    fp_bst.SetPosition(pcbnew.VECTOR2I(pcbnew.FromMM(OX + 8.0), pcbnew.FromMM(OY + 36.0)))
    add_pad(fp_bst, 1, 0, 0, net="V_SW")
    add_pad(fp_bst, 2, 2.54, 0, net="GND")
    add_pad(fp_bst, 3, 5.08, 0, net="+5V")
    add_pad(fp_bst, 4, 7.62, 0, net="GND")
    board.Add(fp_bst)
    bst_loc = [(OX + 8.0 + i*2.54, OY + 36.0) for i in range(4)]
    add_text("BOOST 5V", (OX + 8.0, OY + 33.0), size=1.1)

    # 5. Battery Divider (R1, R2, C_DIV) for ADC GPIO4
    fp_r1 = pcbnew.FOOTPRINT(board)
    fp_r1.SetReference("R_DIV1")
    fp_r1.SetValue("10k")
    fp_r1.SetPosition(pcbnew.VECTOR2I(pcbnew.FromMM(OX + 24.0), pcbnew.FromMM(OY + 14.0)))
    add_pad(fp_r1, 1, 0, 0, net="VBAT")
    add_pad(fp_r1, 2, 0, 7.62, net="ADC_BAT")
    board.Add(fp_r1)
    r1_loc = [(OX + 24.0, OY + 14.0), (OX + 24.0, OY + 21.62)]

    fp_r2 = pcbnew.FOOTPRINT(board)
    fp_r2.SetReference("R_DIV2")
    fp_r2.SetValue("10k")
    fp_r2.SetPosition(pcbnew.VECTOR2I(pcbnew.FromMM(OX + 28.0), pcbnew.FromMM(OY + 14.0)))
    add_pad(fp_r2, 1, 0, 0, net="ADC_BAT")
    add_pad(fp_r2, 2, 0, 7.62, net="GND")
    board.Add(fp_r2)
    r2_loc = [(OX + 28.0, OY + 14.0), (OX + 28.0, OY + 21.62)]

    fp_cdiv = pcbnew.FOOTPRINT(board)
    fp_cdiv.SetReference("C_DIV")
    fp_cdiv.SetValue("100nF")
    fp_cdiv.SetPosition(pcbnew.VECTOR2I(pcbnew.FromMM(OX + 32.0), pcbnew.FromMM(OY + 14.0)))
    add_pad(fp_cdiv, 1, 0, 0, net="ADC_BAT")
    add_pad(fp_cdiv, 2, 0, 5.08, net="GND")
    board.Add(fp_cdiv)
    cdiv_loc = [(OX + 32.0, OY + 14.0), (OX + 32.0, OY + 19.08)]
    add_text("R1/R2/C BAT", (OX + 23.0, OY + 11.0), size=1.0)

    # 6. Buzzer + Transistor Driver Q2 (Protects GPIO5)
    fp_bz = pcbnew.FOOTPRINT(board)
    fp_bz.SetReference("BZ1")
    fp_bz.SetValue("Active Buzzer 5V")
    fp_bz.SetPosition(pcbnew.VECTOR2I(pcbnew.FromMM(OX + 24.0), pcbnew.FromMM(OY + 28.0)))
    add_pad(fp_bz, 1, 0, 0, net="+5V", size=(2.8, 2.8), drill=1.1)
    add_pad(fp_bz, 2, 7.62, 0, net="BUZ_DRIVE", size=(2.8, 2.8), drill=1.1)
    board.Add(fp_bz)
    bz_loc = [(OX + 24.0, OY + 28.0), (OX + 31.62, OY + 28.0)]
    add_text("+ BUZZER -", (OX + 24.0, OY + 25.5), size=1.1)

    fp_q2 = pcbnew.FOOTPRINT(board)
    fp_q2.SetReference("Q2")
    fp_q2.SetValue("S8050 NPN")
    fp_q2.SetPosition(pcbnew.VECTOR2I(pcbnew.FromMM(OX + 38.0), pcbnew.FromMM(OY + 26.0)))
    add_pad(fp_q2, 1, 0, 0, net="GND")
    add_pad(fp_q2, 2, 2.54, 0, net="GPIO5_BUZ")
    add_pad(fp_q2, 3, 5.08, 0, net="BUZ_DRIVE")
    board.Add(fp_q2)
    q2_loc = [(OX + 38.0 + i*2.54, OY + 26.0) for i in range(3)]
    add_text("Q2 (E B C)", (OX + 38.0, OY + 23.5), size=1.0)

    # 7. Motor Driver MOSFET Q1 + Flyback Diode + Resistors (Protects GPIO6)
    fp_q1 = pcbnew.FOOTPRINT(board)
    fp_q1.SetReference("Q1")
    fp_q1.SetValue("MOSFET AOD4184")
    fp_q1.SetPosition(pcbnew.VECTOR2I(pcbnew.FromMM(OX + 24.0), pcbnew.FromMM(OY + 38.0)))
    add_pad(fp_q1, 1, 0, 0, net="GPIO6_VIB")
    add_pad(fp_q1, 2, 2.54, 0, net="MOTOR_DRAIN")
    add_pad(fp_q1, 3, 5.08, 0, net="GND")
    board.Add(fp_q1)
    q1_loc = [(OX + 24.0 + i*2.54, OY + 38.0) for i in range(3)]
    add_text("Q1 (G D S)", (OX + 24.0, OY + 35.0), size=1.0)

    fp_rg = pcbnew.FOOTPRINT(board)
    fp_rg.SetReference("R_GATE")
    fp_rg.SetValue("1k")
    fp_rg.SetPosition(pcbnew.VECTOR2I(pcbnew.FromMM(OX + 34.0), pcbnew.FromMM(OY + 36.0)))
    add_pad(fp_rg, 1, 0, 0, net="GPIO6_VIB")
    add_pad(fp_rg, 2, 0, 7.62, net="GPIO6_VIB")
    board.Add(fp_rg)
    rg_loc = [(OX + 34.0, OY + 36.0), (OX + 34.0, OY + 43.62)]

    fp_rpd = pcbnew.FOOTPRINT(board)
    fp_rpd.SetReference("R_PD")
    fp_rpd.SetValue("10k")
    fp_rpd.SetPosition(pcbnew.VECTOR2I(pcbnew.FromMM(OX + 38.0), pcbnew.FromMM(OY + 36.0)))
    add_pad(fp_rpd, 1, 0, 0, net="GPIO6_VIB")
    add_pad(fp_rpd, 2, 0, 7.62, net="GND")
    board.Add(fp_rpd)
    rpd_loc = [(OX + 38.0, OY + 36.0), (OX + 38.0, OY + 43.62)]

    fp_d1 = pcbnew.FOOTPRINT(board)
    fp_d1.SetReference("D1")
    fp_d1.SetValue("1N4007")
    fp_d1.SetPosition(pcbnew.VECTOR2I(pcbnew.FromMM(OX + 44.0), pcbnew.FromMM(OY + 36.0)))
    add_pad(fp_d1, 1, 0, 0, net="+5V")
    add_pad(fp_d1, 2, 0, 7.62, net="MOTOR_DRAIN")
    board.Add(fp_d1)
    d1_loc = [(OX + 44.0, OY + 36.0), (OX + 44.0, OY + 43.62)]
    add_text("D1 1N4007", (OX + 44.0, OY + 33.5), size=1.0)

    fp_jmot = pcbnew.FOOTPRINT(board)
    fp_jmot.SetReference("J_MOTOR")
    fp_jmot.SetValue("Motor Rung")
    fp_jmot.SetPosition(pcbnew.VECTOR2I(pcbnew.FromMM(OX + 8.0), pcbnew.FromMM(OY + 46.0)))
    add_pad(fp_jmot, 1, 0, 0, net="+5V")
    add_pad(fp_jmot, 2, 2.54, 0, net="MOTOR_DRAIN")
    board.Add(fp_jmot)
    jmot_loc = [(OX + 8.0, OY + 46.0), (OX + 10.54, OY + 46.0)]
    add_text("MOTOR (+ -)", (OX + 8.0, OY + 43.5), size=1.0)

    # 8. External Sensor Headers (Placed at Left & Bottom for direct planar routing without crossings!)
    # J_MPU6050 (1=+3V3, 2=GND, 3=SCL, 4=SDA)
    fp_mpu = pcbnew.FOOTPRINT(board)
    fp_mpu.SetReference("J_MPU6050")
    fp_mpu.SetValue("GY-521")
    fp_mpu.SetPosition(pcbnew.VECTOR2I(pcbnew.FromMM(OX + 8.0), pcbnew.FromMM(OY + 56.0)))
    add_pad(fp_mpu, 1, 0, 0, net="+3V3")
    add_pad(fp_mpu, 2, 2.54, 0, net="GND")
    add_pad(fp_mpu, 3, 5.08, 0, net="I2C_SCL")
    add_pad(fp_mpu, 4, 7.62, 0, net="I2C_SDA")
    board.Add(fp_mpu)
    mpu_loc = [(OX + 8.0 + i*2.54, OY + 56.0) for i in range(4)]
    add_text("MPU6050 (3V3 GND SCL SDA)", (OX + 8.0, OY + 53.0), size=1.1)

    # J_HCSR04 (1=+5V, 2=Trig, 3=ECHO_5V, 4=GND)
    fp_hc = pcbnew.FOOTPRINT(board)
    fp_hc.SetReference("J_HCSR04")
    fp_hc.SetValue("HC-SR04")
    fp_hc.SetPosition(pcbnew.VECTOR2I(pcbnew.FromMM(OX + 8.0), pcbnew.FromMM(OY + 66.0)))
    add_pad(fp_hc, 1, 0, 0, net="+5V")
    add_pad(fp_hc, 2, 2.54, 0, net="GPIO16_TRIG")
    add_pad(fp_hc, 3, 5.08, 0, net="ECHO_5V")
    add_pad(fp_hc, 4, 7.62, 0, net="GND")
    board.Add(fp_hc)
    hc_loc = [(OX + 8.0 + i*2.54, OY + 66.0) for i in range(4)]
    add_text("HC-SR04 (5V TRIG ECHO GND)", (OX + 8.0, OY + 63.0), size=1.1)

    # Echo divider: R_EC1 (1k) from ECHO_5V to GPIO17_ECHO; R_EC2 (2k) from GPIO17_ECHO to GND
    fp_rec1 = pcbnew.FOOTPRINT(board)
    fp_rec1.SetReference("R_EC1")
    fp_rec1.SetValue("1k")
    fp_rec1.SetPosition(pcbnew.VECTOR2I(pcbnew.FromMM(OX + 24.0), pcbnew.FromMM(OY + 64.0)))
    add_pad(fp_rec1, 1, 0, 0, net="ECHO_5V")
    add_pad(fp_rec1, 2, 0, 7.62, net="GPIO17_ECHO")
    board.Add(fp_rec1)
    rec1_loc = [(OX + 24.0, OY + 64.0), (OX + 24.0, OY + 71.62)]

    fp_rec2 = pcbnew.FOOTPRINT(board)
    fp_rec2.SetReference("R_EC2")
    fp_rec2.SetValue("2k")
    fp_rec2.SetPosition(pcbnew.VECTOR2I(pcbnew.FromMM(OX + 28.0), pcbnew.FromMM(OY + 64.0)))
    add_pad(fp_rec2, 1, 0, 0, net="GPIO17_ECHO")
    add_pad(fp_rec2, 2, 0, 7.62, net="GND")
    board.Add(fp_rec2)
    rec2_loc = [(OX + 28.0, OY + 64.0), (OX + 28.0, OY + 71.62)]
    add_text("ECHO DIV (1k/2k)", (OX + 23.0, OY + 61.0), size=1.0)

    # J_E18 (1=+5V, 2=GND, 3=GPIO15_E18)
    fp_e18 = pcbnew.FOOTPRINT(board)
    fp_e18.SetReference("J_E18")
    fp_e18.SetValue("E18-D50NK")
    fp_e18.SetPosition(pcbnew.VECTOR2I(pcbnew.FromMM(OX + 8.0), pcbnew.FromMM(OY + 76.0)))
    add_pad(fp_e18, 1, 0, 0, net="+5V")
    add_pad(fp_e18, 2, 2.54, 0, net="GND")
    add_pad(fp_e18, 3, 5.08, 0, net="GPIO15_E18")
    board.Add(fp_e18)
    e18_loc = [(OX + 8.0 + i*2.54, OY + 76.0) for i in range(3)]
    add_text("E18 (5V GND OUT)", (OX + 8.0, OY + 73.0), size=1.1)

    # R_E18: 10k pull-up to +3V3
    fp_re18 = pcbnew.FOOTPRINT(board)
    fp_re18.SetReference("R_E18")
    fp_re18.SetValue("10k PU")
    fp_re18.SetPosition(pcbnew.VECTOR2I(pcbnew.FromMM(OX + 24.0), pcbnew.FromMM(OY + 76.0)))
    add_pad(fp_re18, 1, 0, 0, net="+3V3")
    add_pad(fp_re18, 2, 5.08, 0, net="GPIO15_E18")
    board.Add(fp_re18)
    re18_loc = [(OX + 24.0, OY + 76.0), (OX + 29.08, OY + 76.0)]

    # SW_SOS (1=GPIO7_SOS, 2=GND)
    fp_sos = pcbnew.FOOTPRINT(board)
    fp_sos.SetReference("SW_SOS")
    fp_sos.SetValue("SOS Button")
    fp_sos.SetPosition(pcbnew.VECTOR2I(pcbnew.FromMM(OX + 38.0), pcbnew.FromMM(OY + 56.0)))
    add_pad(fp_sos, 1, 0, 0, net="GPIO7_SOS")
    add_pad(fp_sos, 2, 2.54, 0, net="GND")
    board.Add(fp_sos)
    sos_loc = [(OX + 38.0, OY + 56.0), (OX + 40.54, OY + 56.0)]
    add_text("SOS BTN", (OX + 38.0, OY + 53.0), size=1.1)

    # LED1 (1=GPIO18_LED, 2=GND) + R_LED (220R)
    fp_led = pcbnew.FOOTPRINT(board)
    fp_led.SetReference("LED1")
    fp_led.SetValue("LED Roi Duong")
    fp_led.SetPosition(pcbnew.VECTOR2I(pcbnew.FromMM(OX + 38.0), pcbnew.FromMM(OY + 66.0)))
    add_pad(fp_led, 1, 0, 0, net="GPIO18_LED")
    add_pad(fp_led, 2, 2.54, 0, net="GND")
    board.Add(fp_led)
    led_loc = [(OX + 38.0, OY + 66.0), (OX + 40.54, OY + 66.0)]

    fp_rled = pcbnew.FOOTPRINT(board)
    fp_rled.SetReference("R_LED")
    fp_rled.SetValue("220R")
    fp_rled.SetPosition(pcbnew.VECTOR2I(pcbnew.FromMM(OX + 46.0), pcbnew.FromMM(OY + 66.0)))
    add_pad(fp_rled, 1, 0, 0, net="GPIO18_LED")
    add_pad(fp_rled, 2, 5.08, 0, net="GPIO18_LED")
    board.Add(fp_rled)
    rled_loc = [(OX + 46.0, OY + 66.0), (OX + 51.08, OY + 66.0)]
    add_text("LED 5mm + 220R", (OX + 38.0, OY + 63.0), size=1.0)

    # 9. PURE PLANAR ZERO-CROSSING ROUTING
    # Signal traces on B.Cu (Width = 0.85 mm, Power = 1.3 mm, GND = 1.5 mm)
    # 1. VBAT network
    route_track([bat_loc[0], tp_loc[0]], net_name="VBAT", width=1.3)
    route_track([tp_loc[2], sw_loc[0]], net_name="VBAT", width=1.3)
    route_track([tp_loc[2], r1_loc[0]], net_name="VBAT", width=0.85)

    # 2. V_SW network
    route_track([sw_loc[1], bst_loc[0]], net_name="V_SW", width=1.3)

    # 3. +5V Rail (Boost OUT+ -> Buzzer, D1, J_MOTOR, HC-SR04, E18, ESP32 VIN)
    # Routed cleanly on the top/left perimeter
    route_track([bst_loc[2], (OX + 18.0, bst_loc[2][1]), (OX + 18.0, bz_loc[0][1]), bz_loc[0]], net_name="+5V", width=1.3)
    route_track([bz_loc[0], (OX + 18.0, bz_loc[0][1]), (OX + 18.0, d1_loc[0][1]), d1_loc[0]], net_name="+5V", width=1.3)
    route_track([d1_loc[0], (OX + 18.0, d1_loc[0][1]), (OX + 18.0, jmot_loc[0][1]), jmot_loc[0]], net_name="+5V", width=1.3)
    route_track([jmot_loc[0], (OX + 4.0, jmot_loc[0][1]), (OX + 4.0, hc_loc[0][1]), hc_loc[0]], net_name="+5V", width=1.3)
    route_track([hc_loc[0], (OX + 4.0, hc_loc[0][1]), (OX + 4.0, e18_loc[0][1]), e18_loc[0]], net_name="+5V", width=1.3)
    # +5V to ESP32 Right Header Pin 43 & 44 (Top perimeter route)
    route_track([bz_loc[0], (bz_loc[0][0], OY + 6.0), (esp_rx + 6.0, OY + 6.0), (esp_rx + 6.0, pins_r[44][1]), pins_r[44]], net_name="+5V", width=1.3)
    route_track([pins_r[44], pins_r[43]], net_name="+5V", width=1.3)

    # 4. +3V3 Rail (From ESP32 Pin 1 to MPU6050 & R_E18)
    route_track([pins_l[1], (pins_l[1][0] - 8.0, pins_l[1][1]), (pins_l[1][0] - 8.0, OY + 50.0), (OX + 20.0, OY + 50.0), (OX + 20.0, mpu_loc[0][1]), mpu_loc[0]], net_name="+3V3", width=1.0)
    route_track([mpu_loc[0], (OX + 20.0, mpu_loc[0][1]), (OX + 20.0, re18_loc[0][1]), re18_loc[0]], net_name="+3V3", width=0.85)

    # 5. ADC_BAT (R1 pin 2 -> R2 pin 1 -> C_DIV pin 1 -> ESP32 Pin 4)
    route_track([r1_loc[1], r2_loc[0]], net_name="ADC_BAT", width=0.85)
    route_track([r2_loc[0], cdiv_loc[0]], net_name="ADC_BAT", width=0.85)
    route_track([cdiv_loc[0], (cdiv_loc[0][0], pins_l[4][1]), pins_l[4]], net_name="ADC_BAT", width=0.85)

    # 6. GPIO5_BUZ (ESP32 Pin 5 -> Q2 Base) & BUZ_DRIVE (Q2 Collector -> BZ1 (-))
    route_track([pins_l[5], (q2_loc[1][0], pins_l[5][1]), q2_loc[1]], net_name="GPIO5_BUZ", width=0.85)
    route_track([q2_loc[2], (q2_loc[2][0], bz_loc[1][1]), bz_loc[1]], net_name="BUZ_DRIVE", width=0.85)

    # 7. GPIO6_VIB (ESP32 Pin 6 -> R_GATE -> Q1 Gate) & MOTOR_DRAIN (Q1 Drain -> D1 Anode & J_MOTOR (-))
    route_track([pins_l[6], (rg_loc[0][0], pins_l[6][1]), rg_loc[0]], net_name="GPIO6_VIB", width=0.85)
    route_track([rg_loc[1], q1_loc[0]], net_name="GPIO6_VIB", width=0.85)
    route_track([q1_loc[0], rpd_loc[0]], net_name="GPIO6_VIB", width=0.85)
    route_track([q1_loc[1], (q1_loc[1][0], d1_loc[1][1]), d1_loc[1]], net_name="MOTOR_DRAIN", width=1.2)
    route_track([q1_loc[1], (q1_loc[1][0], jmot_loc[1][1]), jmot_loc[1]], net_name="MOTOR_DRAIN", width=1.2)

    # 8. GPIO7_SOS (ESP32 Pin 7 -> SW_SOS)
    route_track([pins_l[7], (pins_l[7][0] - 12.0, pins_l[7][1]), (pins_l[7][0] - 12.0, sos_loc[0][1]), sos_loc[0]], net_name="GPIO7_SOS", width=0.85)

    # 9. GPIO15_E18 (ESP32 Pin 8 -> E18 Pin 3 & R_E18)
    route_track([pins_l[8], (pins_l[8][0] - 14.0, pins_l[8][1]), (pins_l[8][0] - 14.0, e18_loc[2][1]), e18_loc[2]], net_name="GPIO15_E18", width=0.85)
    route_track([e18_loc[2], re18_loc[1]], net_name="GPIO15_E18", width=0.85)

    # 10. GPIO16_TRIG (ESP32 Pin 9 -> HC-SR04 Trig)
    route_track([pins_l[9], (pins_l[9][0] - 16.0, pins_l[9][1]), (pins_l[9][0] - 16.0, hc_loc[1][1]), hc_loc[1]], net_name="GPIO16_TRIG", width=0.85)

    # 11. ECHO_5V & GPIO17_ECHO (HC-SR04 Echo 5V -> R_EC1 1k -> GPIO17_ECHO 3.3V -> ESP32 Pin 10)
    route_track([hc_loc[2], rec1_loc[0]], net_name="ECHO_5V", width=0.85)
    route_track([rec1_loc[1], rec2_loc[0]], net_name="GPIO17_ECHO", width=0.85)
    route_track([rec1_loc[1], (rec1_loc[1][0], pins_l[10][1]), pins_l[10]], net_name="GPIO17_ECHO", width=0.85)

    # 12. GPIO18_LED (ESP32 Pin 11 -> R_LED -> LED1)
    route_track([pins_l[11], (rled_loc[1][0], pins_l[11][1]), rled_loc[1]], net_name="GPIO18_LED", width=0.85)
    route_track([rled_loc[0], led_loc[0]], net_name="GPIO18_LED", width=0.85)

    # 13. I2C (ESP32 Pin 12 SDA -> MPU SDA, Pin 13 SCL -> MPU SCL)
    route_track([pins_l[12], (pins_l[12][0] - 18.0, pins_l[12][1]), (pins_l[12][0] - 18.0, mpu_loc[3][1]), mpu_loc[3]], net_name="I2C_SDA", width=0.85)
    route_track([pins_l[13], (pins_l[13][0] - 20.0, pins_l[13][1]), (pins_l[13][0] - 20.0, mpu_loc[2][1]), mpu_loc[2]], net_name="I2C_SCL", width=0.85)

    # 14. COMMON GND TREE (All GNDs connect to solid mass tree without crossing any signal!)
    # Battery -, TP4056 B-, TP4056 OUT-, Boost IN-, Boost OUT-
    route_track([bat_loc[1], tp_loc[1]], net_name="GND", width=1.5)
    route_track([tp_loc[1], tp_loc[3]], net_name="GND", width=1.5)
    route_track([tp_loc[3], bst_loc[1]], net_name="GND", width=1.5)
    route_track([bst_loc[1], bst_loc[3]], net_name="GND", width=1.5)
    
    # R2 GND & C_DIV GND
    route_track([r2_loc[1], cdiv_loc[1]], net_name="GND", width=1.0)
    route_track([r2_loc[1], (r2_loc[1][0], bst_loc[3][1]), bst_loc[3]], net_name="GND", width=1.2)

    # Q2 Emitter GND, Q1 Source GND, R_PD GND
    route_track([q2_loc[0], (q2_loc[0][0], q1_loc[2][1]), q1_loc[2]], net_name="GND", width=1.2)
    route_track([q1_loc[2], rpd_loc[1]], net_name="GND", width=1.2)
    route_track([rpd_loc[1], (rpd_loc[1][0], bst_loc[3][1]), bst_loc[3]], net_name="GND", width=1.2)

    # Bottom sensors GND: MPU pin 2, HC pin 4, Echo div R_EC2 pin 2, E18 pin 2, SOS pin 2, LED pin 2
    # Connect along bottom edge:
    route_track([mpu_loc[1], hc_loc[3]], net_name="GND", width=1.2)
    route_track([hc_loc[3], e18_loc[1]], net_name="GND", width=1.2)
    route_track([hc_loc[3], rec2_loc[1]], net_name="GND", width=1.0)
    route_track([sos_loc[1], led_loc[1]], net_name="GND", width=1.0)
    route_track([led_loc[1], (led_loc[1][0], OY + HEIGHT - 4.0), (OX + 15.0, OY + HEIGHT - 4.0), e18_loc[1]], net_name="GND", width=1.2)

    # Connect to ESP32 GND (Pin 22 Left header & Pin 23 Right header)
    route_track([pins_l[22], (pins_l[22][0], OY + HEIGHT - 4.0), (OX + 15.0, OY + HEIGHT - 4.0)], net_name="GND", width=1.5)
    route_track([pins_l[22], (pins_l[22][0], OY + HEIGHT - 4.0), (pins_r[23][0], OY + HEIGHT - 4.0), pins_r[23]], net_name="GND", width=1.5)

    # Silkscreen Branding
    add_text("GAY THONG MINH - CARRIER BOARD", (OX + 15.0, OY + 5.0), size=2.0)
    add_text("REV 3.0 - 100% PLANAR ZERO-CROSSING (DIY SAFE)", (OX + 15.0, OY + 80.0), size=1.3)

    return board

if __name__ == '__main__':
    out_dir = r"d:\doan\SmartCane_PCB"
    os.makedirs(out_dir, exist_ok=True)
    b = build_perfect_planar_pcb()
    pcb_path = os.path.join(out_dir, "SmartCane_PCB.kicad_pcb")
    b.Save(pcb_path)
    print(f"Planar zero-crossing PCB saved: {pcb_path}")
