import time

def log_action(func):
    async def wrapper(*args, **kwargs):
        action = func.__name__.replace('_', ' ').capitalize()
        print(f"{action} started at {time.strftime('%Y-%m-%d %H:%M:%S')}")
        result = await func(*args, **kwargs)  # Обратите внимание, что мы вызываем асинхронную функцию
        print(f"{action} finished at {time.strftime('%Y-%m-%d %H:%M:%S')}")
        return result
    return wrapper