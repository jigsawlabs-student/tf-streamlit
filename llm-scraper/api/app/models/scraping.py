from sqlalchemy.orm import backref, relationship

from app import db


class Scraping(db.Model):
    __tablename__ = 'scrapings'
    
    id = db.Column(db.Integer, primary_key=True)
    position = db.Column(db.String(120), nullable=False)
    location = db.Column(db.String(120), nullable=False)
    date = db.Column(db.Date(), nullable=False)
    job_idx = db.Column(db.Integer(), nullable=False)
    positions = relationship('Position', back_populates='scraping')
    