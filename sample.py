import pandas as pd
import plotly.figure_factory as ff
import statistics as stats
import random

df = pd.read_csv("data.csv")

data = df["average"].tolist()

average_mean = stats.mean(data)
average_stdev = stats.stdev(data)

print(average_mean, average_stdev)

def random_sampler(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data) - 1)
        value = data[random_index]
        dataset.append(value)
    sample_mean = stats.mean(dataset)
    return sample_mean

def show_fig(data):
    fig = ff.create_distplot([data], ["Average"], show_hist= False)
    fig.show()

def main():
    mean_list = []
    for i in range(0, 1000):
        meanValue = random_sampler(100)
        mean_list.append(meanValue)
    
    show_fig(mean_list)

    mean = stats.mean(mean_list)
    stdev = stats.stdev(mean_list)

    print(mean, stdev)
    

main()