import matplotlib.pyplot as plt
import squarify
from DataProcessing import df

data = {}
with open("CrashOutput") as f:
    for line in f:
        parts = line.strip().split()
        if len(parts) >= 2:
            value = int(parts[-1])
            key = " ".join(parts[:-1])
            data[key] = value

# Plotting bar chart
plt.figure(figsize=(12, 6))
plt.bar(data.keys(), data.values(), color='skyblue')
plt.xlabel('Contributing Factor')
plt.ylabel('Fatalities')
plt.title('Fatalities by Contributing Factor')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Creating a pie chart of the top 5 contributing factors
top_5 = dict(sorted(data.items(), key=lambda item: item[1], reverse=True)[:5])

plt.figure(figsize=(6, 6))
plt.title('Top 5 Contributing Factors by Fatalities')
plt.pie(
    top_5.values(),
    labels=top_5.keys(),
    autopct='%1.1f%%',
    textprops={'fontsize': 8},
    startangle=140
)
plt.axis('equal')
plt.tight_layout()
plt.show()

# Tree Map
# Sort data and select top 10
top_items = dict(sorted(data.items(), key=lambda item: item[1], reverse=True)[:10])
sizes = list(top_items.values())
labels = [f'{k}\n{v}' for k, v in top_items.items()]

# Plot treemap
plt.figure(figsize=(10, 6))
squarify.plot(
    sizes=sizes,
    label=labels,
    color=plt.cm.Set3.colors,
    pad=True,
    text_kwargs={'fontsize': 9}
)
plt.title('Top 10 Contributing Factors - Treemap')
plt.axis('off')
plt.tight_layout()
plt.show()

