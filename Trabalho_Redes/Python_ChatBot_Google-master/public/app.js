const submitButton = document.getElementById('submitButton');
const chatbotInput = document.getElementById('chatbotInput');
const chatbotOutput = document.getElementById('chatbotOutput');

submitButton.onclick = userSubmitEventHandler;
chatbotInput.onkeyup = userSubmitEventHandler;

/*
    Definir evento click
 */
function userSubmitEventHandler(event) {
    if (
        (event.keyCode && event.keyCode === 13) ||
        event.type === 'click'
    ) {
        chatbotOutput.innerText = 'HMM..Pensando ...';
        askChatBot(chatbotInput.value);
    }
}

/*
    envia requisicao com a informacao pesquisada no body
 */
function askChatBot(userInput) {
    const myRequest = new Request('/', {
        method: 'POST',
        body: userInput
    });


    /*
    funcao para tratar erro
 */
    fetch(myRequest).then(function(response) {
        if (!response.ok) {
            throw new Error('erro http = ' + response.status);
        } else {
            return response.text();
        }
    }).then(function(text) {
        chatbotInput.value = '';
        chatbotOutput.innerText = text;
    }).catch((err) => {
        console.error(err);
    });
}
