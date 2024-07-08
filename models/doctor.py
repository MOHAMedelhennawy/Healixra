#!/usr/bin/python3
"""Doctor Class defenition"""

from models.base_model import BaseModel 
from sqlalchemy import Column, String, DateTime, Text, ForeignKey, BLOB
from sqlalchemy.orm import relationship
from models.base_model import db
from sqlalchemy.ext.mutable import MutableDict
from sqlalchemy.dialects.postgresql import JSON
from datetime import datetime, timedelta
from models.appointment import Appointment

class Doctor(BaseModel, db.Model):
    __tablename__ = 'doctors'
    specialization_id = db.Column(db.String(60), db.ForeignKey('specializations.id'),nullable=False)
    location_id = db.Column(db.String(128), db.ForeignKey('locations.id'), nullable=False)
    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128), nullable=False)
    schedule = db.Column(MutableDict.as_mutable(JSON), default={})
    image = db.Column(db.String(40), nullable=False, default='user.jpg')

    appointments = db.relationship('Appointment', back_populates='doctor')
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

    def get_appointments(self, date):
        """
        Get all appointments based on doctor and date
        
        Keyword arguments:
        date -- Date to booking with format 'year:month:day'
        Return: filtration appointments
        """
        times = []
        if date.strftime('%A') in self.schedule.keys():
            for appointment in self.appointments:
                if appointment.appointment_date == date:
                    times.append(appointment.appointment_time.strftime('%H:%M'))
            return times
        else:
            print('invalid day')
            return [], date

    def get_valid_appointments(self, date):
        """
        Get all valid appointments on a date.
        
        Keyword arguments:
        date -- Date for booking with format 'year:month:day'
        Return: valid appointments on that day
        """
        slots = []
        date_object = datetime.strptime(date, '%Y-%m-%d').date()
        if date_object.strftime('%A') in self.schedule.keys():
            schedule = self.schedule[date_object.strftime('%A')]
            for day in schedule:
                start = day['start']
                end = day['end']
                slots.extend(self.generate_time_slots(start, end, date_object))
        return {date: slots}

    def generate_time_slots(self, start_time_str, end_time_str, date, interval_minutes=15):
        """Generate time slots between start and end times with a given interval."""
        start_time = datetime.strptime(start_time_str, '%H:%M').time()
        end_time = datetime.strptime(end_time_str, '%H:%M').time()
        
        slots = []
        current_time = datetime.combine(date, start_time)
        end_time = datetime.combine(date, end_time)
        invalid_appointments = self.get_appointments(date)
        while current_time < end_time:
            if current_time.time().strftime('%H:%M') not in invalid_appointments:
                slots.append(current_time.time().strftime('%H:%M'))
            current_time += timedelta(minutes=interval_minutes)
        
        return slots