import pypdfium2 as pdfium
from reportlab.pdfgen import canvas
from reportlab.lib.colors import black, transparent
import fields as F
import io

import os
HERE=os.path.dirname(os.path.abspath(__file__))
SRC=os.path.join(HERE,"source_original.pdf")
OUT=os.path.join(HERE,"..","Crown_Prince_Rental_Agreement_Fillable.pdf")
W,H=612.0,792.0
DPI=200; scale=DPI/72.0

pdf=pdfium.PdfDocument(SRC)
c=canvas.Canvas(OUT, pagesize=(W,H))
af=c.acroForm
for pi in range(len(pdf)):
    # background: rasterized original page
    img=pdf[pi].render(scale=scale).to_pil().convert("RGB")
    bio=io.BytesIO(); img.save(bio,format="PNG"); bio.seek(0)
    from reportlab.lib.utils import ImageReader
    c.drawImage(ImageReader(bio), 0, 0, width=W, height=H)
    for f in F.PAGES.get(pi, []):
        if f["kind"]=="text":
            x0,x1,yl=f["x0"],f["x1"],f["yline"]
            y=H-yl            # lower-left y
            w=x1-x0; h=14
            fs=11 if w>=40 else 10
            af.textfield(name=f["name"], value="", x=x0, y=y+1, width=w, height=h,
                         borderWidth=0, borderStyle='underlined', forceBorder=False,
                         fillColor=None, borderColor=None, textColor=black,
                         fontName='Helvetica', fontSize=fs, maxlen=120,
                         tooltip=f["name"].replace('_',' ').title())
        elif f["kind"]=="radio":
            bx,by,sz=f["bx"],f["by_top"],f["size"]
            y=H-(by+sz)
            af.radio(name=f["group"], value=f["value"], selected=False,
                     x=bx, y=y, size=sz, buttonStyle='check', shape='square',
                     borderWidth=0, borderColor=None, fillColor=None,
                     textColor=black, forceBorder=False,
                     tooltip="%s: %s"%(f["group"].replace('_',' ').title(), f["value"]))
        elif f["kind"]=="check":
            bx,by,sz=f["bx"],f["by_top"],f["size"]
            y=H-(by+sz)
            af.checkbox(name=f["name"], x=bx, y=y, size=sz, checked=False,
                        buttonStyle='check', borderWidth=0.6, borderColor=black,
                        fillColor=None, forceBorder=False,
                        tooltip=f["name"].replace('_',' ').title())
    c.showPage()
c.save()
print("built", OUT)
