const queryString = window.location.search;
const urlParams = new URLSearchParams(queryString);
const sala = urlParams.get('id');



var links = ["abertura.json","introducaoAoLatex.json","instalacaoDeSistemasOperacionais.json","entendendoGithub.json","amostraDeRobotica.json","introducaoaNodeJS.json","comoMelhorarSeuNegocio.json","fotografiaAudioVisual.json","hospedagemDeSite.json","recomendaçãoDeMusica.json","games.json","porqueFazerCursoDeComputacao.json"] 

var nomelinks = ["Abertura" ,"Introdução ao Latex","Instalação de sistemas Operacionais","Entendendo GitHub","Mostra de robótica","Introdução a Node.JS","Como melhorar seu negócio utilizando redes sociais","Fotografia Audiovisual \"A importância do Olhar na Construção de Narrativas\" ","Hospedagem de sites utilizando Amazon AWS S3","Recomendação de música considerando o estado emocional do usuário","Mundo dos Games","Por que fazer um curso de Computação?"]
const nomeGanhador = document.getElementById('nome-ganhador');
const botaoSorteio = document.getElementById('sortear');
const emailGanhador = document.getElementById('email');
const nomecurso = document.getElementById('nome-curso');




var nome = "";
var email = "";

nomeGanhador.innerHTML = "Selecione um curso acima para sortear!";

if(sala != null){
    nomecurso.innerHTML = nomelinks[sala];
}


botaoSorteio.addEventListener('click',()=>{

    sortear(links[sala])
    

})

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
           // console.log('teste')
           // console.log(Math.floor(Math.random() * aux))
           // console.log(aux - 1)
            //let auxjson = console.log(jsondata[Math.floor(Math.random() * aux)].Nome)
            
        let indicGanhador = Math.floor(Math.random() * aux);
          nome = JSON.stringify( jsondata[indicGanhador].Nome);

          email =JSON.stringify( jsondata[indicGanhador]["E-mail"]);

          nomeGanhador.innerHTML = nome;
          emailGanhador.innerHTML = email;
            
        
           
        })

       
}

//console.log(nome)


//console.log(links)
//function controlaSorteio(sala){
 //       console.log(sortear(links[sala]) )
//}


