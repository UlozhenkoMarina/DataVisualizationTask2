import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = [
    [1,0,2414.17],[1,1,3791.73],[1,2,3570.28],[1,3,4045.11],[1,4,3358.06],
    [1,5,3812.34],[1,6,3193.64],[1,7,3468.18],[1,8,3596.73],[1,9,2764.16],
    [1,10,2139.66],[1,11,2076.65],[1,12,1216.22],[1,13,1930.59],[1,14,2518.79],
    [1,15,1364.77],[1,16,1414.61],[1,17,1212.74],[1,18,1084.32],[1,19,883.08],
    [1,20,656.95],[1,21,2669.89],[1,22,3133.31],[1,23,1736.79],
    [2,0,3021.42],[2,1,4112.84],[2,2,4004.50],[2,3,3811.49],[2,4,3690.45],
    [2,5,3024.02],[2,6,3208.80],[2,7,2720.90],[2,8,3061.69],[2,9,2845.48],
    [2,10,2826.14],[2,11,1066.26],[2,12,1913.84],[2,13,1621.45],[2,14,1056.28],
    [2,15,2038.46],[2,16,1430.39],[2,17,1179.00],[2,18,1853.34],[2,19,125.78],
    [2,20,2029.91],[2,21,406.04],[2,22,2843.58],[2,23,1498.23],
    [3,0,2747.34],[3,1,3009.69]
]

df = pd.DataFrame(data, columns=["day_of_week", "hour_of_day", "avg_tfr_min"])

def sla_color(val):
    if val <= 15:
        return "green"
    elif val <= 45:
        return "yellow"
    else:
        return "red"

heatmap_data = df.pivot(index="hour_of_day", columns="day_of_week", values="avg_tfr_min")

plt.figure(figsize=(12,8))
sns.heatmap(heatmap_data, annot=True, fmt=".0f", cmap="Reds", cbar_kws={'label': 'TFR (хв)'})
plt.title("Середній час відповіді (TFR) по днях та годинах")
plt.xlabel("День тижня (1=Пн, 2=Вт, 3=Ср)")
plt.ylabel("Година дня")
plt.show()

plt.figure(figsize=(14,6))
for day in df['day_of_week'].unique():
    subset = df[df['day_of_week']==day]
    plt.plot(subset['hour_of_day'], subset['avg_tfr_min'], marker='o', label=f"День {day}")

plt.axhline(15, color='green', linestyle='--', label="SLA ≤ 15 хв")
plt.axhline(45, color='red', linestyle='--', label="SLA > 45 хв")

plt.title("Середній TFR по годинах")
plt.xlabel("Година дня")
plt.ylabel("TFR (хв)")
plt.xticks(range(0,24))
plt.legend()
plt.grid(True)
plt.show()
