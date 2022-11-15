# Agenda de pedidos

# Requerimientos
Docker

Docker-compose

# Instrucciones

###
    docker-compose build
    docker-compose up -d

Para ejecutar las pruebas unitarias se deben detener los contenedores para evitar conflictos de red.
###
    docker-compose stop
    docker-compose run web sh -c "python manage.py test"

# Nota

Para acceder al SO del contenedor de la aplicación.
###
    docker-compose exec web bash
