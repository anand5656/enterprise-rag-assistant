const chatBox =
    document.getElementById("chat-box");


function getTime() {

    return new Date().toLocaleTimeString(
        [],
        {
            hour: "2-digit",
            minute: "2-digit"
        }
    );
}


function addMessage(
    sender,
    text
) {

    const msg =
        document.createElement("div");

    msg.classList.add(
        "message"
    );

    if (sender === "You") {

        msg.classList.add(
            "user"
        );

    } else {

        msg.classList.add(
            "assistant"
        );
    }

    msg.innerHTML = `
        <strong>${sender}:</strong><br>
        ${text}

        <div class="timestamp">
            ${getTime()}
        </div>
    `;

    chatBox.appendChild(msg);

    chatBox.scrollTop =
        chatBox.scrollHeight;
}


function showTyping() {

    const typing =
        document.createElement("div");

    typing.id = "typing";

    typing.classList.add(
        "message",
        "assistant"
    );

    typing.innerHTML = `
        <strong>Assistant:</strong>

        <div class="typing">
            <span></span>
            <span></span>
            <span></span>
        </div>
    `;

    chatBox.appendChild(typing);

    chatBox.scrollTop =
        chatBox.scrollHeight;
}


function removeTyping() {

    const typing =
        document.getElementById("typing");

    if (typing) {

        typing.remove();
    }
}


async function sendMessage() {

    const input =
        document.getElementById("message");

    const message =
        input.value.trim();

    if (!message) return;

    addMessage(
        "You",
        message
    );

    input.value = "";

    showTyping();

    try {

        const response = await fetch(

            "http://127.0.0.1:8000/api/chat",

            {
                method: "POST",

                headers: {
                    "Content-Type":
                        "application/json"
                },

                body: JSON.stringify({

                    sessionId: "abc123",

                    message: message
                })
            }
        );

        const data =
            await response.json();

        removeTyping();

        let responseText =
            data.reply;

        if (
            data.sources &&
            data.sources.length > 0
        ) {

            responseText +=
                "<br><br><strong>Sources:</strong><br>";

            data.sources.forEach(source => {

                responseText +=
                    `• ${source}<br>`;
            });
        }

        addMessage(
            "Assistant",
            responseText
        );

    } catch (error) {

        removeTyping();

        addMessage(
            "Assistant",
            "Error connecting to backend."
        );

        console.error(error);
    }
}


async function uploadFile() {

    const fileInput =
        document.getElementById("fileInput");

    const file =
        fileInput.files[0];

    if (!file) {

        alert(
            "Please select a file"
        );

        return;
    }

    const formData =
        new FormData();

    formData.append(
        "file",
        file
    );

    try {

        addMessage(
            "Assistant",
            `Uploading ${file.name}...`
        );

        const response = await fetch(

            "http://127.0.0.1:8000/api/upload",

            {
                method: "POST",
                body: formData
            }
        );

        const data =
            await response.json();

        addMessage(
            "Assistant",
            `📄 ${data.message}`
        );

    } catch (error) {

        addMessage(
            "Assistant",
            "File upload failed."
        );

        console.error(error);
    }
}


/* CLEAR CHAT */

document
    .getElementById("clear-btn")
    .addEventListener(
        "click",
        () => {

            chatBox.innerHTML = "";
        }
    );


/* ENTER KEY SUPPORT */

document
    .getElementById("message")
    .addEventListener(
        "keypress",
        function(event) {

            if (event.key === "Enter") {

                sendMessage();
            }
        }
    );