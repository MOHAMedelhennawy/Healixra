#!/usr/bin/python3
"""Specialization Class defenition"""

from models.base_model import BaseModel 
from sqlalchemy import Column, String, DateTime, Text
from sqlalchemy.orm import relationship
from models.base_model import db
from __init__ import app

class Specialization(BaseModel, db.Model):
    __tablename__ = 'specializations'
    specialization_name = db.Column(String(128), nullable=False, unique=True)
    doctors = db.relationship('Doctor', back_populates='specialization', cascade='all, delete')