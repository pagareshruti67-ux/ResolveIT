/**
 * ResolveIT: Digital Complaint Management System
 * Core Application Engine: CRUD, State, Filter, Search, and Timeline Tracking
 */

const SAMPLE_COMPLAINTS = [
  {
    id: "RES-2026-1042",
    title: "Wi-Fi Access Point Frequent Disconnection",
    category: "Internet and Wi-Fi",
    location: "Computer Lab 3, 2nd Floor",
    description: "The ceiling mounted access point frequently drops connections during practical lab hours.",
    status: "In Progress",
    priority: "High",
    submittedBy: "Shruti Pagare",
    studentUid: "student_117",
    date: "2026-10-24 10:15",
    resolutionNote: "IT Infrastructure team assigned. New replacement AP ordered.",
    updatedAt: "2026-10-25 14:30"
  },
  {
    id: "RES-2026-1043",
    title: "Projector Lamp Burnout in Classroom 204",
    category: "Classroom Facilities",
    location: "Main Academic Building, Room 204",
    description: "The overhead digital projector lamp is blinking red and failing to project lectures.",
    status: "Resolved",
    priority: "Medium",
    submittedBy: "Shruti Pagare",
    studentUid: "student_117",
    date: "2026-10-21 09:30",
    resolutionNote: "New 4000-lumen lamp bulb replaced and alignment calibrated by AV support.",
    updatedAt: "2026-10-22 11:20"
  },
  {
    id: "RES-2026-1044",
    title: "Water Cooler RO Purifier Maintenance",
    category: "Water Supply",
    location: "Hostel Block B, 1st Floor",
    description: "Water flow from the cooler is very slow and filter change indicator light is on.",
    status: "Pending",
    priority: "Low",
    submittedBy: "Rahul Verma",
    studentUid: "student_202",
    date: "2026-10-26 08:45",
    resolutionNote: "",
    updatedAt: "2026-10-26 08:45"
  },
  {
    id: "RES-2026-1045",
    title: "Flickering Tube Lights and Defective Switch",
    category: "Electricity",
    location: "Library Reading Hall, North Wing",
    description: "Two tube lights directly above study tables 12-14 are constantly flickering causing eye strain.",
    status: "In Progress",
    priority: "Medium",
    submittedBy: "Priyanka Gandhi",
    studentUid: "student_035",
    date: "2026-10-25 16:10",
    resolutionNote: "Campus electrician notified; scheduled for replacement this afternoon.",
    updatedAt: "2026-10-26 09:00"
  },
  {
    id: "RES-2026-1046",
    title: "Restroom Tap Leakage & Low Pressure",
    category: "Washroom and Cleanliness",
    location: "Ground Floor Boys Restroom, Dept of CE",
    description: "Continuous water dripping from the central handwash faucet wasting water.",
    status: "Resolved",
    priority: "Low",
    submittedBy: "Amit Deshmukh",
    studentUid: "student_508",
    date: "2026-10-20 11:00",
    resolutionNote: "Washer replaced and valve tightened by plumbing maintenance.",
    updatedAt: "2026-10-20 15:45"
  },
  {
    id: "RES-2026-1047",
    title: "Digital Oscilloscope Calibration Error",
    category: "Laboratory Equipment",
    location: "Hardware & Microprocessor Lab",
    description: "Bench unit #04 shows an offset voltage drift of +1.5V on Channel 1.",
    status: "Pending",
    priority: "High",
    submittedBy: "Shruti Pagare",
    studentUid: "student_117",
    date: "2026-10-26 14:10",
    resolutionNote: "",
    updatedAt: "2026-10-26 14:10"
  }
];

// Initialize Local Store if empty
function initStore() {
  if (!localStorage.getItem("resolveit_complaints")) {
    localStorage.setItem("resolveit_complaints", JSON.stringify(SAMPLE_COMPLAINTS));
  }
}
initStore();

// Fetch complaints from Firestore or Local Store
async function getComplaints(filterStudentUid = null) {
  if (window.ResolveIT.isCloudConnected()) {
    try {
      let query = window.ResolveIT.db.collection("complaints");
      if (filterStudentUid) {
        query = query.where("studentUid", "==", filterStudentUid);
      }
      const snapshot = await query.orderBy("date", "desc").get();
      const list = [];
      snapshot.forEach(doc => list.push(doc.data()));
      return list;
    } catch (err) {
      console.warn("Firestore query fallback:", err);
    }
  }

  // Local Store Fallback
  const all = JSON.parse(localStorage.getItem("resolveit_complaints") || "[]");
  if (filterStudentUid) {
    return all.filter(c => c.studentUid === filterStudentUid || c.studentUid === "student_117");
  }
  return all;
}

