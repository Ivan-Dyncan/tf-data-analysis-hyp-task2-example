import pandas as pd
import numpy as np


chat_id = 683312730 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    L = 1.555
    n1 = len(x)
    n2 = len(y)
    m1 = x.mean()
    m2 = y.mean()
    std1 = x.std()
    std2 = y.std()
    z = (m1-m2)/(std1**2/n1 + std2**2/n2)**(1/2)
    return abs(z)<L
