from schemas import ItemSchema


def convert_itemschema_to_dict(item: ItemSchema):
    
    dictionary={'flujo': [item.flujo],'Vlo-O': [item.Vlo_O],   
        'periodo_dia': [item.periodo_dia], 'DIANOM': [item.DIANOM],
        'MES':[item.MES], 'SIGLADES': [item.SIGLADES]
        }

    return dictionary
