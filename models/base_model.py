#!/usr/bin/python3
'''
module that contain BaseModel
'''

from uuid import uuid4
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import models
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, DateTime
import os
# from routes import db
from __init__ import  app

db = SQLAlchemy(app)

class BaseModel:
    '''
    BaseModel that defines all common attributes/methods for other classes
    '''

    id = db.Column(db.String(60), primary_key=True, nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow())


    def __init__(self, *args, **kwargs):
        """Initialization of the base model"""
        format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], format)
            else:
                self.created_at = datetime.utcnow()
            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], format)
            else:
                self.updated_at = datetime.utcnow()
            if kwargs.get("id", None) is None:
                self.id = str(uuid4())
        else:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at

    def __str__(self):
        '''
        Return the informal presentation of class
        '''
        obj_dict = self.__dict__.copy()
        obj_dict.pop("_sa_instance_state", None)
        return f"[{self.__class__.__name__}] ({self.id}) {obj_dict}"

    def save(self):
        '''
        updates the public instance attribute updated_at
        with the current datetime
        '''

        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        '''
        returns a dictionary containing all keys/values of
        __dict__ of the instance
        '''

        instance_dict = self.__dict__.copy()
        instance_dict["__class__"] = self.__class__.__name__
        if "created_at" in instance_dict:
            instance_dict["created_at"] = self.created_at.isoformat()
        if "updated_at" in instance_dict:
            instance_dict["updated_at"] = self.updated_at.isoformat()

        if "_sa_instance_state" in instance_dict.keys():
            del instance_dict["_sa_instance_state"]
        return instance_dict

    def delete(self):
        """
        to delete the current instance from the storage
        """
        models.storage.delete(self)