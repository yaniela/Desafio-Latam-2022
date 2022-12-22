from pydantic import BaseModel
from typing import Union


class ItemSchema(BaseModel):
    flujo: int
    Vlo_O: int
    periodo_dia: str
    DIANOM: str
    MES:int
    SIGLADES: str

### ejemplo 
'''{
  "flujo": 420,
  "Vlo_O": 71,
  "periodo_dia": "mañana",
  "DIANOM": "Miercoles",
  "MES": 3,
  "SIGLADES": "Concepcion"
}'''

   