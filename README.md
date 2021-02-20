# generate-qrcode

Api para gerar qrcode em imagem png, a partir de qualquer dado.


## Instalação

* Clonar o projeto, e em seguida navegar até a pasta do projeto:
```
$ git clone https://github.com/rafaelo19/generate-qrcode.git

$ cd generate-qrcode
```

* Criando o ambiente:
```
$ docker-compose up -d --build
```

* Se necessário entrar no shell do container:
```
$ docker exec -it api-qrcode sh
```

## Rotas
| Url           | Metodo  |  Uso                              |
| :------------ |:--------| :---------------------------------|
| /generates    | POST    | Gerar qrcode a partir de um dado  |

## Dados para consumir rota
 - Request:
 <br> Os tipos de dados na propriedade ``data`` aceitos são string, int e float.</br>
 ```
    {
      "data": "https://google.com.br"
    }
```
- Response:
 <br> A informação da propriedade ``qrcode`` é base64 de uma imagem png.</br>
```
    {
      "qrcode": "iVBORw0KGgoAAAANSUhEUgAAAQgAAAEIAQAAAACLjVdSAAAA2klEQVR4nO3VYRbCMAgD4Nz/0ujaBOiceoCAzznp9yuvtIh/hREjRoz4LrDr/Xs10DqmgtGcqi+6ibV2/WFO6niLWIlRjxCIEXpypFrHUujErc/9xLUSVfuMubfcBBRavmrKXEUNkt60gRzF6mj3gBYVp51QNzIj3kWeAh+b5hw3O1HRcStFbiBLwfnJRbT8HIWAFM7o/ERkWllx3lFOQtVDchaVEb/MD66C0ewxwnE9ewrmxLB2fue1bCpyF8WI0BlDaSz0zHbLzVBwhnKUuOIqftaIESNGPNcLJpqxklu+2S0AAAAASUVORK5CYII="
    }
```
 