// Submit a new complaint
async function submitComplaint(data) {
  const user = window.AuthModule.getCurrentUser();
  const complaintId = "RES-2026-" + Math.floor(1000 + Math.random() * 9000);
  const now = new Date();
  const dateStr = now.toISOString().slice(0, 10) + " " + now.toTimeString().slice(0, 5);

  const newRecord = {
    id: complaintId,
    title: data.title.trim(),
    category: data.category,
    location: data.location.trim(),
    description: data.description.trim(),
    priority: data.priority || "Medium",
    status: "Pending",
    submittedBy: user ? user.name : "Anonymous Student",
    studentUid: user ? user.uid : "student_guest",
    date: dateStr,
    resolutionNote: "",
    updatedAt: dateStr
  };

  if (window.ResolveIT.isCloudConnected()) {
    try {
      await window.ResolveIT.db.collection("complaints").doc(complaintId).set(newRecord);
    } catch (err) {
      console.error("Firestore submit error:", err);
    }
  }

  // Always update local store
  const all = JSON.parse(localStorage.getItem("resolveit_complaints") || "[]");
  all.unshift(newRecord);
  localStorage.setItem("resolveit_complaints", JSON.stringify(all));

  return newRecord;
}

// Update status and resolution note (Admin feature)
async function updateComplaintStatus(complaintId, newStatus, resolutionNote = null, newPriority = null) {
  const all = JSON.parse(localStorage.getItem("resolveit_complaints") || "[]");
  const target = all.find(c => c.id === complaintId);

  if (!target) return { success: false, message: "Complaint not found" };

  target.status = newStatus;
  target.updatedAt = new Date().toISOString().slice(0, 10) + " " + new Date().toTimeString().slice(0, 5);
  if (resolutionNote !== null) target.resolutionNote = resolutionNote.trim();
  if (newPriority !== null) target.priority = newPriority;

  if (window.ResolveIT.isCloudConnected()) {
    try {
      const updateData = {
        status: target.status,
        updatedAt: target.updatedAt
      };
      if (resolutionNote !== null) updateData.resolutionNote = target.resolutionNote;
      if (newPriority !== null) updateData.priority = target.priority;
      await window.ResolveIT.db.collection("complaints").doc(complaintId).update(updateData);
    } catch (err) {
      console.error("Firestore update error:", err);
    }
  }

  localStorage.setItem("resolveit_complaints", JSON.stringify(all));
  return { success: true, updated: target };
}

// Calculate Statistics
function computeStats(complaints) {
  return {
    total: complaints.length,
    pending: complaints.filter(c => c.status === "Pending").length,
    progress: complaints.filter(c => c.status === "In Progress").length,
    resolved: complaints.filter(c => c.status === "Resolved").length
  };
}

// Toast helper
function showToast(message, type = "success") {
  let container = document.getElementById("toast-container");
  if (!container) {
    container = document.createElement("div");
    container.id = "toast-container";
    container.className = "toast-container";
    document.body.appendChild(container);
  }

  const toast = document.createElement("div");
  toast.className = `toast ${type}`;
  toast.innerHTML = `
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
      ${type === "success" 
        ? '<polyline points="20 6 9 17 4 12"></polyline>' 
        : '<circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line>'}
    </svg>
    <span>${message}</span>
  `;
  container.appendChild(toast);

  setTimeout(() => {
    toast.style.opacity = "0";
    setTimeout(() => toast.remove(), 300);
  }, 3500);
}

// Global UI Rendering Helpers
function renderTimeline(status) {
  const steps = [
    { label: "Submitted", code: "submitted" },
    { label: "Pending", code: "Pending" },
    { label: "In Progress", code: "In Progress" },
    { label: "Resolved", code: "Resolved" }
  ];

  if (status === "Rejected") {
    return `
      <div class="timeline">
        <div class="timeline-step completed">
          <div class="timeline-dot">✓</div>
          <div class="timeline-label">Submitted</div>
        </div>
        <div class="timeline-step rejected">
          <div class="timeline-dot">✕</div>
          <div class="timeline-label">Rejected</div>
        </div>
      </div>
    `;
  }

  let activeIndex = 0;
  if (status === "Pending") activeIndex = 1;
  else if (status === "In Progress") activeIndex = 2;
  else if (status === "Resolved") activeIndex = 3;

  let html = '<div class="timeline">';
  steps.forEach((step, idx) => {
    let stateClass = "";
    let icon = idx + 1;
    if (idx < activeIndex) {
      stateClass = "completed";
      icon = "✓";
    } else if (idx === activeIndex) {
      stateClass = "active";
    }
    html += `
      <div class="timeline-step ${stateClass}">
        <div class="timeline-dot">${icon}</div>
        <div class="timeline-label">${step.label}</div>
      </div>
    `;
  });
  html += '</div>';
  return html;
}

window.AppEngine = {
  getComplaints,
  submitComplaint,
  updateComplaintStatus,
  computeStats,
  showToast,
  renderTimeline
};
