async function predictPrice() {
    const crop = document.getElementById("crop").value;

    const response = await fetch("/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ crop: crop })
    });

    const data = await response.json();

    if (data.error) {
        document.getElementById("result").innerText = data.error;
    } else {
        document.getElementById("result").innerText =
            "Predicted Price: " + data.price;
    }
}