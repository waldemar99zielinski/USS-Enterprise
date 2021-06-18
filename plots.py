import matplotlib.pyplot as plt





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



