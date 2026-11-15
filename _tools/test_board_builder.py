import os
import sys
import math

# Force UTF-8 encoding
if sys.stdout:
    sys.stdout.reconfigure(encoding='utf-8')
if sys.stderr:
    sys.stderr.reconfigure(encoding='utf-8')

import pcbnew

def build_board():
    board = pcbnew.BOARD()
    
    # Board dimensions in mm
    WIDTH = 92.0
    HEIGHT = 68.0
    ORIGIN_X = 50.0
    ORIGIN_Y = 50.0
    
    # Layers
    b_cu = pcbnew.B_Cu
    f_cu = pcbnew.F_Cu
    f_silk = pcbnew.F_SilkS
    b_silk = pcbnew.B_SilkS
    edge_cuts = pcbnew.Edge_Cuts
    
    # 1. Edge Cuts (Board Outline 92 x 68 mm with rounded/clean border)
    x0 = pcbnew.FromMM(ORIGIN_X)
    y0 = pcbnew.FromMM(ORIGIN_Y)
    x1 = pcbnew.FromMM(ORIGIN_X + WIDTH)
    y1 = pcbnew.FromMM(ORIGIN_Y + HEIGHT)
    
    corners = [
        pcbnew.VECTOR2I(x0, y0),
        pcbnew.VECTOR2I(x1, y0),
        pcbnew.VECTOR2I(x1, y1),
        pcbnew.VECTOR2I(x0, y1),
        pcbnew.VECTOR2I(x0, y0)
    ]
    for i in range(len(corners) - 1):
        seg = pcbnew.PCB_SHAPE(board)
        seg.SetShape(pcbnew.SHAPE_T_SEGMENT)
        seg.SetStart(corners[i])
        seg.SetEnd(corners[i+1])
        seg.SetLayer(edge_cuts)
        seg.SetWidth(pcbnew.FromMM(0.2))
        board.Add(seg)
        
    # 2. Mounting Holes M3 (diameter 3.2mm, pad 6.0mm)
    mount_offsets = [(4.0, 4.0), (WIDTH - 4.0, 4.0), (4.0, HEIGHT - 4.0), (WIDTH - 4.0, HEIGHT - 4.0)]
    for idx, (mx, my) in enumerate(mount_offsets, 1):
        fp = pcbnew.FOOTPRINT(board)
        fp.SetReference(f"H{idx}")
        fp.SetValue("MountingHole_M3")
        fp.SetPosition(pcbnew.VECTOR2I(pcbnew.FromMM(ORIGIN_X + mx), pcbnew.FromMM(ORIGIN_Y + my)))
        pad = pcbnew.PAD(fp)
        pad.SetNumber("1")
        pad.SetShape(pcbnew.PAD_SHAPE_CIRCLE)
        pad.SetSize(pcbnew.VECTOR2I(pcbnew.FromMM(6.0), pcbnew.FromMM(6.0)))
        pad.SetDrillSize(pcbnew.VECTOR2I(pcbnew.FromMM(3.2), pcbnew.FromMM(3.2)))
        pad.SetAttribute(pcbnew.PAD_ATTRIB_NPTH)
        fp.Add(pad)
        board.Add(fp)
        
    print("Edge cuts and mounting holes added.")
    return board

if __name__ == '__main__':
    b = build_board()
    out_dir = r"d:\doan\SmartCane_PCB"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "SmartCane_PCB.kicad_pcb")
    b.Save(out_path)
    print(f"Saved initial board to {out_path}")
