# Pedalavel

Pedalavel é um aplicativo para iOS que se propõe a gerar rotas de bicicleta até um destino escolhido pelo usuário, tendo como foco a segurança do ciclista.

### Como assim?

Hoje em dia nós já reconhecemos o ciclismo como uma alternativa mais sustentável para o transporte urbano, elevando seu status de esporte e lazer para um verdadeiro meio de transporte. Mas os ciclistas ainda enfrentam muitos desafios no dia-a-dia, o maior deles sendo a segurança no trânsito: ciclofaixas ainda estão apenas começando a surgir, e motoristas nem sempre respeitam quem está andando de bike. Isso é um problema que é ainda maior quando se quer fazer caminhos novos, em lugares diferentes. Foi pensando nisso que surgiu o app Pedalavel, que tem como objetivo gerar rotas seguras para ciclistas que querem ir de um ponto A a um ponto B.

### Como o Pedalavel funciona?

O Pedalavel usa a engine OSRM para gerar rotas seguras para ciclistas a partir de um perfil customizado, que se equilibra em cima de dois grandes pilares de informação: Em primeiro lugar, os dados abertos da cidade do Recife, com datasets sobre acidentes de trânsito, e posição de câmeras de monitoramento, que podem ser usados para criar um perfil de uma rua/avenida/etc como sendo segura ou não. Em segundo lugar está o engajamento da comunidade de ciclistas, que é uma comunidade muito interessada em ajudar uns aos outros, informar, e facilitar a entrada dos que se interessam em se tornar ciclistas; eles, após seguir uma certa rota, tem a possibilidade de dar algumas informações sobre o estado dessa rota, gerando assim informações mais subjetivas, e também mais atualizadas.

### Como o Pedalavel está organizado?

O app é dividido em duas partes, o front-end, que pode ser encontrado em [iillx/CodeCup2018](https://github.com/iillx/CodeCup18), e o back-end, que é formado pelos arquivos desse repositório.

#### Sobre o Back-End

O back-end pode ser dividido em dois pedaços: O préprocessamento dos dados coletados, através dos dados abertos do Recife e dos feedbacks de usuário, e a nossa versão da engine de roteamento OSRM. Os dados coletados são processados de forma a transformar diversas datapoints sobre trechos de rota, como a quantidade de acidentes ocorridos lá, em pesos customizados para o mapa OSM. Esses pesos, então, são usados para o desenvolvimento do modelo de mapa que será usado para gerar as rotas que se adequam ao nosso perfil. Isso é feito pela própria engine OSRM, usando o nosso perfil de ciclismo customizado.
