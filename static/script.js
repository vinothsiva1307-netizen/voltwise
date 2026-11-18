
const vehicles = [
    { name: "Tata Tiago EV", type: "Hatchback", price: 8, range: 315 },
    { name: "MG Comet EV", type: "Hatchback", price: 7, range: 230 },
    { name: "Tata Punch EV", type: "SUV", price: 10, range: 421 },
    { name: "MG ZS EV", type: "SUV", price: 18, range: 461 }
];

function findEV() {
    const budget = Number(document.getElementById("budget").value);
    const type = document.getElementById("vehicleType").value;
    const results = document.getElementById("results");

    const matches = vehicles.filter(car =>
        car.price <= budget &&
        (type === "Any" || car.type === type)
    );

    if (matches.length === 0) {
        results.innerHTML = "<p>No matching EV found. Try another selection.</p>";
        return;
    }

    results.innerHTML = matches.map(car => `
        <div class="vehicle-card">
            <h3>${car.name}</h3>
            <p>Type: ${car.type}</p>
            <p>Approx. price: ₹${car.price} lakh</p>
            <p>Claimed range: ${car.range} km</p>
        </div>
    `).join("");
}

// VOLTWISE AI RECOMMENDATION ASSISTANT


// VOLTWISE CHATBOT CONNECTION

const startChatBtn = document.getElementById("startChatBtn");
const chatBox = document.getElementById("chatBox");
const chatInput = document.getElementById("chatInput");
const sendChatBtn = document.getElementById("sendChatBtn");
const chatMessages = document.getElementById("chatMessages");

startChatBtn.addEventListener("click", function () {
    chatBox.style.display = "block";
    startChatBtn.style.display = "none";

    addMessage("bot", "Hello! I'm VoltWise AI Assistant. Ask me about EVs!");
});

function addMessage(sender, message) {
    const messageElement = document.createElement("p");

    messageElement.textContent =
        (sender === "user" ? "You: " : "VoltWise: ") + message;

    chatMessages.appendChild(messageElement);
}

async function sendMessage() {
    const message = chatInput.value.trim();

    if (!message) return;

    addMessage("user", message);
    chatInput.value = "";

    try {
        const response = await fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message: message })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.reply || "Unable to get a response.");
        }

        addMessage("bot", data.reply);

    } catch (error) {
        addMessage("bot", "Sorry, something went wrong. Please try again.");
        console.error(error);
    }
}

sendChatBtn.addEventListener("click", sendMessage);

chatInput.addEventListener("keydown", function(event) {
    if (event.key === "Enter") {
        sendMessage();
    }
});

const compareBtn = document.getElementById("compareBtn");

compareBtn.addEventListener("click", function () {

    const firstEV = document.getElementById("ev1").value;
    const secondEV = document.getElementById("ev2").value;

    const evData = {
        "Tata Tiago EV": {
            price: 8,
            range: 315,
            type: "Hatchback"
        },

        "MG Comet EV": {
            price: 7,
            range: 230,
            type: "Hatchback"
        },

        "Tata Punch EV": {
            price: 10,
            range: 421,
            type: "SUV"
        },

        "MG ZS EV": {
            price: 18,
            range: 461,
            type: "SUV"
        }
    };

    const result = document.getElementById("comparisonResults");

    if (firstEV === secondEV) {
        result.innerHTML = "<p>Please select two different EVs.</p>";
        return;
    }

    const car1 = evData[firstEV];
    const car2 = evData[secondEV];

    result.innerHTML = `
        <h2>EV Comparison Results ⚡</h2>

        <table>
            <tr>
                <th>Features</th>
                <th>${firstEV}</th>
                <th>${secondEV}</th>
            </tr>

            <tr>
                <td>Price</td>
                <td>₹${car1.price} lakh</td>
                <td>₹${car2.price} lakh</td>
            </tr>

            <tr>
                <td>Range</td>
                <td>${car1.range} km</td>
                <td>${car2.range} km</td>
            </tr>

            <tr>
                <td>Vehicle Type</td>
                <td>${car1.type}</td>
                <td>${car2.type}</td>
            </tr>
        </table>
    `;
});



