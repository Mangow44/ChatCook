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
    let userBox = createBox(msg, "right", "user");
    dialog.appendChild(userBox);

    fetch("http://localhost:5005/webhooks/rest/webhook", {
        method: "POST",
        body: JSON.stringify({ message: msg }),
    })
        .then((response) => response.json())
        .then((data) => {
            data.forEach((message) => {
                if (message["text"])
                    dialog.appendChild(
                        createBox(message["text"], "left", "bot")
                    );
                if (message["image"]) {
                    let botBox = createBox("", "left", "bot");
                    botBox.removeChild(botBox.children[1]);
                    let img = document.createElement("img");
                    img.setAttribute("src", message["image"]);
                    img.setAttribute("alt", "image from rasa");
                    img.setAttribute("referrerpolicy", "no-referrer");
                    img.setAttribute("class", "box-img");
                    botBox.appendChild(img);
                    dialog.appendChild(botBox);
                }
            });

            dialog.scrollTop = dialog.scrollHeight;
        })
        .catch((error) => {
            botBox.children[1].style.color = "red";
            botBox.children[1].innerText = "I am afraid, an error occurred :/";
        });

    dialog.scrollTop = dialog.scrollHeight;
}

function createBox(msg, position, sender) {
    let box = document.createElement("div");
    box.setAttribute("class", `dialog-box ${position}`);
    let text = document.createElement("p");
    text.innerText = msg;
    if (sender === "bot") {
        let picture = document.createElement("img");
        picture.setAttribute("src", "./chatcookpic.png");
        picture.setAttribute("alt", "chatcook's picture");
        picture.setAttribute("class", "avatar");
        box.appendChild(picture);
    }
    box.appendChild(text);
    return box;
}
