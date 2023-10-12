#!/usr/bin/python3

def class_to_json(obj):
    if isinstance(obj, (list, tuple)):
        return [class_to_json(item) for item in obj]
    elif isinstance(obj, dict):
        return {class_to_json(k): class_to_json(v) for k, v in obj.items()}
    elif isinstance(obj, str):
        return obj
    elif isinstance(obj, int):
        return obj
    elif isinstance(obj, bool):
        return obj
    else:
        # For unsupported types, return None
        return None