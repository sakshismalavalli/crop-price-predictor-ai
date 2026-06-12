let history = [];

async function showPrice() {

    let crop = document.getElementById("crop").value;

    try {

        let response = await fetch("http://127.0.0.1:5000/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                crop: crop
            })
        });

        let data = await response.json();

        if (data.error) {
            document.getElementById("result").innerText =
                "Error: " + data.error;
            return;
        }

        document.getElementById("result").innerText =
            "AI Price: ₹" + data.price;

        if (data.price > 100) {
            document.getElementById("recommendation").innerText =
                "Good market price. Consider selling now.";
        } else {
            document.getElementById("recommendation").innerText =
                "Price is moderate. You may wait for better rates.";
        }

        history.push(data.price);

        document.getElementById("history").innerHTML =
            history.map(price => `<li>₹${price}</li>`).join("");

    } catch (error) {

        document.getElementById("result").innerText =
            "Server not running or error";

        console.log(error);
    }
}