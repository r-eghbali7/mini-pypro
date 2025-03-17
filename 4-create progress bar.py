import time
import progressbar

with progressbar.ProgressBar(max_value=10) as bar:
    for i in range(100):
        time.sleep(0.1)
        bar.update(i)