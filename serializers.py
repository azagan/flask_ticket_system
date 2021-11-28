from flask_restful import reqparse

ticketlist_post_args = reqparse.RequestParser()
ticketlist_post_args.add_argument('theme', type=str, help="Theme of the ticket", required=True)
ticketlist_post_args.add_argument('text', type=str, help="Text of the ticket", required=True)
ticketlist_post_args.add_argument('email', type=str, help="Email author of the ticket", required=True)

ticketsingle_put_args = reqparse.RequestParser()
ticketsingle_put_args.add_argument('status', type=int, help='Status of the ticket', required=True)

comment_to_ticket_post_args = reqparse.RequestParser()
comment_to_ticket_post_args.add_argument('email', type=str, help="Email author of the comment", required=True)
comment_to_ticket_post_args.add_argument('text', type=str, help="Text of the comment", required=True)