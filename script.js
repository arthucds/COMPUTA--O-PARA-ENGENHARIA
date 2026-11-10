let leiturasConcluidas = 0;
const botaoConcluir = document.querySelector("#concluir-leitura");
const botaoReiniciar = document.querySelector("#reiniciar-leitura");
const total = document.querySelector("#total");

botaoConcluir.addEventListener("click", () => {
    leiturasConcluidas += 1;
    total.textContent = leiturasConcluidas;
});

botaoReiniciar.addEventListener("click", () => {
    leiturasConcluidas = 0;
    total.textContent = leiturasConcluidas;
});