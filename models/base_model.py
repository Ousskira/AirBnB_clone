#!/usr/bin/python3
"""
The BaseModel class
"""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """Base class - the parent class"""

    def __init__(self, *args, **kwargs):
        """initialize function"""

        # initialize None 
        if kwargs == {}:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)
            return

        # deserialize
        for key, val in kwargs.items():
            if key == '__class__':
                continue
            self.__dict__[key] = val
        if 'created_at' in kwargs:
            self.created_at = datetime.strptime(
                    kwargs['created_at'],
                    '%Y-%m-%dT%H:%M:%S.%f')
        if 'updated_at' in kwargs:
            self.updated_at = datetime.strptime(
                    kwargs['updated_at'],
                    '%Y-%m-%dT%H:%M:%S.%f')

    def __str__(self):
        """revrite str"""
        fmt = "[{}] ({}) {}"
        return fmt.format(
                type(self).__name__,
                self.id,
                self.__dict__)

    def save(self):
        """up the last updated variable"""
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """give a dict representation of self"""
        temp = {**self.__dict__}
        temp['__class__'] = type(self).__name__
        temp['created_at'] = self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        temp['updated_at'] = self.updated_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        return temp

    @classmethod
    def all(cls):
        """Retrieve of cls"""
        return models.storage.find_all(cls.__name__)

    @classmethod
    def count(cls):
        """return num of all instances of the cls"""
        return len(models.storage.find_all(cls.__name__))

    @classmethod
    def create(cls, *args, **kwargs):
        """make an Instance"""
        new = cls(*args, **kwargs)
        return new.id

    @classmethod
    def show(cls, instance_id):
        """Ret instance"""
        return models.storage.find_by_id(
            cls.__name__,
            instance_id
        )

    @classmethod
    def destroy(cls, instance_id):
        """rm instance"""
        return models.storage.delete_by_id(
            cls.__name__,
            instance_id
        )

    @classmethod
    def update(cls, instance_id, *args):
        """Update an instance"""
        if not len(args):
            print("** attribute name missing **")
            return
        if len(args) == 1 and isinstance(args[0], dict):
            args = args[0].items()
        else:
            args = [args[:2]]
        for arg in args:
            models.storage.update_one(
                cls.__name__,
                instance_id,
                *arg
            )
