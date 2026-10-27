import os
from PIL import Image, ImageDraw, ImageFont

ASSETS_DIR = r"C:\Users\Shruti\ResolveIT_Complaint_Management_System\assets"
os.makedirs(ASSETS_DIR, exist_ok=True)

def get_font(size, bold=False):
    paths = [
        r"C:\Windows\Fonts\arialbd.ttf" if bold else r"C:\Windows\Fonts\arial.ttf",
        r"C:\Windows\Fonts\calibrib.ttf" if bold else r"C:\Windows\Fonts\calibri.ttf",
        r"C:\Windows\Fonts\segoeuib.ttf" if bold else r"C:\Windows\Fonts\segoeui.ttf",
    ]
    for p in paths:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except:
                pass
    return ImageFont.load_default()

# -----------------------------------------------------------------------------
# 1. Architecture Diagram
# -----------------------------------------------------------------------------
def make_architecture_diagram():
    W, H = 1400, 720
    img = Image.new("RGB", (W, H), "#FFFFFF")
    draw = ImageDraw.Draw(img)
    draw.rectangle([(2, 2), (W-3, H-3)], outline="#CBD5E1", width=2)
    
    font_title = get_font(26, bold=True)
    font_layer = get_font(20, bold=True)
    font_box_h = get_font(18, bold=True)
    font_box_p = get_font(14, bold=False)
    
    # Title
    draw.text((W//2, 35), "ResolveIT: Cloud System Architecture Diagram", fill="#1E40AF", font=font_title, anchor="mm")
    
    # 3 Main Tiers / Layers
    tiers = [
        ("Client Tier (User Devices)", 80, 200, "#EFF6FF", "#3B82F6"),
        ("Cloud Frontend Hosting Tier (AWS Amplify / Azure SWA)", 230, 370, "#F0FDF4", "#10B981"),
        ("Cloud Backend & Database Tier (Google Cloud / Firebase)", 400, 680, "#FEF3C7", "#F59E0B")
    ]
    
    for name, y1, y2, bg, border in tiers:
        draw.rounded_rectangle([(40, y1), (W-40, y2)], radius=14, fill=bg, outline=border, width=2)
        draw.text((60, y1 + 18), name, fill=border, font=font_layer)
        
    # Tier 1 Components: Student & Admin
    draw.rounded_rectangle([(120, 115), (480, 185)], radius=10, fill="#FFFFFF", outline="#1E40AF", width=2)
    draw.text((300, 140), "Student (Client Browser)", fill="#1E40AF", font=font_box_h, anchor="mm")
    draw.text((300, 165), "Desktop / Smartphone (Chrome, Edge, Safari)", fill="#475569", font=font_box_p, anchor="mm")
    
    draw.rounded_rectangle([(920, 115), (1280, 185)], radius=10, fill="#FFFFFF", outline="#1E40AF", width=2)
    draw.text((1100, 140), "College Administrator", fill="#1E40AF", font=font_box_h, anchor="mm")
    draw.text((1100, 165), "Admin Web Portal / Dashboard", fill="#475569", font=font_box_p, anchor="mm")
    
    # Tier 2 Components: AWS Amplify / Azure Static Web Apps
    draw.rounded_rectangle([(120, 275), (660, 355)], radius=10, fill="#FFFFFF", outline="#059669", width=2)
    draw.text((390, 302), "Option A: AWS Amplify Hosting", fill="#059669", font=font_box_h, anchor="mm")
    draw.text((390, 330), "Global Amazon CloudFront CDN • Automated CI/CD • Free SSL", fill="#334155", font=font_box_p, anchor="mm")
    
    draw.rounded_rectangle([(740, 275), (1280, 355)], radius=10, fill="#FFFFFF", outline="#059669", width=2)
    draw.text((1010, 302), "Option B: Azure Static Web Apps", fill="#059669", font=font_box_h, anchor="mm")
    draw.text((1010, 330), "Global Edge Hosting • GitHub Actions Pipeline • Custom Domains", fill="#334155", font=font_box_p, anchor="mm")
    
    # Tier 3 Components: Firebase Auth, Firestore, Security Rules
    draw.rounded_rectangle([(120, 460), (480, 650)], radius=10, fill="#FFFFFF", outline="#D97706", width=2)
    draw.text((300, 490), "Firebase Authentication", fill="#D97706", font=font_box_h, anchor="mm")
    draw.text((300, 525), "• Email / Password Authentication", fill="#475569", font=font_box_p, anchor="mm")
    draw.text((300, 555), "• Secure JWT Token Issuance", fill="#475569", font=font_box_p, anchor="mm")
    draw.text((300, 585), "• Client Session Persistence", fill="#475569", font=font_box_p, anchor="mm")
    draw.text((300, 615), "• Role-Based Access Guards", fill="#475569", font=font_box_p, anchor="mm")
    
    draw.rounded_rectangle([(520, 460), (880, 650)], radius=10, fill="#FFFFFF", outline="#D97706", width=2)
    draw.text((700, 490), "Cloud Firestore (NoSQL DB)", fill="#D97706", font=font_box_h, anchor="mm")
    draw.text((700, 525), "• Document-based real-time data", fill="#475569", font=font_box_p, anchor="mm")
    draw.text((700, 555), "• 'complaints' collection (CRUD)", fill="#475569", font=font_box_p, anchor="mm")
    draw.text((700, 585), "• 'users' collection (Roles)", fill="#475569", font=font_box_p, anchor="mm")
    draw.text((700, 615), "• Auto-scaling & 99.99% availability", fill="#475569", font=font_box_p, anchor="mm")
    
    draw.rounded_rectangle([(920, 460), (1280, 650)], radius=10, fill="#FFFFFF", outline="#D97706", width=2)
    draw.text((1100, 490), "Firestore Security Rules", fill="#D97706", font=font_box_h, anchor="mm")
    draw.text((1100, 525), "• request.auth != null validation", fill="#475569", font=font_box_p, anchor="mm")
    draw.text((1100, 555), "• Student read/write isolation", fill="#475569", font=font_box_p, anchor="mm")
    draw.text((1100, 585), "• Admin-only status modification", fill="#475569", font=font_box_p, anchor="mm")
    draw.text((1100, 615), "• Role escalation prevention", fill="#475569", font=font_box_p, anchor="mm")
    
    # Directional Arrows
    # Client to Hosting
    draw.line([(300, 185), (300, 240), (390, 240), (390, 275)], fill="#1E40AF", width=3)
    draw.polygon([(385, 270), (395, 270), (390, 277)], fill="#1E40AF")
    
    draw.line([(1100, 185), (1100, 240), (1010, 240), (1010, 275)], fill="#1E40AF", width=3)
    draw.polygon([(1005, 270), (1015, 270), (1010, 277)], fill="#1E40AF")
    
    # Hosting to Backend
    draw.line([(390, 355), (390, 410), (300, 410), (300, 460)], fill="#059669", width=3)
    draw.polygon([(295, 455), (305, 455), (300, 462)], fill="#059669")
    
    draw.line([(700, 355), (700, 460)], fill="#059669", width=3)
    draw.polygon([(695, 455), (705, 455), (700, 462)], fill="#059669")
    
    draw.line([(1010, 355), (1010, 410), (1100, 410), (1100, 460)], fill="#059669", width=3)
    draw.polygon([(1095, 455), (1105, 455), (1100, 462)], fill="#059669")
    
    out_path = os.path.join(ASSETS_DIR, "architecture_diagram.png")
    img.save(out_path, quality=95)
    print("Saved:", out_path)

# -----------------------------------------------------------------------------
# 2. Data Flow Diagram (DFD)
# -----------------------------------------------------------------------------
def make_data_flow_diagram():
    W, H = 1400, 720
    img = Image.new("RGB", (W, H), "#FFFFFF")
    draw = ImageDraw.Draw(img)
    draw.rectangle([(2, 2), (W-3, H-3)], outline="#CBD5E1", width=2)
    
    font_title = get_font(26, bold=True)
    font_box_h = get_font(17, bold=True)
    font_box_p = get_font(13, bold=False)
    
    draw.text((W//2, 35), "ResolveIT: Data Flow Diagram (Level 1 Process Flow)", fill="#1E40AF", font=font_title, anchor="mm")
    
    # External Entities
    draw.rectangle([(50, 220), (220, 360)], fill="#DBEAFE", outline="#1E40AF", width=2)
    draw.text((135, 270), "STUDENT", fill="#1E40AF", font=font_box_h, anchor="mm")
    draw.text((135, 305), "(End User)", fill="#475569", font=font_box_p, anchor="mm")
    
    draw.rectangle([(1180, 220), (1350, 360)], fill="#FEF3C7", outline="#D97706", width=2)
    draw.text((1265, 270), "ADMINISTRATOR", fill="#B45309", font=font_box_h, anchor="mm")
    draw.text((1265, 305), "(Staff / Authority)", fill="#475569", font=font_box_p, anchor="mm")
    
    # Processes (Circles / Rounded Rectangles)
    processes = [
        ("1.0", "Authenticate User", 380, 160),
        ("2.0", "Lodge & Validate Complaint", 380, 360),
        ("3.0", "Query Personal Complaints", 380, 560),
        ("4.0", "Review & Filter Complaints", 820, 260),
        ("5.0", "Update Status & Resolution", 820, 460)
    ]
    
    for num, name, px, py in processes:
        draw.rounded_rectangle([(px-120, py-50), (px+120, py+50)], radius=20, fill="#F0FDF4", outline="#16A34A", width=2)
        draw.text((px, py-16), f"Process {num}", fill="#15803D", font=font_box_h, anchor="mm")
        draw.text((px, py+14), name, fill="#1F2937", font=font_box_p, anchor="mm")
        
    # Data Stores (Open-ended or Double line boxes)
    # D1: Users DB
    draw.line([(580, 120), (740, 120)], fill="#334155", width=3)
    draw.line([(580, 180), (740, 180)], fill="#334155", width=3)
    draw.text((660, 140), "D1 | Users Store", fill="#0F172A", font=font_box_h, anchor="mm")
    draw.text((660, 162), "(Firebase Auth / UID)", fill="#475569", font=font_box_p, anchor="mm")
    
    # D2: Complaints DB
    draw.line([(580, 400), (740, 400)], fill="#334155", width=3)
    draw.line([(580, 500), (740, 500)], fill="#334155", width=3)
    draw.text((660, 435), "D2 | Complaints Collection", fill="#0F172A", font=font_box_h, anchor="mm")
    draw.text((660, 465), "(Cloud Firestore)", fill="#475569", font=font_box_p, anchor="mm")
    
    # Connectors & Flow Labels
    # Student to P1
    draw.line([(220, 260), (300, 260), (300, 160), (380-120, 160)], fill="#1E40AF", width=2)
    draw.text((270, 145), "Credentials", fill="#1E40AF", font=font_box_p)
    
    # P1 to D1
    draw.line([(380+120, 150), (580, 150)], fill="#16A34A", width=2)
    draw.text((450, 135), "Verify User", fill="#16A34A", font=font_box_p)
    
    # Student to P2
    draw.line([(220, 310), (380-120, 330)], fill="#1E40AF", width=2)
    draw.text((240, 305), "Complaint Form Data", fill="#1E40AF", font=font_box_p)
    
    # P2 to D2
    draw.line([(380+120, 380), (500, 380), (500, 430), (580, 430)], fill="#16A34A", width=2)
    draw.text((430, 410), "Write Record", fill="#16A34A", font=font_box_p)
    
    # Student to P3
    draw.line([(135, 360), (135, 560), (380-120, 560)], fill="#1E40AF", width=2)
    draw.text((210, 540), "Fetch Status Request", fill="#1E40AF", font=font_box_p)
    
    # D2 to P3
    draw.line([(660, 500), (660, 560), (380+120, 560)], fill="#334155", width=2)
    draw.text((510, 540), "User Complaints", fill="#334155", font=font_box_p)
    
    # Admin to P4
    draw.line([(1180, 270), (820+120, 260)], fill="#D97706", width=2)
    draw.text((980, 245), "Filter / Search Query", fill="#D97706", font=font_box_p)
    
    # D2 to P4
    draw.line([(740, 430), (800, 430), (800, 310), (820, 310)], fill="#334155", width=2)
    draw.text((750, 350), "All Records", fill="#334155", font=font_box_p)
    
    # Admin to P5
    draw.line([(1180, 330), (1050, 330), (1050, 460), (820+120, 460)], fill="#D97706", width=2)
    draw.text((960, 440), "Status Update & Notes", fill="#D97706", font=font_box_p)
    
    # P5 to D2
    draw.line([(820-120, 460), (740, 460)], fill="#16A34A", width=2)
    draw.text((745, 475), "Update State", fill="#16A34A", font=font_box_p)
    
    out_path = os.path.join(ASSETS_DIR, "data_flow_diagram.png")
    img.save(out_path, quality=95)
    print("Saved:", out_path)

# -----------------------------------------------------------------------------
# 3. Use Case Diagram
# -----------------------------------------------------------------------------
def make_use_case_diagram():
    W, H = 1400, 750
    img = Image.new("RGB", (W, H), "#FFFFFF")
    draw = ImageDraw.Draw(img)
    draw.rectangle([(2, 2), (W-3, H-3)], outline="#CBD5E1", width=2)
    
    font_title = get_font(26, bold=True)
    font_actor = get_font(18, bold=True)
    font_uc = get_font(15, bold=False)
    
    draw.text((W//2, 35), "ResolveIT: System Use Case Diagram", fill="#1E40AF", font=font_title, anchor="mm")
    
    # System Boundary Box
    draw.rectangle([(320, 80), (1080, 710)], fill="#F8FAFC", outline="#3B82F6", width=2)
    draw.text((700, 105), "ResolveIT Web Application Boundary", fill="#1E40AF", font=get_font(16, bold=True), anchor="mm")
    
    # Actor 1: Student (Left)
    ax, ay = 150, 320
    # Head
    draw.ellipse([(ax-25, ay-70), (ax+25, ay-20)], fill="#DBEAFE", outline="#1E40AF", width=2)
    # Body
    draw.line([(ax, ay-20), (ax, ay+40)], fill="#1E40AF", width=3)
    # Arms
    draw.line([(ax-40, ay), (ax+40, ay)], fill="#1E40AF", width=3)
    # Legs
    draw.line([(ax, ay+40), (ax-30, ay+100)], fill="#1E40AF", width=3)
    draw.line([(ax, ay+40), (ax+30, ay+100)], fill="#1E40AF", width=3)
    draw.text((ax, ay+120), "Student", fill="#1E40AF", font=font_actor, anchor="mm")
    
    # Actor 2: Administrator (Right)
    bx, by = 1250, 320
    draw.ellipse([(bx-25, by-70), (bx+25, by-20)], fill="#FEF3C7", outline="#D97706", width=2)
    draw.line([(bx, by-20), (bx, by+40)], fill="#D97706", width=3)
    draw.line([(bx-40, by), (bx+40, by)], fill="#D97706", width=3)
    draw.line([(bx, by+40), (bx-30, by+100)], fill="#D97706", width=3)
    draw.line([(bx, by+40), (bx+30, by+100)], fill="#D97706", width=3)
    draw.text((bx, by+120), "Administrator", fill="#D97706", font=font_actor, anchor="mm")
    
    # Use Case Ellipses inside boundary
    use_cases = [
        ("Register & Login Account", 700, 160, ["student", "admin"]),
        ("Submit Facility Complaint", 700, 230, ["student"]),
        ("View Real-Time Statistics", 700, 300, ["student", "admin"]),
        ("Track Complaint Timeline", 700, 370, ["student"]),
        ("Search & Filter by Category/Status", 700, 440, ["student", "admin"]),
        ("View All College Complaints", 700, 510, ["admin"]),
        ("Update Status (In Progress/Resolved)", 700, 580, ["admin"]),
        ("Add Resolution Note & Priority", 700, 650, ["admin"])
    ]
    
    for text, cx, cy, actors in use_cases:
        draw.ellipse([(cx-190, cy-25), (cx+190, cy+25)], fill="#FFFFFF", outline="#1E40AF", width=2)
        draw.text((cx, cy), text, fill="#0F172A", font=font_uc, anchor="mm")
        
        if "student" in actors:
            draw.line([(ax+45, ay), (cx-190, cy)], fill="#3B82F6", width=2)
        if "admin" in actors:
            draw.line([(bx-45, by), (cx+190, cy)], fill="#F59E0B", width=2)
            
    out_path = os.path.join(ASSETS_DIR, "use_case_diagram.png")
    img.save(out_path, quality=95)
    print("Saved:", out_path)

# -----------------------------------------------------------------------------
# 4. Complaint Workflow Diagram
# -----------------------------------------------------------------------------
def make_complaint_workflow_diagram():
    W, H = 1400, 500
    img = Image.new("RGB", (W, H), "#FFFFFF")
    draw = ImageDraw.Draw(img)
    draw.rectangle([(2, 2), (W-3, H-3)], outline="#CBD5E1", width=2)
    
    font_title = get_font(26, bold=True)
    font_st_h = get_font(18, bold=True)
    font_st_p = get_font(13, bold=False)
    
    draw.text((W//2, 35), "ResolveIT: Complaint Lifecycle & State Transition Workflow", fill="#1E40AF", font=font_title, anchor="mm")
    
    states = [
        ("1. SUBMISSION", "Complaint Submitted", "• Form validated\n• Unique ID generated\n• Saved to Firestore", 80, 200, "#EFF6FF", "#3B82F6"),
        ("2. PENDING", "Pending Review", "• Visible to Admin\n• Placed in triage\n• Awaiting staff review", 400, 200, "#FEF3C7", "#D97706"),
        ("3. IN PROGRESS", "Action Underway", "• Facility staff dispatched\n• Priority assigned\n• Timeline updated", 720, 200, "#DBEAFE", "#2563EB"),
        ("4. RESOLVED", "Resolved & Closed", "• Maintenance verified\n• Resolution note logged\n• Student notified", 1040, 200, "#DCFCE7", "#16A34A")
    ]
    
    box_w, box_h = 280, 180
    
    for code, title, details, x, y, bg, border in states:
        draw.rounded_rectangle([(x, y), (x+box_w, y+box_h)], radius=12, fill=bg, outline=border, width=2)
        # Header banner
        draw.rounded_rectangle([(x, y), (x+box_w, y+45)], radius=12, fill=border)
        draw.rectangle([(x, y+30), (x+box_w, y+45)], fill=border)
        draw.text((x+box_w//2, y+22), code, fill="#FFFFFF", font=font_st_h, anchor="mm")
        
        draw.text((x+box_w//2, y+70), title, fill="#0F172A", font=get_font(16, bold=True), anchor="mm")
        
        # Details lines
        lines = details.split("\n")
        dy = y + 105
        for line in lines:
            draw.text((x+20, dy), line, fill="#334155", font=font_st_p)
            dy += 24
            
        # Arrow to next
        if x < 1000:
            ax1 = x + box_w + 5
            ax2 = x + box_w + 35
            ay = y + box_h//2
            draw.line([(ax1, ay), (ax2, ay)], fill="#1E40AF", width=4)
            draw.polygon([(ax2, ay-8), (ax2+12, ay), (ax2, ay+8)], fill="#1E40AF")
            
    # Rejection Branch (Alternative outcome from Pending)
    rx, ry = 560, 410
    draw.rounded_rectangle([(rx, ry), (rx+280, ry+70)], radius=10, fill="#FFE4E6", outline="#E11D48", width=2)
    draw.text((rx+140, ry+22), "Alternative: REJECTED", fill="#9F1239", font=get_font(15, bold=True), anchor="mm")
    draw.text((rx+140, ry+46), "Duplicate / Invalid inquiry with admin remarks", fill="#881337", font=font_st_p, anchor="mm")
    
    # Arrow from Pending down to Rejected
    draw.line([(540, 380), (540, 445), (rx, 445)], fill="#E11D48", width=2)
    draw.polygon([(rx-5, 440), (rx+5, 445), (rx-5, 450)], fill="#E11D48")
    
    out_path = os.path.join(ASSETS_DIR, "complaint_workflow_diagram.png")
    img.save(out_path, quality=95)
    print("Saved:", out_path)

if __name__ == "__main__":
    make_architecture_diagram()
    make_data_flow_diagram()
    make_use_case_diagram()
    make_complaint_workflow_diagram()
    print("All 4 system diagrams generated successfully!")
