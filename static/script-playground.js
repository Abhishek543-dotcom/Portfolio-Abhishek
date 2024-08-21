  function sendMessage() {
        const userInput = document.getElementById('userInput').value;
        fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: userInput }),
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('chatResponses').innerHTML += '<p>' + data.response + '</p>';
        });
    }