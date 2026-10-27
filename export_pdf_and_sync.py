import os
import shutil
import win32com.client
import pythoncom

BASE_DIR = r"C:\Users\Shruti\ResolveIT_Complaint_Management_System"
DESKTOP_DIR = r"C:\Users\Shruti\OneDrive\Desktop\ResolveIT_Complaint_Management_System"
os.makedirs(DESKTOP_DIR, exist_ok=True)

# Word to PDF conversion
print("Converting Mini-Project Report to PDF via Word COM...")
pythoncom.CoInitialize()
try:
    word = win32com.client.DispatchEx("Word.Application")
    word.Visible = False
    in_docx = os.path.join(BASE_DIR, "ResolveIT_Cloud_Computing_Mini_Project_Report.docx")
    out_pdf = os.path.join(BASE_DIR, "ResolveIT_Cloud_Computing_Mini_Project_Report.pdf")
    doc = word.Documents.Open(in_docx)
    doc.SaveAs(out_pdf, FileFormat=17) # 17 = wdFormatPDF
    doc.Close()
    print("Saved Report PDF:", out_pdf)
    word.Quit()
except Exception as e:
    print("Word conversion error:", e)

# PowerPoint to PDF conversion
print("Converting Presentation to PDF via PowerPoint COM...")
try:
    ppt = win32com.client.DispatchEx("PowerPoint.Application")
    in_pptx = os.path.join(BASE_DIR, "ResolveIT_Cloud_Computing_Mini_Project_Presentation.pptx")
    out_pdf = os.path.join(BASE_DIR, "ResolveIT_Cloud_Computing_Mini_Project_Presentation.pdf")
    pres = ppt.Presentations.Open(in_pptx, WithWindow=False)
    pres.SaveAs(out_pdf, 32) # 32 = ppSaveAsPDF
    pres.Close()
    print("Saved Presentation PDF:", out_pdf)
    ppt.Quit()
except Exception as e:
    print("PowerPoint conversion error:", e)

# Sync all files to Desktop folder
print("\nSyncing complete project to Desktop:", DESKTOP_DIR)
for item in os.listdir(BASE_DIR):
    s = os.path.join(BASE_DIR, item)
    d = os.path.join(DESKTOP_DIR, item)
    if os.path.isdir(s):
        if os.path.exists(d):
            shutil.rmtree(d)
        shutil.copytree(s, d)
    else:
        shutil.copy2(s, d)
    print(f"Copied: {item}")

print("\nAll files synchronized successfully to Desktop!")
