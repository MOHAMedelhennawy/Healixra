#!/usr/bin/python3
"""Doctor Class defenition"""

from models.base_model import BaseModel 
from sqlalchemy import Column, String, DateTime, Text, ForeignKey, BLOB
from sqlalchemy.orm import relationship
from models.base_model import db
from sqlalchemy.ext.mutable import MutableDict
from sqlalchemy.dialects.postgresql import JSON


class Doctor(BaseModel, db.Model):
    __tablename__ = 'doctors'
    specialization_id = db.Column(db.String(60), db.ForeignKey('specializations.id'),nullable=False)
    location_id = db.Column(db.String(128), db.ForeignKey('locations.id'), nullable=False)
    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128), nullable=False)
    schedule = db.Column(MutableDict.as_mutable(JSON), default={})
    image = db.Column(db.String(40), nullable=False, default='user.jpg')

    reviews = db.relationship('Review', backref='doctor', cascade='all, delete')
    specialization = db.relationship('Specialization', back_populates='doctors')
    patients = db.relationship('Patient', secondary='doctor_patient', back_populates='doctors')


    def set_schedule(self, schedule_dict):
        """Set the doctor's weekly schedule"""
        self.schedule = schedule_dict

    def get_schedule(self):
        """Get the doctor's weekly schedule"""
        return self.schedule

    def add_availability(self, day, start_time, end_time):
        """Add availability to the doctor's schedule"""
        if day not in self.schedule:
            self.schedule[day] = []
        self.schedule[day].append({'start': start_time, 'end': end_time})
        self.schedule = self.schedule  # Trigger change tracking

    def remove_availability(self, day, start_time, end_time):
        """Remove availability from the doctor's schedule"""
        if day in self.schedule:
            self.schedule[day] = [slot for slot in self.schedule[day] if slot['start'] != start_time or slot['end'] != end_time]
            if not self.schedule[day]:
                del self.schedule[day]
            self.schedule = self.schedule  # Trigger change tracking