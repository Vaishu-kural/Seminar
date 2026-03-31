import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Machine": ["M1","M2","M3","M4","M5"],
    "Production": [120,150,130,170,160]
}

df = pd.DataFrame(data)

plt.bar(df["Machine"], df["Production"])
plt.title("Factory Production Analysis")
plt.xlabel("Machine")
plt.ylabel("Units Produced")
plt.show()
