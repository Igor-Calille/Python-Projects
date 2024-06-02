# Sistema de Gerenciamento de Locação de Veículos - README

## Introdução

Este documento fornece um guia passo a passo para configurar e executar o sistema de gerenciamento de locação de veículos. O sistema é um aplicativo web com funcionalidades CRUD, permitindo a gestão completa de veículos, locações e clientes.

## Passos para Configuração

### 1. Configurar o MySQL

Abra o MySQL e estabeleça uma conexão. Recomendamos criar uma nova conexão para evitar alterações no código. Utilize as seguintes informações de conexão:

```plaintext
host: '127.0.0.1'
user: 'root'
password: 'root'
database: 'sistema_locacao_veiculos'
```

### 2. Criar e Popular a Database

Utilize o código `./SQL/Criar Database.sql` para criar a database do sistema de locação de veículos. Em seguida, utilize o código `./SQL/Popular Database.sql` para popular a database com dados.

### 3. Instalar Docker

#### Tutorial Simples para Instalar Docker:

1. **Para Windows e Mac:**
   - Baixe o Docker Desktop do site oficial [Docker Desktop](https://www.docker.com/products/docker-desktop).
   - Execute o instalador e siga as instruções na tela.
   - Após a instalação, abra o Docker Desktop e certifique-se de que ele está em execução.

2. **Para Linux:**
   - Atualize o índice de pacotes:
     ```sh
     sudo apt-get update
     ```
   - Instale os pacotes necessários:
     ```sh
     sudo apt-get install \
       apt-transport-https \
       ca-certificates \
       curl \
       gnupg \
       lsb-release
     ```
   - Adicione a chave GPG oficial do Docker:
     ```sh
     curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
     ```
   - Configure o repositório estável:
     ```sh
     echo \
       "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
       $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
     ```
   - Instale o Docker Engine:
     ```sh
     sudo apt-get update
     sudo apt-get install docker-ce docker-ce-cli containerd.io
     ```
   - Verifique se o Docker está instalado corretamente:
     ```sh
     sudo docker run hello-world
     ```

### 4. Executar Docker Compose

Utilize a sua IDE de preferência e rode o seguinte comando dentro do diretório `./Sistema`:

```sh
docker-compose up --build
```

### 5. Acessar o Sistema

O Flask retornará a URL do aplicativo. Acesse a URL pelo terminal ou digite `localhost:5000` no seu navegador web.

### 6. Funcionalidades do Sistema

Agora você tem acesso ao sistema de locação de veículos com tela de login e três funcionalidades CRUD, cada uma com um relatório específico:

- **Gestão de Veículos:** Adicionar, visualizar, editar e excluir veículos.
- **Gestão de Locações:** Adicionar, visualizar, editar e excluir locações.
- **Gestão de Clientes:** Adicionar, visualizar, editar e excluir clientes.

## Conclusão

Siga os passos acima para configurar e executar o sistema de gerenciamento de locação de veículos. Caso tenha alguma dúvida ou problema durante o processo, mande mensagem pelo teams.