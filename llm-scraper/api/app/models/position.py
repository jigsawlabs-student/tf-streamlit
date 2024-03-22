from sqlalchemy.orm import backref, relationship

from app import db


class Position(db.Model):
    __tablename__ = 'positions'
    
    job_id = db.Column(db.String, primary_key=True)
    job_title = db.Column(db.String(120))
    company_name = db.Column(db.String(120))
    seniority_level = db.Column(db.String(120))
    min_salary = db.Column(db.Float, nullable=True)
    max_salary = db.Column(db.Float, nullable=True)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    zipcode = db.Column(db.String(120))
    presence = db.Column(db.String(120))
    scraping_id = db.Column(db.Integer, db.ForeignKey('scrapings.id'))
    
    scraping = relationship('Scraping', back_populates='positions')

    def to_dict(self):
        return dict((col, getattr(self, col)) for col in self.__table__.columns.keys())