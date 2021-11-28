import enum


class Status(enum.Enum):
    OPEN = 0
    ANSWERED = 1
    WAIT_ANSWER = 2
    CLOSED = 3


class TicketException(Exception):
    pass


class OpenedStatus:
    def __init__(self, ticket) -> None:
        self.ticket = ticket

    def setOpen(self):
        raise TicketException("can't make open")

    def setAnswered(self):
        self.ticket.status = Status.ANSWERED.value

    def setClosed(self):
        self.ticket.status = Status.CLOSED.value

    def setWait(self):
        raise TicketException("can't make wait")

    def __str__(self) -> str:
        return "Открыт"


class AnsweredStatus:
    def __init__(self, ticket) -> None:
        self.ticket = ticket

    def setOpen(self):
        raise TicketException("can't make open")

    def setAnswered(self):
        raise TicketException("can't make answered")

    def setClosed(self):
        self.ticket.status = Status.CLOSED.value

    def setWait(self):
        self.ticket.status = Status.WAIT_ANSWER.value

    def __str__(self) -> str:
        return "Отвечен"


class WaitAnswerStatus:
    def __init__(self, ticket) -> None:
        self.ticket = ticket

    def setOpen(self):
        raise TicketException("can't make open")

    def setAnswered(self):
        raise TicketException("can't make answered")

    def setClosed(self):
        self.ticket.status = Status.CLOSED.value

    def setWait(self):
        raise TicketException("can't make wait")

    def __str__(self) -> str:
        return "Ожидает ответа"


class ClosedStatus:
    def __init__(self, ticket) -> None:
        self.ticket = ticket

    def setOpen(self):
        raise TicketException("can't make open")

    def setAnswered(self):
        raise TicketException("can't make answered")

    def setClosed(self):
        raise TicketException("can't make close")

    def setWait(self):
        raise TicketException("can't make wait")

    def __str__(self) -> str:
        return "Закрыт"
