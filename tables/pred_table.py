from config_db.database import Base
from sqlalchemy import Column, Integer, String

class PredTable(Base):

    __tablename__ = 'predictions_table_2'
    id = Column(Integer, primary_key=True)
    credit_limit = Column(Integer)
    gender = Column(Integer)
    education = Column(Integer)
    age = Column(Integer)
    n_delay_payment = Column(Integer)
    bill_at_1 = Column(Integer)
    bill_at_2 = Column(Integer)
    bill_at_3 = Column(Integer)
    bill_at_4 = Column(Integer)
    bill_at_5 = Column(Integer)
    bill_at_6 = Column(Integer)
    model_name = Column(String)
    prediction = Column(String)
