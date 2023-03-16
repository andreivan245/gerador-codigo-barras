# Gerador de código de barras

## Gerador e leitor de código de barras feito em Python com banco de dados local em MySQL

## Bibliotecas Utilizadas

- barcode
- pyzbar
- mysql.connector

## Objetivos

O objetivo principal é a criação de um gerador e leitor de código de barras, onde um código é criado aleatoriamente ou de acordo com o usuário, esse código é armazenado em um banco de dados ao mesmo tempo em que se cria uma imagem em png desse código de barras que é armazenada localmente na pasta "produtos". Futuramente será adicionado a funcionalidade de ler um código pelo celular.

## Execução

Para a execução é necessário ter instalado o python juntamento com as bibliotecas listadas acima e em seguida executar o arquivo python "geradorCodigoBarras.py".

## Observações

Apesar de pedir apenas 12 números é gerado 13 números no código de barra no qual o 13 é um número de checagem dá biblioteca barcode uma vez que o formato escolhido é EAN13.
