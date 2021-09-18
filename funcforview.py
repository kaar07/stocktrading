import pandas as pd
from collections import *
def daywisegain(data):
    gainofdate = defaultdict(lambda:0)
    for i in range(len(data)):
        gainofdate[str(data.iloc[i]["DATE"])] += data.iloc[i]["ESTIMATEDPL"]
    total = 0
    pday = 0
    lday = 0
    highest = 0
    lowest = 0
    for key,value in gainofdate.items():
        print(key,value)
        highest = max(highest,value)
        lowest = min(lowest,value)
        total += value
        if(value<0):
            lday += 1
        else:
            pday += 1
    print("\n------------------------------------\n")    
    print(f"Total net gain inclusive of all estimated p/l: {total}")
    print(f"Days with profits: {pday}")
    print(f"Days with losses: {lday}")
    print(f"Average gain/loss per day: {total/(pday+lday)}")
    print(f"Most gain: {highest}")
    print(f"Most loss: {lowest}")
    
