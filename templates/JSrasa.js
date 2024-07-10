function sendMessage() {
            var userInput = document.getElementById("user-input").value;
            document.getElementById("user-input").value = "";

            fetch('/chatbot', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ message: userInput })
            })
            .then(response => response.json())
            .then(data => {
                var chatLog = document.getElementById("chat-log");
                chatLog.innerHTML += "<p><strong>User:</strong> " + userInput + "</p>";
                chatLog.innerHTML += "<p><strong>Chatbot:</strong> " + data[0].text + "</p>";
                chatLog.scrollTop = chatLog.scrollHeight;
            })
            .catch(error => {
                console.error('Error:', error);
            });
        }

        function toggleChat() {
            var chatContainer = document.getElementById("chat-container");
            var toggleButton = document.getElementById("toggle-chat");
            if (chatContainer.style.display === "none") {
                chatContainer.style.display = "flex";
                toggleButton.textContent = "-";
            } else {
                chatContainer.style.display = "none";
                toggleButton.textContent = "+";
            }
        }