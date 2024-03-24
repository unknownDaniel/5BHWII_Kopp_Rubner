from functools import wraps
import time

def timer(func):
    @wraps(func)                             
    def wrapped_timer(*args, **kwargs): 
                                            
        start_t = time.perf_counter()
        result = func(*args, **kwargs)
        end_t = time.perf_counter()
        whole_t = end_t - start_t
        print(f'Die Funktion {func.__name__}{args} hat {whole_t:.6f} Sekunden gedauert')
        return result
    return wrapped_timer
