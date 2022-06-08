import re

def validate_price(value: str):
    """valueが価格として
    正しい文字列(数字とカンマを含む文字列)であるかどうかを判別し、
    正しくない値の場合は例外ValueErrorを発生させる
    """
    if not re.search(r"^[0-9,]+$", value):
        raise ValueError(f"Invalid price: {value}")

validate_price("3,000")
validate_price("無料")
