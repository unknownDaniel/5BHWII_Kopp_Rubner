from functools import wraps
import time

def timer(func):
    @wraps(func)                             # damit beim returnieren der ganzen methode die magic variablen erhalten bleiden oder so
    def wrapped_timer(*args, **kwargs): #(kw)args kommen von der func ind den Parametern der wrapper function
                                             # args für listenartige Param. und kwargs für benannte Param. (= z.B. dicts)
        start_t = time.perf_counter()
        result = func(*args, **kwargs)
        end_t = time.perf_counter()
        whole_t = end_t - start_t
        print(f'Die Funktion {func.__name__}{args} hat {whole_t:.6f} Sekunden gedauert')
        return result
    return wrapped_timer