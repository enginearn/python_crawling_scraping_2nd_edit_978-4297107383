from jsonschema import validate

schema = {
    "type": "object", # rule 1
    "properties": {
        # rule 2
        "name": {
            "type": "string"
        },
        # rule 3
        "price": {
            "type": "string",
            "pattern": "^[0-9,]+$"
        }
    },
    # rule 4
    "required": ["name", "price"]
}

validate({
    "name": "ぶどう",
    "price": "3,000"
}, schema)

validate({
    "name": "みかん",
    "price": "無料"
}, schema)
