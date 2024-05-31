import time
import random

counter = 0
def marriage(name):
    global counter
    r = random.randint(0, 10)
    time.sleep(r)
    print(f"{name} marriage after {r} years")
    counter += 1

def main():
    for child in ["mamad", "goli", "gholi", "reza"]:
        marriage(child)

if __name__=="__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    total_time = end_time - start_time
    print(f"Executed in {total_time} seconds")