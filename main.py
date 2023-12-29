import pandas
import matplotlib.pyplot as plt
import seaborn as sns

from commons import *

path = "datasets/population_by_country_2020.csv"

df = pandas.read_csv(path)


def top_population(count=20, colorful=0, df=df):

    font = {"size":15}

    df = df.sort_values("Population (2020)", ascending=False)
    df = df.head(count)

    xticks = [i * 100000000 for i in range(18)]
    palette = ["#00FFFF", "#0000FF"]

    if colorful:
        palette = [random_color_pick() for i in range(count)]

    sns.set_style("whitegrid")

    plt.figure(figsize=(12,10))
    sns.barplot(df, x="Population (2020)", y="Country (or dependency)", legend=False, palette=palette)

    plt.title(f"Top {count} population countries 2020 year", fontdict=font)
    plt.xlabel("Population (in 100 millions)", fontdict=font)
    plt.ylabel("")
    plt.xticks(xticks)
    #plt.ticklabel_format(style='plain', axis='x')

    plt.show()


def lowest_lifespan(count=20, colorful=0, df=df):

    font = {"size": 20}

    df = df.sort_values("Med. Age")
    df = df.head(count)

    palette = ["#900C3F", "#FF5733"]
    xticks = [i*2 for i in range(10)]

    if colorful:
        palette = [random_color_pick() for i in range(count)]

    sns.set_style("whitegrid")

    plt.figure(figsize=(12, 10))
    sns.barplot(df, x="Med. Age", y="Country (or dependency)", orient="h", legend=False, palette=palette)

    plt.title(f"Top {count} lowest average lifespan countries 2020 year", fontdict=font)
    plt.xlabel("Lifespan", fontdict=font)
    plt.ylabel("")
    #plt.xticks(xticks)

    plt.show()


def country_urban_pop(country="Russia", df=df):

    font = {"size": 26}

    labels = ["Urban", "Rural"]
    explode = (0, 0.08)
    colors = ["#E53935", "#4CAF50"]
    autopct = "%1.1f%%"
    urban_pop = int(df[df["Country (or dependency)"] == "Russia"]["Urban Pop %"].to_list()[0][:3])
    rural_pop = 100 - urban_pop
    pops = [urban_pop, rural_pop]

    plt.xkcd()

    plt.figure(figsize=(6, 5))
    plt.pie(pops, labels=labels, autopct=autopct, startangle=100, explode=explode, colors=colors)

    plt.title(f"{country} urban/rural pops ratio", fontdict=font)

    plt.show()


def countries_land_comparasion(count=10, df=df):

    font = {"size": 26}

    df = df.sort_values("Land Area (Km²)")
    df = df.tail(count)
    area_sum = df["Land Area (Km²)"].sum()
    countries = [i for i in df["Country (or dependency)"]]
    areas = [i for i in df["Land Area (Km²)"]]
    areas_percentage = [areas[i] / area_sum * 100 for i in range(len(countries))]

    autopct = "%1.1f%%"

    plt.figure(figsize=(6, 5))
    plt.pie(areas_percentage, labels=countries, autopct=autopct)

    plt.title(f"Land area ratio", fontdict=font)

    plt.show()
