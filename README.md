![EACH-USP](./imagens/each.png)

# ACH2018 - PSGII

Este repositório faz parte do projeto de ACH2018,  funcionando em conjunto com o [review-classifier](https://github.com/mautoz/reviews-classifier) e [python-webhook](https://github.com/mautoz/python-webhook).
Algumas funcionalidades do projeto podem ou devem ser automatizadas. Os códigos para esses casos ficaram melhores em um repositório separado.


# Pré-requisitos e considerações iniciais

- Os scripts neste repositório foram executados no Ubuntu 18.04.5 LTS em que o 'cron' é instalado previamente.

- Python >= 3.7

# Instruções

1. As configurações deste repositório devem ser as últimas coisas feitas e necessitam alterar o cron da máquina. Logo, antes de iniciar, confira se ele já está instalado com o comando:
```
$ crontab -e
```

2. Fala um clone deste repositório em sua máquina e verifique com cuidado o endereço em que ficará, pois será necessário para alterar o cron. Na dúvida, utilize o comando:
```
$ pwd
/home/<caminho_da_maquina>/reviews-classifier
```

3. Configure o [run](run) com as informações do seu Postgres.

4. Copie e cole o caminho acima no [cron](crontab), por exemplo:
```
SCRAPER_PATH=/home/<caminho_da_maquina>/reviews-classifier
```

5. Considero que os scripts rodaram em uma máquina pessoal, por isso, verifique se o horário para rodar vc terá a máquina ligada. Deixei como exemplo às 10 e 22 horas! Se tudo estiver ok, é só salvar!

6. Se as configurações estiverem corretas, os script rodarão sozinho sempre que a máquina estiver ligada. Na pasta [exemplos](/exemplos) é possível ver alguns exemplos de arquivos logs de saída.


# Troubleshooting

- Pode ser que seja necessário instalar o cron! Optei por não indicar nenhum tutorial pois existem diversos disponíveis, escolha o que mais agradar!
- Em algumas máquinas, o Python roda como 'python3' no lugar de 'python'.
