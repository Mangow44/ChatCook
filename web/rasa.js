let status_circle = document.querySelector(".status-circle");
let input = document.querySelector(".chat-input");
let dialog = document.querySelector(".dialog");

input.focus();

fetch("http://localhost:5005/")
    .then((response) => response.text())
    .then(() => (status_circle.style.backgroundColor = "green"))
    .catch(() => (status_circle.style.backgroundColor = "red"));

window.addEventListener("keypress", (e) => {
    if (e.key === "Enter" && input.value != "") {
        sendMessage(input.value);
        input.value = "";
    }
});

function sendMessage(msg) {
    let userBox = createBox(msg, "right");
    dialog.appendChild(userBox);
    dialog.scrollTop = dialog.scrollHeight;

    fetch("http://localhost:5005/webhooks/rest/webhook", {
        method: "POST",
        body: JSON.stringify({ message: msg }),
    })
        .then((response) => response.json())
        .then((data) => {
            dialog.appendChild(createBox(data[0].text, "left"));
        })
        .catch((error) => {
            console.error("Error:", error);
        });
}

function createBox(msg, position) {
    let box = document.createElement("div");
    box.setAttribute("class", `dialog-box ${position}`);
    box.innerText = msg;
    return box;
}
