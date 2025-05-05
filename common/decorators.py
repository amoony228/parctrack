
def json_return(func):
    async def wrapper(*args):
        result = await func(*args)
        return [dict(record) for record in result]
    return wrapper
