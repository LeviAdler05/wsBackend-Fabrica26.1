# 🧪 Rickpedia - O Portal Completo para o Multiverso de Rick and Morty

[![Django](https://img.shields.io/badge/Django-5.1-092E20?style=for-the-badge&logo=django)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/DRF-3.15-A30000?style=for-the-badge&logo=django)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-336791?style=for-the-badge&logo=postgresql)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED?style=for-the-badge&logo=docker)](https://www.docker.com/)

Bem-vindo ao **Rickpedia**! Esta é uma aplicação web completa (Full Stack) que permite explorar o multiverso da série *Rick and Morty*. Você pode buscar personagens, favoritá-los, criar suas próprias listas personalizadas e gerenciar sua conta de forma segura.


## ✨ Funcionalidades do Projeto

### 👤 Autenticação de Usuários (Conta Própria)
*   **Cadastro:** Crie sua conta com usuário, e-mail e senha.
*   **Login Seguro:** Sistema baseado em Tokens (DRF Token Authentication).
*   **Área Restrita:** Apenas usuários logados podem favoritar e criar listas.

### 🧬 Exploração do Multiverso (API Rick and Morty)
*   **Lista Dinâmica:** Navegue por todos os personagens da série.
*   **Busca Inteligente:** Filtre personagens por **Nome** ou **Status** (Vivo, Morto, Desconhecido).
*   **Paginação:** Navegação fluida entre as centenas de personagens disponíveis.
*   **Cache Inteligente:** O sistema salva informações no banco de dados local para maior rapidez.

### 💖 Favoritos e Coleções Personalizadas (CRUD Completo)
*   **Favoritos:** Salve seus personagens prediletos com um clique.
*   **Minhas Listas:** Crie listas com nomes personalizados (Ex: "Ricks do Mal", "Alienígenas Estranhos").
*   **Gestão:** Adicione ou remova personagens de suas listas e exclua listas que não deseja mais.

### 🎨 Interface Profissional
*   Design moderno inspirado na série (Dark Mode).
*   Alertas visuais interativos (SweetAlert2).
*   Totalmente responsivo (funciona no celular e computador).

---

## 🚀 Como Rodar o Projeto

Existem duas formas de rodar o projeto. A mais fácil é usando o **Docker**.

### Opção 1: Usando Docker (Recomendado)
*O Docker configura tudo para você, inclusive o banco de dados.*

1.  **Baixe o código:**
    ```bash
    git clone https://github.com/LeviAdler05/wsBackend-Fabrica26.1
    cd wsBackend-Fabrica26.1
    ```
2.  **Inicie o sistema:**
    Certifique-se de que o Docker Desktop está aberto e rode:
    ```bash
    docker-compose up --build
    ```
3.  **Prepare o Banco de Dados:**
    Abra um novo terminal na mesma pasta e rode estes dois comandos:
    ```bash
    docker-compose exec web python manage.py migrate
    docker-compose exec web python manage.py createsuperuser
    ```
4.  **Acesse:** Abra o navegador em `http://localhost:8000`.

---

### Opção 2: Rodando Localmente (Sem Docker)
*Você precisará ter o Python instalado e um banco PostgreSQL rodando no seu PC.*

1.  **Crie um Ambiente Virtual:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate  # No Windows
    source venv/bin/activate # No Linux/Mac
    ```
2.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Configure o Banco de Dados:**
    Crie um arquivo chamado `.env` na raiz do projeto e coloque as informações do seu banco:
    ```env
    SECRET_KEY=sua_chave_secreta
    DEBUG=True
    DB_NAME=rickpedia
    DB_USER=seu_usuario_postgres
    DB_PASSWORD=sua_senha_postgres
    DB_HOST=localhost
    ```
4.  **Migrações e Servidor:**
    ```bash
    cd src
    python manage.py migrate
    python manage.py runserver
    ```
5.  **Acesse:** `http://127.0.0.1:8000`.

---

## 🛠️ Tecnologias Utilizadas

*   **Backend:** Python 3.11+, Django 5.1, Django REST Framework.
*   **Segurança:** Configuração de `DEFAULT_AUTHENTICATION_CLASSES` para suportar `TokenAuthentication`.
*   **Banco de Dados:** PostgreSQL 15.
*   **Frontend:** HTML5, CSS3, JavaScript (Vanilla), Bootstrap 5, FontAwesome, SweetAlert2.
*   **Documentação:** Swagger (drf-yasg).
*   **Integração:** Rick and Morty API Oficial.

---

## 📖 Endpoints Importantes (Para Desenvolvedores)

*   **Página Inicial:** `/`
*   **API de Personagens:** `/api/characters/`
*   **API de Favoritos:** `/api/lists/favorites/`
*   **API de Listas:** `/api/lists/`
*   **Swagger (Documentação):** `/swagger/`

---

## 📝 Autor

Desenvolvido por **Levi Adler** - [GitHub](https://github.com/LeviAdler05)
