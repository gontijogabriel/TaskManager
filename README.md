# Tasks Manager

Este é um projeto de gerenciamento de tarefas criado com Django. Ele permite que os usuários criem, editem, filtrem e concluam tarefas, além de registrar o tempo de trabalho para cada tarefa.

- [Funcionalidades](#funcionalidades)
- [Modelos](#modelos)
  - [Task](#task)
  - [WorkTime](#worktime)
- [Instalação e Configuração](#instalação-e-configuração)
  - [Passos para Instalação](#passos-para-instalação)
- [URLs Principais](#urls-principais)
- [Templates](#templates)
- [Autenticação](#autenticação)
- [Filtros](#filtros)

## Funcionalidades

- CRUD e pesquisa de tarefas.
- Marcar tarefas como concluídas.
- Filtrar tarefas por status: pendente, finalizado ou todas.
- Registrar e listar horas trabalhadas em cada tarefa.
- Filtros para buscar tarefas e registros de trabalho.

## Modelos

### Task

O modelo `Task` representa uma tarefa e contém os seguintes campos:

- `user`: O usuário que criou a tarefa.
- `title`: Título da tarefa (máximo de 200 caracteres).
- `description`: Descrição detalhada da tarefa (máximo de 500 caracteres).
- `status`: Indica se a tarefa está concluída (booleano).
- `created_at`: Data e hora de criação da tarefa (herdado de `BaseModel`).

### WorkTime

O modelo `WorkTime` registra as horas de trabalho de um usuário em uma tarefa e contém:

- `user`: O usuário que registrou o tempo de trabalho.
- `task`: A tarefa relacionada ao registro de trabalho.
- `start_time`: Hora de início do trabalho.
- `end_time`: Hora de término do trabalho.
- `hours_worked`: Calculado automaticamente com base no `start_time` e `end_time`.
- `description`: Descrição do trabalho realizado.

## Instalação e Configuração

### Passos para Instalação
1. Clone este repositório:

   ```bash
   git clone https://github.com/gontijogabriel/TaskManager.git
   cd seu-repositorio
   ```

2. Crie e ative um ambiente virtual:

   ```bash
    - Linux
   python3 -m venv .venv
   source venv/bin/activate
   
    - Windows
   python -m venv .venv
   .venv\Scripts\activate.bat
   ```

3. Instale as dependências do projeto:

   ```bash
   pip install -r requirements.txt
   ```

4. Realize as migrações do banco de dados:

   ```bash
   python manage.py migrate
   ```

5. Faça o dump de usuários e task (caso queira alimentar o banco com alguns dados):

   ```bash
   python manage.py loaddata dump_db.json
   ```

6. Crie um superusuário para acessar o painel administrativo:

   ```bash
   python manage.py createsuperuser
   ```

7. Execute o servidor local:

   ```bash
   python manage.py runserver
   ```

## URLs Principais
- `/tasks/`: Lista de tarefas.
- `/tasks/create/`: Criação de novas tarefas.
- `/task/check/<id>/`: Concluir uma tarefa.
- `/worktime/`: Lista de horas trabalhadas.
- `/worktime/create/`: Registrar horas trabalhadas.

## Templates

- **Listagem de Tarefas**: Exibe as tarefas, permitindo filtrar por status (pendente, finalizado, todos) e registrar horas de trabalho.
- **Criação de Tarefas**: Formulário para criar uma nova tarefa.
- **Registro de Horas**: Modal para registrar horas trabalhadas em uma tarefa.
- **Login**: Página de login personalizada para autenticação de usuários.

## Autenticação

A autenticação é feita com o modelo de usuário padrão do Django. A página de login é acessível através de `/auth/login/`.

## Filtros

- Filtros para tarefas por título, usuário e período de tempo.
- Filtros para registros de horas trabalhadas por tarefa, usuário, descrição e período de tempo.