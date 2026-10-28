/**
 * ResolveIT: Digital Complaint Management System
 * Firebase Cloud Configuration & Data Storage Provider
 * 
 * Instructions:
 * Replace the placeholder credentials below with your own Firebase Project settings
 * obtained from the Firebase Console (https://console.firebase.google.com).
 */

const firebaseConfig = {
  apiKey: "AIzaSy_YOUR_FIREBASE_API_KEY_HERE",
  authDomain: "resolveit-cloud-system.firebaseapp.com",
  projectId: "resolveit-cloud-system",
  storageBucket: "resolveit-cloud-system.appspot.com",
  messagingSenderId: "123456789012",
  appId: "1:123456789012:web:abcdef123456789"
};

// Check if developer has replaced default placeholder keys
const isFirebaseConfigured = () => {
  return (
    firebaseConfig.apiKey &&
    !firebaseConfig.apiKey.includes("YOUR_FIREBASE_API_KEY") &&
    typeof firebase !== "undefined"
  );
};

let db = null;
let auth = null;

if (isFirebaseConfigured()) {
  try {
    firebase.initializeApp(firebaseConfig);
    auth = firebase.auth();
    db = firebase.firestore();
    console.log("[ResolveIT Cloud] Connected to Live Firebase Cloud Services.");
  } catch (err) {
    console.error("[ResolveIT Cloud] Firebase initialization error:", err);
  }
} else {
  console.info(
    "[ResolveIT Cloud] Running in Local Cloud Simulator Mode. " +
    "To connect to live Google Cloud Firestore, provide your Firebase keys in js/firebase-config.js."
  );
}

// Export global cloud handles
window.ResolveIT = {
  isCloudConnected: isFirebaseConfigured,
  auth: auth,
  db: db
};
