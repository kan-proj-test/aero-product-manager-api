# Aero Product Manager API

Este es el backend API para el sistema de gestión de productos aeroespaciales.

## Tecnologías utilizadas

- Python
- Flask
- SQLAlchemy
- Pytest
- Pytest-cov

## Estructura del proyecto

```
/
− src/
    �"H __init__.py
    − main.py
    − config.py
    − api/
    |   − __init__.py
    |   − routes.py
    |   − controllers/
    |       − __init__.py
    |       − product_controller.py
    − services/
    |   − __init__.py
    |   − product_service.py
    − models/
    |   − __init__.py
    |   − product.py
    − repositories/
        − __init__.py
        − product_repository.py
− tests/
    − __init__.py
    − test_api.py
    − test_services.py
    − test_models.py
− requirements.txt
‒ README.md
```

## Desarrollo y deployment

Para el desarrollo local, utiliza el siguiente comando:

```bash
pip install -r requirements.txt
flask run
```

Para el deployment en AWS Lambda, se utilizará el Serverless Framework. La configuración específica se encuentra en el archivo `serverless.yml`.

## Contribución

Si deseas contribuir al proyecto, por favor crea un pull request con tus cambios.