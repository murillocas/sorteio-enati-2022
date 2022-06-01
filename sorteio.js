var links = ["teste2222.json","abertura.json","introducaoAoLatex.json","instalacaoDeSistemasOperacionais.json","entendendoGithub.json","amostraDeRobotica.json"]

function sortear(arquivo) {
    fetch(arquivo)
        .then(response => {
            return response.json();
        })
        .then(jsondata => {
            let aux = 0
            let test
            let terminar = -10
            for (aux; terminar < 0; aux++) {
                test = jsondata[aux]
                if (test == null) {
                    terminar = +10
                } else {
                    aux += 1
                }
            }
            console.log('teste')
            console.log(Math.floor(Math.random() * aux))
            console.log(aux - 1)
            let auxjson =
                console.log(jsondata[Math.floor(Math.random() * aux)].Nome)
        })
}

console.log(links)
function controlaSorteio(sala){
        sortear(links[sala])  
}
controlaSorteio(0)