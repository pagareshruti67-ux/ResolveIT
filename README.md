# ResolveIT — Cloud-Based Digital Complaint Management System

**A Complete, Functional, Beginner-Friendly Cloud Computing Mini-Project**  
Developed for: Third Year Computer Engineering (SPPU 2024 Pattern)  
Candidate: Shruti Pagare [Roll No: 24CO117]  
Department of Computer Engineering, AISSMS College of Engineering, Pune  

---

## 📌 1. Project Overview

**ResolveIT** is an institutional digital grievance redressal portal designed for college campuses. It allows students to lodge complaints regarding campus facilities (hostels, washrooms, electricity, water supply, classrooms, laboratories, Wi-Fi, library, transportation, and general inquiries) and track their resolution status in real-time. 

College facility administrators use an oversight control portal to review triage queues, assign maintenance priorities (Low, Medium, High), update lifecycle states, and publish official resolution notes.

---

## ☁️ 2. Cloud Computing Architecture & Technology Stack

The project adheres strictly to modern cloud computing paradigms by decoupling frontend edge hosting from serverless cloud database services:

* **Frontend Layer:** Semantic HTML5, Vanilla CSS3 (custom responsive design system), and modern ES6 JavaScript.
* **Cloud Authentication:** **Firebase Authentication** providing secure tokenized JWT sessions and email/password verification.
* **Cloud Database:** **Google Cloud Firestore**, a fully-managed serverless NoSQL document database offering sub-second queries and 99.99% availability.
* **Frontend Cloud Hosting Options:** 
  * **Microsoft Azure Static Web Apps** *(Recommended for easiest student setup)*
  * **AWS Amplify Hosting** *(Backed by Amazon CloudFront CDN and S3)*

```
[Student / Administrator] ➔ [Web Browser (Desktop / Mobile)]
                                        │
                                        ▼ HTTPS
             [Cloud-Hosted Frontend: AWS Amplify / Azure Static Web Apps]
                                        │
                    ┌───────────────────┴───────────────────┐
                    ▼                                       ▼
        [Firebase Authentication]               [Cloud Firestore Database]
         (JWT Session / Role Guard)             (Collections: users, complaints)
```

---

## 📂 3. Folder & File Structure

```text
ResolveIT_Complaint_Management_System/
│
├── index.html                                        # Public Landing Page & Feature Overview
├── login.html                                        # Student & Administrator Sign In / Registration
├── dashboard.html                                    # Student Dashboard, Form & Status Tracking Timeline
├── admin.html                                        # Facility Administrator Oversight & Resolution Portal
│
├── css/
│   └── style.css                                     # Responsive Institutional Design System & Badges
│
├── js/
│   ├── firebase-config.js                            # Firebase SDK Initialization & Cloud Provider
│   ├── auth.js                                       # Role Guards, JWT Session State, Demo Logins
│   └── app.js                                        # Complaint CRUD, Live Metrics, Filter & Timeline
│
├── assets/
│   ├── architecture_diagram.png                      # Decoupled 3-Tier Cloud Architecture Diagram
│   ├── data_flow_diagram.png                         # DFD Level 1 Process Flow Diagram
│   ├── use_case_diagram.png                          # System Use Case Diagram
│   └── complaint_workflow_diagram.png                # Lifecycle State Transition Diagram
│
├── firestore.rules                                   # Production Cloud Firestore Security Rules
├── README.md                                         # Complete Project Documentation & Deployment Guide
├── ResolveIT_Cloud_Computing_Mini_Project_Report.docx # Complete 35-Section Academic Project Report
├── ResolveIT_Cloud_Computing_Mini_Project_Report.pdf  # Publication-Ready Report PDF
├── ResolveIT_Cloud_Computing_Mini_Project_Presentation.pptx # 15-Slide Presentation with Speaker Notes
└── ResolveIT_Viva_and_Demo_Guide.docx                # 25+ Viva Q&A, Script & Demonstration Guide
```

---

## 🚀 4. How to Run Locally (Instant Setup)

The application requires **zero complex build tools, zero Node.js bundlers, and zero hardware**.

### Option A: Direct Browser Launch (Easiest)
1. Navigate to the project directory: `C:\Users\Shruti\ResolveIT_Complaint_Management_System\`
2. Double-click **`index.html`** to open it in Google Chrome, Microsoft Edge, or any modern browser.
3. The application runs immediately in **Dual-Mode**:
   * If Firebase credentials are not yet configured, the integrated **Local Cloud Simulator** activates automatically using browser storage pre-seeded with realistic college complaints.
   * You can immediately test student login, complaint lodging, tracking timeline, and administrator triage without needing API keys!

### Option B: Local Python Web Server
Open PowerShell in the project directory and run:
```powershell
python -m http.server 8000
```
Then navigate to: `http://localhost:8000` in your web browser.

---

## 🔥 5. Connecting to Live Google Firebase

To connect the application to your actual Google Cloud backend:

