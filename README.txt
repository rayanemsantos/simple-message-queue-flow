# Aplicação funciona como producer e consumer
# Utilizando activemq

# Exemplo

curl --location --request POST 'http://127.0.0.1:5000/api/v1/order' \
--header 'Content-Type: application/json' \
--data-raw '{
    "code": 1,
    "value": 35,
    "email": "rayanemsantos.contato@gmail.com"
}'