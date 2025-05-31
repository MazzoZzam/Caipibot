const chat = document.getElementById("chat");
const input = document.getElementById("mensagem");
const somEnvio = document.getElementById("som-envio");
const somResposta = document.getElementById("som-resposta");

function adicionarMensagem(texto, classe) {
  const div = document.createElement("div");
  div.className = `${classe} animar-mensagem`;

  if (classe === "bot") {
    let i = 0;
    let html = "";
    const typingInterval = setInterval(() => {
      if (i < texto.length) {
        const char = texto[i];
        html += char === "\n" ? "<br>" : char;
        div.innerHTML = html;
        chat.scrollTop = chat.scrollHeight;
        i++;
      } else {
        clearInterval(typingInterval);
      }
    }, 40);
  } else {
    div.innerText = texto;
  }

  chat.appendChild(div);
  chat.scrollTop = chat.scrollHeight;

  if (classe === "bot") somResposta.play();
  if (classe === "user") somEnvio.play();

  setTimeout(() => {
    div.classList.remove("animar-mensagem");
  }, 1000);
}

async function enviarMensagem() {
  const texto = input.value;
  if (!texto.trim()) return;

  adicionarMensagem(texto, "user");
  input.value = "";

  const digitando = document.createElement("div");
  digitando.className = "bot animar-mensagem";
  digitando.innerHTML =
    'CaipiBOT está digitando<span class="pontos">...</span>';
  chat.appendChild(digitando);
  chat.scrollTop = chat.scrollHeight;

  const tempoPensamento = Math.random() * (2500 - 1200) + 1200;

  try {
    const response = await fetch("/responder", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ mensagem: texto }),
    });

    const data = await response.json();
    setTimeout(() => {
      chat.removeChild(digitando);
      adicionarMensagem(data.resposta, "bot");
    }, tempoPensamento);
  } catch (error) {
    setTimeout(() => {
      chat.removeChild(digitando);
      adicionarMensagem(
        "Desculpe, não consegui me conectar. Mas posso te ajudar com vinhos, cervejas e destilados!",
        "bot"
      );
    }, tempoPensamento);
  }
}

input.addEventListener("keypress", function (e) {
  if (e.key === "Enter") {
    e.preventDefault();
    enviarMensagem();
  }
});

window.onload = () => {
  adicionarMensagem(
    "Olá! Eu sou o CaipiBOT 🍹<br>Para começarmos por favor informe seu nome",
    "bot"
  );
};
