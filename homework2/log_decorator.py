import datetime
def function_logger(log_file):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Записываем информацию в лог-файл
            with open(log_file, 'a') as file:
                file.write(f"{func.__name__}\n")
                file.write(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                file.write(f"{args}\n")
                result = func(*args, **kwargs)
                file.write(f"{result}\n")
                file.write(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                file.write(f"{datetime.datetime.now() - start_time}\n\n")
                return result
        return wrapper
    return decorator
