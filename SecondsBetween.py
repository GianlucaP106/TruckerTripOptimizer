from datetime import datetime

def SecondsBetween(d1, d2):
    d1 = datetime.fromisoformat(d1)
    d2 = datetime.fromisoformat(d2)
    return int(abs((d1 - d2).total_seconds()))