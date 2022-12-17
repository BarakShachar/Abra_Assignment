from pydantic import BaseModel, validator


class SendMessage(BaseModel):
    subject: str
    message: str
    receiver: str

    @validator("subject", pre=True)
    def validate_subject(cls, value):
        if len(value) > 255:
            raise ValueError("subject too long, max length: 255")
        return value

    @validator("message", pre=True)
    def validate_message(cls, value):
        if len(value) > 2048:
            raise ValueError("message too long, max length: 2048")
        return value

    @validator("receiver", pre=True)
    def validate_receiver(cls, value):
        if value == "":
            raise ValueError("you must add receiver username")
        return value
