async function sendMessage() {
    const input = document.getElementById("user-input");
    const message = input.value;
    const formData = new FormData();
    formData.append("user_message", message);

    const response = await fetch("/chat", {
        method: "POST",
        body: formData
    });
    const data = await response.json();

    const chatBox = document.getElementById("chat-box");
    chatBox.innerHTML += `<p><strong>You:</strong> ${message}</p>`;
    chatBox.innerHTML += `<p><strong>Bot:</strong> ${data.answer}</p>`;

    input.value = "";
}
