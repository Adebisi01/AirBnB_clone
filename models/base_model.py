#!/usr/bin/python3
import uuid
from datetime import datetime
import sys
# sys.path.insert(0, './engine/')
from .__init__ import storage


class BaseModel:
    def __init__(self, *args, **kwargs):
        self.id = uuid.uuid1()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if self.created_at is self.updated_at:
            storage.new()
        for key, value in kwargs.items():
            if key != __class__:
                if isinstance(value, datetime):
                    self.key = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.key = value
            else:
                continue

    def __str__(self):
        return '[{}] ({}) {}'.format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        self.__class__ = self.__class__
        self.created_at = self.created_at.isoformat('T')
        self.updated_at = self.updated_at.isoformat('T')
        return self.__dict__


if __name__ == "__main__":
    BaseModel()
