from tqdm import tqdm
from time import sleep

for i in tqdm(range(100), desc="Processing"):
    sleep(0.1)
    print(i)