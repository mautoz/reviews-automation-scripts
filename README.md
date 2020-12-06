![EACH-USP](./imagens/each.png)

# ACH2018 - PSGII

Este repositório faz parte do projeto de ACH2018,  funcionando em conjunto com o [review-classifier](https://github.com/mautoz/reviews-classifier) e [python-webhook](https://github.com/mautoz/python-webhook).
Algumas funcionalidades do projeto podem ou devem ser automatizadas. Os códigos para esses casos ficaram melhores em um repositório separado.


# Pré-requisitos e considerações iniciais

- Os scripts neste repositório foram executados no Ubuntu 18.04.5 LTS em que o 'cron' é instalado previamente.

- Git
- Python >= 3.7
- Node >= 12.20.0

Bibliotecas:
- psycopg2 == 2.8.6
- Pandas == 1.1.4


# Instruções do Google Play API

O [Google Play API](https://github.com/facundoolano/google-play-api) é um repositório de uma API para coletar reviews do Google Play Store. Parte do projeto era automatizar a coleta e armazenamento dos dados através desta ferramenta. As instruções nesta seção são para isso!

1. As configurações deste repositório devem ser as últimas coisas feitas e necessitam alterar o cron da máquina. Logo, antes de iniciar, confira se ele já está instalado com o comando:
```
$ crontab -e
```

2. Faça um clone do repositório [Google Play API](https://github.com/facundoolano/google-play-api).

3. Faça um clone deste repositório.

4. Copie e cole o arquivo [start_google_api.py](./start_google_api.py) na raiz da pasta do repositório do item 2.

5. Utilize o pwd para pegar o caminho da pasta do item acima, por exemplo:
```
$ pwd
/home/<caminho_da_maquina>/google-play-api
```
Pegue esse caminho e cole no [run_google](run_google)

6. Agora é só alterar o crontab como no modelo: [cron](crontab). Por exemplo:
```
SCRAPER_PATH=/home/<caminho_da_maquina>/reviews-classifier
```
No cron sera chamado o [run_google](run_google). Lembre-se que o Google API deve ser programado para executar antes dos scrapers abaixo e precisa de Node.js.

# Instruções dos scrapers

1. Um clone deste repositório deve ter sido feito acima. Caso ainda não tenha sido feito, este é o momento! Verifique com cuidado o endereço em que ficará, pois será necessário para alterar o cron. Na dúvida, utilize o comando:
```
$ pwd
/home/<caminho_da_maquina>/reviews-classifier
```

2. Configure o [run](run) com as informações do seu Postgres.

3. Copie e cole o caminho acima no [cron](crontab), por exemplo:
```
SCRAPER_PATH=/home/<caminho_da_maquina>/reviews-classifier
```
Se você já fez isso na seção anterior, não precisa repetir.

4. Considero que os scripts serão rodados em uma máquina pessoal, por isso, verifique se no horário escolhido para rodar sua máquina estará ligada. Deixei como exemplo às 23:09 (depois de iniciado o Google API)! Se tudo estiver ok, é só salvar!

5. Se as configurações estiverem corretas, os script rodarão sozinho sempre que a máquina estiver ligada. Na pasta [exemplos](/exemplos) é possível ver alguns exemplos de arquivos logs de saída.

6. Para o _scraper_ de _reviews_ é necessário antes executar antes o [google_api_seach.py](./google_api_seach.py) que faz uma busca dos aplicaticos relacionados ao termo buscado e os salva em um '.csv' chamado [app_seach_results.csv](./app_seach_results.csv). Por exemplo, se você quiser buscar 'facebook' faça:
```
python3 google_api_aux.py --search "facebook"
```
Caso queira, pode preencher manualmente o csv tomando cuidado para não errar o appId e utilizando ';' como delimitador. O header foi retirado para não sobrescrever o csv, assim é possível buscar vários app e só dar append na lista que será coletada. 
Um exemplo está disponível em [app_seach_results.csv](/app_seach_results.csv).

7. O [scraper_google_reviews.py](./scraper_google_reviews.py) será responsável por ler o [app_seach_results.csv](./app_seach_results.csv) e coletar os reviews de todos os itens que estiver na lista. Dependendo do tamanho, o processo pode ser demorado.

# Troubleshooting

- Pode ser que seja necessário instalar o cron! Optei por não indicar nenhum tutorial pois existem diversos disponíveis, escolha o que mais agradar!
- Em algumas máquinas, o Python roda como 'python3' no lugar de 'python'.