1. Go to the [Firebase Console](https://console.firebase.google.com/) and create a new project named `resolveit-cloud-system`.
2. Enable **Firebase Authentication**:
   * Navigate to **Build > Authentication > Sign-in method**.
   * Enable the **Email/Password** provider and save.
3. Enable **Cloud Firestore**:
   * Navigate to **Build > Firestore Database > Create database**.
   * Select a region (e.g. `asia-south1` or `us-central1`) and choose **Start in test mode**.
4. Register a Web App:
   * In Project Settings, click the Web icon (`</>`) to register your app.
   * Copy the `firebaseConfig` object.
5. Paste your keys into **`js/firebase-config.js`**:
   ```javascript
   const firebaseConfig = {
     apiKey: "YOUR_ACTUAL_API_KEY",
     authDomain: "YOUR_PROJECT_ID.firebaseapp.com",
     projectId: "YOUR_PROJECT_ID",
     storageBucket: "YOUR_PROJECT_ID.appspot.com",
     messagingSenderId: "YOUR_SENDER_ID",
     appId: "YOUR_APP_ID"
   };
   ```
6. Apply Cloud Security Rules:
   * Open the **Rules** tab in Cloud Firestore.
   * Copy the contents of [`firestore.rules`](file:///C:/Users/Shruti/ResolveIT_Complaint_Management_System/firestore.rules) and paste them into the editor.
   * Click **Publish**.

---

## 🛡️ 6. Documented Admin Role Configuration & Security

To prevent unauthorized users from elevating themselves to Administrator:
* Ordinary user registration strictly assigns `role: "student"`.
* The designated administrator accounts are restricted to institutional emails: `admin@college.edu` and `facilities@college.edu`.
* The server-side Firestore Security Rules validate that `request.resource.data.role == "student"` upon registration and block ordinary students from altering their role or viewing complaints submitted by other students.

---

## 🌐 7. Cloud Deployment: AWS vs Azure

### 🏆 Recommended Option: Microsoft Azure Static Web Apps (Easiest)
**Why Azure Static Web Apps is recommended for college mini-projects:**
* Generates an automated GitHub Actions CI/CD workflow with zero manual scripting.
* Completely free tier with SSL, global CDN distribution, and custom domains.
* Steps to Deploy:
  1. Initialize a git repository and push your project to GitHub:
     ```bash
     git init
     git add .
     git commit -m "Initial ResolveIT commit"
     git branch -M main
     git remote add origin https://github.com/YOUR_USERNAME/ResolveIT.git
     git push -u origin main
     ```
  2. Sign in to the [Azure Portal](https://portal.azure.com/).
  3. Search for **Static Web Apps** and click **Create**.
  4. Select your subscription, resource group, and choose the **Free Plan**.
  5. Sign in with GitHub and select your repository and `main` branch.
  6. Under **Build Presets**, select **Custom**, set App location to `/`, and leave Output location empty.
  7. Click **Review + Create**. Azure deploys the site in under 2 minutes and provides a live HTTPS URL!

### Alternative Option: AWS Amplify Hosting
1. Push project code to GitHub.
2. Sign in to the [AWS Management Console](https://console.aws.amazon.com/) and navigate to **AWS Amplify**.
3. Click **Host web app** and choose **GitHub**.
4. Select your repository and `main` branch.
5. In build settings, select static hosting (base directory: `./`).
6. Click **Save and deploy**. AWS Amplify builds the site, provisions CloudFront CDN, and outputs a live `.amplifyapp.com` domain.

---

## 🧪 8. Testing Instructions & Fast Viva Evaluation

For instant demonstration in front of an examination panel:
1. Open [`login.html`](file:///C:/Users/Shruti/ResolveIT_Complaint_Management_System/login.html).
2. Click **`👤 Student Demo`** for instant 1-click access as Shruti Pagare.
3. Click **`Lodge New Complaint`**, submit an issue, and watch the dynamic metrics counter increment.
4. Click **`Track Status`** to view the interactive 4-stage visual timeline.
5. Log out and click **`🛡️ Admin Demo`** to access the Facility Administrator portal.
6. Change the complaint status to **`In Progress`** or **`Resolved`**, add an administrative resolution note, and save.
7. Return to the student dashboard and confirm that the timeline and note update in real-time!

---

## 📄 9. Project Deliverables Summary

All generated project artifacts are located in:
`C:\Users\Shruti\ResolveIT_Complaint_Management_System\`
and mirrored on your Desktop at:
`C:\Users\Shruti\OneDrive\Desktop\ResolveIT_Complaint_Management_System\`

* 📘 **Project Report (Word):** [`ResolveIT_Cloud_Computing_Mini_Project_Report.docx`](file:///C:/Users/Shruti/ResolveIT_Complaint_Management_System/ResolveIT_Cloud_Computing_Mini_Project_Report.docx)
* 📕 **Project Report (PDF):** [`ResolveIT_Cloud_Computing_Mini_Project_Report.pdf`](file:///C:/Users/Shruti/ResolveIT_Complaint_Management_System/ResolveIT_Cloud_Computing_Mini_Project_Report.pdf)
* 📊 **Presentation (PowerPoint):** [`ResolveIT_Cloud_Computing_Mini_Project_Presentation.pptx`](file:///C:/Users/Shruti/ResolveIT_Complaint_Management_System/ResolveIT_Cloud_Computing_Mini_Project_Presentation.pptx)
* 📑 **Viva & Demo Guide (Word):** [`ResolveIT_Viva_and_Demo_Guide.docx`](file:///C:/Users/Shruti/ResolveIT_Complaint_Management_System/ResolveIT_Viva_and_Demo_Guide.docx)
* 🖼️ **Architecture Diagrams:** Located in the [`assets/`](file:///C:/Users/Shruti/ResolveIT_Complaint_Management_System/assets/) directory.
