function attachEvents() {
    const messagesField = document.getElementById('messages');
    const [nameField, newMessageField, sendBtn, refreshBtn] = document.querySelectorAll('#controls input');
    const BASE_URL = 'http://localhost:3030/jsonstore/messenger/'
    
    sendBtn.addEventListener('click', newMessage);
    refreshBtn.addEventListener('click', getMessages)

    function newMessage() {
        const author = nameField.value;
        const message = newMessageField.value;
        const newMessage = { author: author, content: message}
        fetch(`${BASE_URL}`, {
            method: 'POST',
            headers: {"content-type": "application/json"},
            body: JSON.stringify(newMessage)
        })
        .then(res => res.json())
        .then(() => getMessages())
        .catch(err => console.error(err))
    }

    function getMessages() {
        fetch(BASE_URL)
        .then(res => res.json())
        .then(messages => handleMessages(messages))
        .catch(err => console.log(err))
    }

    function handleMessages(messages) {
        nameField.value = '';
        newMessageField.value = '';
        let messagesArr = [];
        Object.values(messages).forEach(message => {
            messagesArr.push(`${message.author}: ${message.content}`);
        })
        messagesField.textContent = messagesArr.join('\n')
    }
}

attachEvents();