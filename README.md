# Sistema de Oficina Mecânica (Back-End)

API REST simples construída com **Django + Django REST Framework + MongoDB (Djongo)**.

## Funcionalidades
- Clientes
- Veículos
- Ordens de Serviço

## Como executar
```bash
git clone <repo>
cd oficina-mecanica

python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/Mac:
# source venv/bin/activate

pip install -r requirements.txt

python myproject/manage.py migrate
python myproject/manage.py runserver
```

## Endpoints
- `/clientes/`
- `/veiculos/`
- `/ordens/`
