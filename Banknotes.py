from pydantic import BaseModel
class banknote(BaseModel):
    variance:float
    skewness:float	
    curtosis:float	
    entropy:float
