import matplotlib.pyplot as plt
from datetime import datetime




def get_fitness_scatter_plot(log):
    x = []
    y = []
    x_counter = 0
    for generation in log:
        for fitness in generation:
            x.append(x_counter)
            y.append(fitness)
        x_counter += 1
    s = 10000/len(x)

    plt.scatter(x, y, s)
    plt.xlabel("Generation")
    plt.show()


def get_fitness_average_scatter_plot(log):
    x=[]
    y=[]
    x_counter = 0
    for generation in log:
        sumOfFintess = sum(generation)
        avg = sumOfFintess / len(generation)
        x.append(x_counter)
        x_counter += 1
        y.append(avg)
    s = 10000 / len(x)
    plt.scatter(x, y, s)
    plt.xlabel("Generation")
    plt.ylabel("Average population fitness")
    plt.show()


def getmicro(str):
    hours = int(str[0])
    min = int(str[2:4])
    sec = int(str[5:7])
    micro = int(str[8:13])
    time = hours*60*60*(10**6) + min*60*(10**6) + sec*(10**6)+micro
    return time




def get_time_plot():
    x=[]
    evo_y=[]
    sjf_y=[]
    res = []
    for _ in range(0, 1100, 10):
        x.append(_)

    file1 = open("evo_time2.txt", "r")
    file2 = open("sjf_time2.txt", "r")
    file3 = open("res_diff2.txt", "r")
    linesF1 = file1.readlines()
    linesF2 = file2.readlines()
    linesF3 = file3.readlines()
    for l in linesF1:
        evo_y.append(getmicro(l))

    for l in linesF2:
        sjf_y.append(getmicro(l))
    for l in linesF3:
        res.append(float(l))
    print("1: x len", len(x))
    print("res len", len(res))

    for _ in range(1250, 1750, 250):
        x.append(_)

    file1 = open("evo_time3.txt", "r")
    file2 = open("sjf_time3.txt", "r")
    file3 = open("res_diff3.txt", "r")
    linesF1 = file1.readlines()
    linesF2 = file2.readlines()
    linesF3 = file3.readlines()
    for l in linesF1:
        evo_y.append(getmicro(l))
    for l in linesF2:
        sjf_y.append(getmicro(l))
    for l in linesF3:
        res.append(float(l))
    print("2: x len", len(x))
    print("res len", len(res))
    x.append(2000)

    file1 = open("evo_time.txt", "r")
    file2 = open("sjf_time.txt", "r")
    file3 = open("res_diff.txt", "r")
    linesF1 = file1.read().splitlines()
    linesF2 = file2.readlines()
    linesF3 = file3.readlines()
    for l in linesF1:

        evo_y.append(getmicro(l))
    for l in linesF2:
        sjf_y.append(getmicro(l))
    for l in linesF3:
        res.append(float(l))
    print("x len", len(x))
    print("3: res len", len(res))
    plt.title("SJF EVO solution comparison")
    plt.xlabel("Crewmates number")
    plt.ylabel("Time in microseconds")
    plt.plot(x,res)
    plt.show()
