/**
 * ResolveIT: Digital Complaint Management System
 * Authentication & Role Management Module
 */

const ADMIN_EMAILS = ["admin@college.edu", "facilities@college.edu"];

// Retrieve current logged in user
function getCurrentUser() {
  const userJson = localStorage.getItem("resolveit_user");
  return userJson ? JSON.parse(userJson) : null;
}

// Check role guards
function checkPageAccess(requiredRole) {
  const user = getCurrentUser();
  const currentPath = window.location.pathname;

  if (!user) {
    if (currentPath.includes("dashboard.html") || currentPath.includes("admin.html")) {
      window.location.href = "login.html";
    }
    return;
  }

  // Update UI user name if available
  const userNameEl = document.getElementById("nav-user-name");
  const userBadgeEl = document.getElementById("nav-user-badge");
  if (userNameEl) userNameEl.textContent = user.name || user.email;
  if (userBadgeEl) {
    userBadgeEl.textContent = user.role.toUpperCase();
    userBadgeEl.className = `user-badge ${user.role}`;
  }

  if (requiredRole && user.role !== requiredRole) {
    if (requiredRole === "admin") {
      alert("Access Denied: Administrator privileges required.");
      window.location.href = "dashboard.html";
    } else if (requiredRole === "student" && user.role === "admin") {
      // Admin can view dashboard or redirect to admin portal
    }
  }
}

// Register Student
async function registerUser(name, email, password, department) {
  if (window.ResolveIT.isCloudConnected()) {
    try {
      const cred = await window.ResolveIT.auth.createUserWithEmailAndPassword(email, password);
      const uid = cred.user.uid;
      const userData = {
        uid: uid,
        name: name,
        email: email,
        department: department,
        role: "student",
        createdAt: new Date().toISOString()
      };
      await window.ResolveIT.db.collection("users").doc(uid).set(userData);
      localStorage.setItem("resolveit_user", JSON.stringify(userData));
      return { success: true, user: userData };
    } catch (err) {
      return { success: false, message: err.message };
    }
  } else {
    // Local Simulator
    const userData = {
      uid: "usr_" + Math.random().toString(36).substr(2, 9),
      name: name,
      email: email,
      department: department,
      role: ADMIN_EMAILS.includes(email.toLowerCase()) ? "admin" : "student",
      createdAt: new Date().toISOString()
    };
    localStorage.setItem("resolveit_user", JSON.stringify(userData));
    return { success: true, user: userData };
  }
}

// Login
async function loginUser(email, password) {
  if (window.ResolveIT.isCloudConnected()) {
    try {
      const cred = await window.ResolveIT.auth.signInWithEmailAndPassword(email, password);
      const uid = cred.user.uid;
      const doc = await window.ResolveIT.db.collection("users").doc(uid).get();
      let userData = doc.exists ? doc.data() : { uid: uid, email: email, role: "student" };
      if (ADMIN_EMAILS.includes(email.toLowerCase())) {
        userData.role = "admin";
      }
      localStorage.setItem("resolveit_user", JSON.stringify(userData));
      return { success: true, user: userData };
    } catch (err) {
      return { success: false, message: err.message };
    }
  } else {
    // Local Simulator
    const isAdmin = ADMIN_EMAILS.includes(email.toLowerCase()) || email.startsWith("admin");
    const userData = {
      uid: isAdmin ? "admin_001" : "student_117",
      name: isAdmin ? "Campus Facility Admin" : (email.split("@")[0].toUpperCase() || "Shruti Pagare"),
      email: email,
      department: isAdmin ? "Facility Management" : "Computer Engineering",
      role: isAdmin ? "admin" : "student"
    };
    localStorage.setItem("resolveit_user", JSON.stringify(userData));
    return { success: true, user: userData };
  }
}

// Quick Demo Logins for Viva
function quickLogin(type) {
  if (type === "student") {
    loginUser("shruti.pagare@college.edu", "student123").then(() => {
      window.location.href = "dashboard.html";
    });
  } else if (type === "admin") {
    loginUser("admin@college.edu", "admin123").then(() => {
      window.location.href = "admin.html";
    });
  }
}

// Logout
function logoutUser() {
  if (window.ResolveIT.isCloudConnected()) {
    window.ResolveIT.auth.signOut().then(() => {
      localStorage.removeItem("resolveit_user");
      window.location.href = "login.html";
    });
  } else {
    localStorage.removeItem("resolveit_user");
    window.location.href = "login.html";
  }
}

// Expose globally
window.AuthModule = {
  getCurrentUser,
  checkPageAccess,
  registerUser,
  loginUser,
  quickLogin,
  logoutUser
};
