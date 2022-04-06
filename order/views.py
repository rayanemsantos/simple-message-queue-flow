from flask_restful import Resource, request
from .utils import ActiveMQ

class Order(Resource):

    def post(self):
        data = request.get_json()
        _amq = ActiveMQ()
        _amq.send(data)        
        return {'message': 'Pedido registrado com sucesso!'}, 201, {'content-type': 'application/json'}