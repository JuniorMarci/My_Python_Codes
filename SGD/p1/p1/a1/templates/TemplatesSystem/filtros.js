function filtrarPorDuracao() {
    var tabela = document.getElementById("tabela-chamadas");
    var linhas = tabela.getElementsByTagName("tr");

    for (var i = 1; i < linhas.length; i++) {
        var colunaDuracao = linhas[i].getElementsByTagName("td")[2];
        var duracao = parseInt(colunaDuracao.textContent);

        if (duracao <= 25) {
            linhas[i].style.display = "none";
        } else {
            linhas[i].style.display = "";
        }
    }
}
