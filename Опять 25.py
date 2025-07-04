from loguru import logger as log

log.add("logfile.log", rotation="1 MB", encoding="utf-8", level="DEBUG")

def divide(a, b):
    return a / b

try:
    answer_A = int(input("Input A> "))
    answer_B = int(input("Input B> "))
    print(divide(answer_A, answer_B))
except ZeroDivisionError:
    log.exception("Error with device")
except Exception:
    log.exception("Unknow error")