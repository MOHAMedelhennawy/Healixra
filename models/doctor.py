#!/usr/bin/python3
"""Doctor Class defenition"""

from models.base_model import BaseModel 
from sqlalchemy import Column, String, DateTime, Text, ForeignKey, BLOB
from sqlalchemy.orm import relationship
from models.base_model import db
from sqlalchemy.ext.mutable import MutableDict
from sqlalchemy.dialects.postgresql import JSON
from datetime import datetime, timedelta

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

    def get_appointments(self):
        appointments_time = {}
        for appointment in self.appointments:
            appointments_time[appointment.appointment_date] = appointment.appointment_time
        return appointments_time

    def generate_time_slots(self, start_time_str, end_time_str, day, interval_minutes=15):
        """Generate time slots between start and end times with a given interval."""
        start_time = datetime.strptime(start_time_str, '%H:%M')
        end_time = datetime.strptime(end_time_str, '%H:%M')

        slots = []
        current_time = start_time
        while current_time < end_time:
            next_time = current_time + timedelta(minutes=interval_minutes)
            slot_time = current_time.time()
            is_free = True
            for date, time in self.get_appointments().items():
                appoin_day = date.strftime('%A')
                if slot_time == time and appoin_day == day:
                    is_free = False
                    break
            if is_free:
                slots.append(current_time.strftime('%H:%M'))
            current_time = next_time
        return slots

    def get_valid_appointments(self, day):
        i = 1
        slots_dict = {}
        times = self.schedule[day]
        for time in times:
            slots = self.generate_time_slots(time['start'], time['end'], day)
            slots_dict[i] = slots
            i += 1
        return slots_dict