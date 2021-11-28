from models import db
from flask_migrate import Migrate

from flask import Flask
from flask_restful import  Api
from views import TicketList, TicketSingle, CommentToTicket
from cache import cache

app = Flask(__name__)
app.config.from_object('config.BaseConfig')
api = Api(app)

db.init_app(app)
migrate = Migrate(app, db)

cache.init_app(app)

api.add_resource(TicketList, '/tickets')
api.add_resource(TicketSingle, '/tickets/<int:ticket_id>')
api.add_resource(CommentToTicket, '/comments/<int:ticket_id>')

if __name__ == '__main__':
    app.run(debug=True)
