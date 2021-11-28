from flask_restful import abort, Resource

from flask import jsonify, make_response

from models import Ticket, Comment, db
from models.ticket_states import Status, TicketException
from serializers import comment_to_ticket_post_args, ticketlist_post_args, ticketsingle_put_args
from cache import cache


class TicketSingle(Resource):
    def get(self, ticket_id):
        ticket = cache.get(str(ticket_id))
        if ticket is not None:
            return ticket
        else:
            ticket = Ticket.query.filter_by(id=ticket_id).one_or_none()
            if ticket is None:
                abort(404)
            response = jsonify(ticket.to_json())
            cache.set(str(ticket_id), response, timeout=30)
        return response

    def put(self, ticket_id):
        args = ticketsingle_put_args.parse_args()
        ticket = Ticket.query.filter_by(id=ticket_id).one_or_none()
        if ticket is None:
            abort(404)
        try:
            if args['status'] == Status.OPEN.value:
                ticket.set_open_status()
            elif args['status'] == Status.ANSWERED.value:
                ticket.set_answered_status()
            elif args['status'] == Status.WAIT_ANSWER.value:
                ticket.set_wait_status()
            elif args['status'] == Status.CLOSED.value:
                ticket.set_closed_status()
            else:
                abort(400)
        except TicketException as e:
            return make_response(jsonify({"Error": "Ошибка в переводе статуса"}), 400)
        else:
            db.session.commit()

            response = jsonify(ticket.to_json())
            cache.set(str(ticket_id), response, timeout=30)
            return response


class TicketList(Resource):
    def get(self):
        tickets = Ticket.query.all()
        if tickets:
            return jsonify([ticket.to_json() for ticket in tickets])
        return make_response(jsonify({"Error": "Нет записей"}), 404)

    def post(self):
        args = ticketlist_post_args.parse_args()
        new_ticket = Ticket(theme=args['theme'], text=args['text'], email=args['email'])
        db.session.add(new_ticket)
        db.session.commit()
        return make_response(jsonify(new_ticket.to_json()), 200)


class CommentToTicket(Resource):
    def post(self, ticket_id):
        args = comment_to_ticket_post_args.parse_args()
        ticket = Ticket.query.filter_by(id=ticket_id).one_or_none()
        if ticket is None:
            abort(404)
        if ticket.status == Status.CLOSED:
            return make_response(jsonify({"Error": 'Нельзя оставить комментарий к закрытому тикету'}), 400)
        new_comment = Comment(ticket_id=ticket.id, email=args['email'], text=args['text'])
        db.session.add(new_comment)
        db.session.commit()
        return make_response(jsonify(new_comment.to_json()), 200)
