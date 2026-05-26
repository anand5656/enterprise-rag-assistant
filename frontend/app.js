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


function addMessage(sender, text) {

    const msg =
        document.createElement("div");

    msg.classList.add("message");

    if (sender === "You") {

        msg.classList.add("user");

    } else {

        msg.classList.add("assistant");
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


/* CHAT FUNCTION */

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

            "https://enterprise-rag-assistant-2d7j.onrender.com/api/chat",

            {
                method: "POST",

                headers: {
                    "Content-Type":
                        "application/json"
                },

                body: JSON.stringify({

                    query: message
                })
            }
        );

        const data =
            await response.json();

        removeTyping();

        let responseText =
            data.answer;

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


/* FILE UPLOAD FUNCTION */

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

            "https://enterprise-rag-assistant-2d7j.onrender.com/api/upload",

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