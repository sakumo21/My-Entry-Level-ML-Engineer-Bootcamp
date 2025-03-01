import time
import sys

def ft_progress(m):
    total = len(m)
    start_time = time.time()
    for i in m:
        temp_i = i + 1
        elapsed_time = time.time() - start_time
        remaining_time = max((elapsed_time / temp_i) * (total - temp_i), 0)
        percent = temp_i  / total
        bar_lenght = 30
        progress_bar = int(percent * bar_lenght)
        bar = "=" * progress_bar + ">"
        sys.stdout.write(f"\rETA: {remaining_time:.02f}s  [{int(percent * 100):02d}%][{bar:<30}] /{total} | elapsed time  {elapsed_time:.02f}s     ")
        sys.stdout.flush()
        yield i
		
listy = range(3333)
ret = 0
for elem in ft_progress(listy):
    ret += elem
    time.sleep(0.005)
print()
print(ret)
