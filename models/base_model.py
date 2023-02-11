#!/usr/bin/python3
import uuid
from datetime import datetime

class BaseModel:
    def __init__(self):
        self.id = uuid.uuid1()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return '[{}] ({}) {}'.format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()
    def to_dict(self):
        self.__class__ = self.__class__.__name__
        self.created_at = self.created_at.isoformat('T')
        self.updated_at = self.updated_at.isoformat('T')
        return self.__dict__
