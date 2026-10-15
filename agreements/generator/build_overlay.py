# Step 1: build a fields-ONLY overlay (transparent pages) from fields.py.
import os
from reportlab.pdfgen import canvas
from reportlab.lib.colors import black
import fields as F
HERE=os.path.dirname(os.path.abspath(__file__))
W,H=612.0,792.0
OUT=os.path.join(HERE,"overlay_fields.pdf")
c=canvas.Canvas(OUT, pagesize=(W,H)); af=c.acroForm
for pi in range(4):
    for f in F.PAGES.get(pi, []):
        if f["kind"]=="text":
            x0,x1,yl=f["x0"],f["x1"],f["yline"]; y=H-yl; w=x1-x0
            fs=11 if w>=40 else 10
            af.textfield(name=f["name"], value="", x=x0, y=y+1, width=w, height=14,
                         borderWidth=0, borderStyle='underlined', forceBorder=False,
                         fillColor=None, borderColor=None, textColor=black,
                         fontName='Helvetica', fontSize=fs, maxlen=120,
                         tooltip=f["name"].replace('_',' ').title())
        else:
            bx,by,sz=f["bx"],f["by_top"],f["size"]; y=H-(by+sz)
            af.radio(name=f["group"], value=f["value"], selected=False,
                     x=bx, y=y, size=sz, buttonStyle='check', shape='square',
                     borderWidth=0, borderColor=None, fillColor=None,
                     textColor=black, forceBorder=False,
                     tooltip="%s: %s"%(f["group"].replace('_',' ').title(), f["value"]))
    c.showPage()
c.save(); print("overlay built:", OUT)
