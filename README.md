# Crocosphere

# Autores Pedro Antônio e Gustavo Lindenberg

https://github.com/P-ASilva/crocosphere

## Como instalar e executar
    - Instale o Python (https://www.python.org/) em sua máquina. O jogo foi desenvolvido especificamente para Windows, portanto não há garantia de que funcionará em outros sistemas operacionais.

    - Instale algum editor de texto/código, como o Visual Studio Code (https://code.visualstudio.com/).

    - Abra o Visual Studio Code, procure pela opção Clonar Repositório, e selecione Clonar da Internet. No campo, cole o seguinte link: https://github.com/P-ASilva/crocosphere

    - Escolha uma localização em sua máquina para salvar o repositório clonado.

    - Abra o terminal e digite o comando a seguir:
        pip install -r "requirements.txt"

    - No Visual Studio, abra o arquivo "main.py" dentro do repositório clonado para rodar o jogo.


## Como jogar
    História

    Você controla um crocodilo preso em uma bolha. Ninguém sabe como o pobrezinho acabou numa bolha de ar no espaço, mas não há tempo a perder.
    Nosso querido protagonista possui uma fome insaciável por alvos. Sim, alvos. Foi isso que eu disse. Ajude ele a ser feliz com sua comida favorita! Mas tome cuidado com os planetas.

    Objetivo
    Lançar a bolha e acertar o alvo para completar cada fase.

    O movimento da bolha é constante no espaço, mas é afetado pela gravidade dos planetas presentes em cada fase.

    Acertar um planeta ou sair da tela faz com que a bolha volte ao ponto inicial.

    Controles
    Mouse: clicar na direção de lançamento desejada. Quanto mais longe o mouse da bolha, mais rápido o lançamento.

# Modelo Físico :
    - Nosso modelo físico rebedeu diversos ajustes em relação ao demostrado em sala, principalmente noque se diz ao alcance e força das orbitas. Primeiramente, modificamos o alcance das orbitas para serem baseados na constante usada em seu calculo (Nome de variável " k "), de forma que o personamgem principal seja afetado por uma orbita mais fraca quando se encontrar a uma distancia menor que o raio do planeta multiplicado por 25 alvos de k, e uma orbita mais forte quando estiver tão próximo quanto o raio do planeta multiplicado por 250 alvos de k. o valor de k foi dobrado para planetas muito pequenos, para melhorar a jogabilidade.
    Referente ao calculo da aceleração gravitacional, utilizamos o modelo em sala ajustando k de acordo com a situação : a = (dp/d)*k/d**2, com o vetor a tendo a direção definada por um vetor normalizaddo, dado pela diferênça entre as posições dos objetos em questão e seu módulo multiplicado por k e dividido pelo quadrado da distância entre personagem e planeta, que é uma simplificação das leis da gravitação.
    - Nosso modelo físico rebedeu diversos ajustes em relação ao demostrado em sala, principalmente no que se diz ao alcance e força das orbitas. Primeiramente, modificamos o alcance das orbitas para serem baseados na constante usada em seu calculo (Nome de variável "k"), de forma que o personamgem principal seja afetado por uma orbita mais fraca quando se encontrar a uma distancia menor que o raio do planeta multiplicado por 25 alvos de k, e uma orbita mais forte quando estiver tão próximo quanto o raio do planeta multiplicado por 250 alvos de k. o valor de k foi dobrado para planetas muito pequenos, para melhorar a jogabilidade.
    Referente ao calculo da aceleração gravitacional, utilizamos o modelo em sala ajustando k de acordo com a situação: a = (dp/d)*k/d**2, com o vetor a tendo a direção definada por um vetor normalizaddo, dado pela diferênça entre as posições dos objetos em questão e seu módulo multiplicado por k e dividido pelo quadrado da distância entre personagem e planeta, que é uma simplificação das leis da gravitação.
