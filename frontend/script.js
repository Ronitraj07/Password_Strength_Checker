// Import and initialize Vercel Web Analytics
import { inject } from '@vercel/analytics';

// Initialize analytics on page load
if (typeof window !== 'undefined') {
    inject();
}

// Expose checkPassword to global scope for HTML onclick handlers
window.checkPassword = async function checkPassword() {
    const password = document.getElementById("password").value;

    try {
        const response = await fetch("https://password-strength-checker-6o1x.onrender.com/check-password/", { 
            method: "POST",  
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ password: password }),
        });

        if (!response.ok) {
            throw new Error(`Server responded with an error! Status: ${response.status}`);
        }

        const data = await response.json();
        console.log("Response:", data);
        document.getElementById("result").innerText = `Strength: ${data.strength}`;
    } catch (error) {
        console.error("Error:", error);
        alert("Failed to fetch. Check backend status and CORS policy.");
    }
}
