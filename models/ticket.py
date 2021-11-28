from .database import db
import datetime
from .ticket_states import Status, OpenedStatus, ClosedStatus, WaitAnswerStatus, AnsweredStatus

class Ticket(db.Model):
    __tablename__ = "tickets"
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=datetime.datetime.now)
    updated = db.Column(db.DateTime, onupdate=datetime.datetime.now)
    theme = db.Column(db.String(250), nullable=False)
    text = db.Column(db.Text, nullable=False)
    email = db.Column(db.String(120), nullable=False)
    status = db.Column(db.Integer, nullable=False, default=0)

    def status_string(self):
        return str(self._get_state(self.status))
    
    def _get_state(self, status):
        states = {
            Status.OPEN.value: OpenedStatus(self),
            Status.ANSWERED.value: AnsweredStatus(self),
            Status.WAIT_ANSWER.value: WaitAnswerStatus(self),
            Status.CLOSED.value: ClosedStatus(self)
        }
        return states[status]
    
    def set_open_status(self):
        self._get_state(self.status).setOpen()
    
    def set_wait_status(self):
        self._get_state(self.status).setWait()
    
    def set_answered_status(self):
        self._get_state(self.status).setAnswered()
    
    def set_closed_status(self):
        self._get_state(self.status).setClosed()

    def to_json(self):
        return {
            "id": self.id,
            "created": self.created,
            "updated": self.updated,
            "theme": self.theme,
            "text": self.text,
            "email": self.email,
            "status": self.status_string()
        }


class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    ticket_id = db.Column(db.Integer, db.ForeignKey('tickets.id'), nullable=False)
    created = db.Column(db.DateTime, default=datetime.datetime.now)
    email = db.Column(db.String(120), nullable=False)
    text = db.Column(db.Text, nullable=False)

    def to_json(self):
        return {
            "id": self.id,
            "ticket_id": self.ticket_id,
            "created": self.created,
            "email": self.email,
            "text": self.text
        }