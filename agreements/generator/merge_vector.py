# Step 2: graft the overlay fields onto the ORIGINAL vector pages (no rasterizing).
import os, pikepdf
import fields as F
HERE=os.path.dirname(os.path.abspath(__file__))
SRC=os.path.join(HERE,"source_original.pdf")
OV=os.path.join(HERE,"overlay_fields.pdf")
OUT=os.path.join(HERE,"..","Crown_Prince_Rental_Agreement_Fillable.pdf")

name2page={}; group2page={}
for pi,flds in F.PAGES.items():
    for f in flds:
        (name2page if f["kind"]=="text" else group2page)[f.get("name") if f["kind"]=="text" else f["group"]]=pi

orig=pikepdf.open(SRC); ov=pikepdf.open(OV)
if not ov.Root.AcroForm.is_indirect:
    ov.Root.AcroForm=ov.make_indirect(ov.Root.AcroForm)
# strip page refs so copy_foreign won't drag overlay pages across
for field in ov.Root.AcroForm.Fields:
    if '/Kids' in field:
        for k in field.Kids:
            if '/P' in k: del k.P
    elif '/P' in field: del field.P
orig.Root.AcroForm=orig.copy_foreign(ov.Root.AcroForm)

def add(page, w):
    if '/Annots' in page: page.Annots.append(w)
    else: page.Annots=pikepdf.Array([w])
for field in orig.Root.AcroForm.Fields:
    name=str(field.T)
    if '/Kids' in field:
        i=group2page[name]
        for kid in field.Kids: kid.P=orig.pages[i].obj; add(orig.pages[i].obj, kid)
    else:
        i=name2page[name]; field.P=orig.pages[i].obj; add(orig.pages[i].obj, field)
orig.Root.AcroForm.NeedAppearances=False
orig.save(OUT); print("saved:", OUT)
