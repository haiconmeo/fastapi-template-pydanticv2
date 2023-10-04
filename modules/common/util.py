from typing import List

def pick_(source: any, keys: List[str]) -> dict:
    if type(source) is dict:
        return {key: source[key] for key in keys}

    return {key: getattr(source, key) for key in keys}

def clone_model(model):
    """Clone an arbitrary sqlalchemy model object without its primary key values."""
    # Ensure the model’s data is loaded before copying.
    model.id

    table = model.__table__
    non_pk_columns = [k for k in table.columns.keys() if k not in table.primary_key]
    data = {c: getattr(model, c) for c in non_pk_columns}
    if 'id' in data:
        data.pop('id')
    return data