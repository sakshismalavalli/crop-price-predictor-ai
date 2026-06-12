let history = [];

async function predictPrice() {
    try {
        const crop = document.getElementById("crop").value;

        const response = await fetch("/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ crop: crop })
        });

        const data = await response.json();

        document.getElementById("result").innerText =
            "Predicted Price: " + data.price;

        if (data.price > 50) {
            document.getElementById("recommendation").innerText =
                "Good market price, consider selling now";
        } else {
            document.getElementById("recommendation").innerText =
                "Price is moderate, you may wait for better rates";
        }

        history.push(data.price);

        document.getElementById("history").innerHTML =
            history.map(p => `<li>${p}</li>`).join("");

    } catch (error) {
        document.getElementById("result").innerText =
            "Server not running or error";

        console.log(error);
    }
}