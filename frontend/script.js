const API_BASE_URL = "http://localhost:5000";

async function loadAccounts() {
    const accountsDiv = document.getElementById("accounts");
    accountsDiv.innerHTML = "Loading accounts...";

    try {
        const response = await fetch(`${API_BASE_URL}/accounts`);
        const accounts = await response.json();

        accountsDiv.innerHTML = "";

        accounts.forEach(account => {
            accountsDiv.innerHTML += `
                <div class="card">
                    <strong>${account.customer_name}</strong><br>
                    Balance: ₹${account.balance}
                </div>
            `;
        });
    } catch (error) {
        accountsDiv.innerHTML = "Error loading accounts.";
    }
}

async function askAI() {
    const message = document.getElementById("message").value;
    const aiResponseDiv = document.getElementById("aiResponse");

    aiResponseDiv.innerHTML = "AI is thinking...";

    try {
        const response = await fetch(`${API_BASE_URL}/ai-chat`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message })
        });

        const data = await response.json();

        aiResponseDiv.innerHTML = `
            <div class="card">
                ${data.response}
            </div>
        `;
    } catch (error) {
        aiResponseDiv.innerHTML = "Error connecting to AI service.";
    }
}