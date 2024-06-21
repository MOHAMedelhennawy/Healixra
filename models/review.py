# #!/usr/bin/python3
# """Specialization Class defenition"""

# from models.base_model import BaseModel, Base 
# from sqlalchemy import Column, String, Integer, Text, ForeignKey


# class Review(BaseModel, Base):
#     __tablename__ = 'reviews'
#     patient_id = Column(String(60), ForeignKey('patients.id'), nullable=False)
#     doctor_id = Column(String(60), ForeignKey('doctors.id'), nullable=False)
#     review_text = Column(Text)
#     rating = Column(Integer)
