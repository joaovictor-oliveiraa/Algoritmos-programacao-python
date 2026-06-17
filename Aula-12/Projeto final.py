import csv
import pandas as pd

dados_vgsales = [
    ["Rank", "Name", "Platform", "Year", "Genre", "Publisher", "Global_Sales"],
    [1, "Wii Sports", "Wii", 2006, "Sports", "Nintendo", 82.74],
    [2, "Super Mario Bros.", "NES", 1985, "Platform", "Nintendo", 40.24],
    [3, "Mario Kart Wii", "Wii", 2008, "Racing", "Nintendo", 35.82],
    [4, "Wii Sports Resort", "Wii", 2009, "Sports", "Nintendo", 33.00],
    [5, "Pokemon Red/Pokemon Blue", "GB", 1996, "Role-Playing", "Nintendo", 31.37],
    [6, "Tetris", "GB", 1989, "Puzzle", "Nintendo", 30.26],
    [7, "New Super Mario Bros.", "DS", 2006, "Platform", "Nintendo", 30.01],
    [8, "Kinect Adventures!", "X360", 2010, "Misc", "Microsoft Game Studios", 21.82],
    [10, "Duck Hunt", "NES", 1984, "Shooter", "Nintendo", 28.31],
    [11, "Nintendogs", "DS", 2005, "Simulation", "Nintendo", 24.76],
    [12, "Mario Kart DS", "DS", 2005, "Racing", "Nintendo", 23.42],
    [16, "Kinect Adventures!", "X360", 2010, "Misc", "Microsoft Game Studios", 21.82],
    [17, "Grand Theft Auto V", "PS3", 2013, "Action", "Take-Two Interactive", 21.40],
    [18, "Grand Theft Auto: San Andreas", "PS2", 2004, "Action", "Take-Two Interactive", 20.81],
    [19, "Super Mario World", "SNES", 1990, "Platform", "Nintendo", 20.61],
    [20, "Brain Age", "DS", 2005, "Misc", "Nintendo", 20.15],
    [21, "Pokemon Diamond/Pokemon Pearl", "DS", 2006, "Role-Playing", "Nintendo", 18.25],
    [22, "Super Mario Land", "GB", 1989, "Platform", "Nintendo", 18.14],
    [24, "Grand Theft Auto V", "X360", 2013, "Action", "Take-Two Interactive", 16.38],
    [25, "Grand Theft Auto: Vice City", "PS2", 2002, "Action", "Take-Two Interactive", 16.15]
]

with open("vgsales_sample.csv", "w", newline='', encoding='utf-8') as f:
    escritor = csv.writer(f)
    escritor.writerows(dados_vgsales)

df = pd.read_csv("vgsales_sample.csv")

print(df.isnull().sum())
print("-" * 40)

vendas_por_empresa = df.groupby('Publisher')['Global_Sales'].sum()
ranking = vendas_por_empresa.sort_values(ascending=False)
print(ranking)
print("-" * 40)

print("Conclusão: As Top 3 empresas que mais venderam são Nintendo, Take-Two Interactive e Microsoft Game Studios.")