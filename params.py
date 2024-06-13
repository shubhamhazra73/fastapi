# pip install pydantic
from pydantic import BaseModel

class question_pairs(BaseModel) :

    question1 : str
    question2 : str
