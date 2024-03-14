from pydantic import BaseModel

class Features(BaseModel):
    credit_limit: int
    gender: int
    education: int
    age: int
    n_delay_payment: int
    bill_at_1:int
    bill_at_2:int
    bill_at_3:int
    bill_at_4:int
    bill_at_5:int
    bill_at_6:int
    model_name:str

