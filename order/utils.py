import json
import stomp
import datetime
from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['MAIL_SERVER']= 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'rayanesantostestes@gmail.com'
app.config['MAIL_PASSWORD'] = 'etipuscscclhvoim'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)

class EmailSender:

    def send(self, data):
        date = datetime.datetime.now() + datetime.timedelta(days=10)
        date = date.strftime('%d/%m/%Y')
        body = "O pedido #{} com o total de R${} foi cadastrado com sucesso. O prazo de entrega será até {}.".format(data['code'], data['value'], date)    
        msg = Message("Novo pedido!", sender='no-reply@gmail.com', recipients=[data['email']])
        msg.body = body
        with app.app_context():
            mail.send(msg)       

class Listener(stomp.ConnectionListener):

    def on_message(self, frame):
        es = EmailSender()
        print('Mensagem recebida "%s"' % frame.body)
        es.send(json.loads(frame.body))

class ActiveMQ:

    def __init__(self) -> None:
        self.conn = stomp.Connection()
        self.conn.set_listener('', Listener())
        self.conn.connect('admin', 'admin', wait=True)
        self.receive()
    
    # producer
    def send(self, data, queue='/queue/order'):
        self.conn.send(body=json.dumps(data), destination=queue)   
        print('Mensagem enviada')
        self.conn.disconnect()
    
    # consumer
    def receive(self, queue='/queue/order'):
        self.conn.subscribe(queue, id=1, ack='auto')