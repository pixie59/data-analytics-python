import matplotlib.pyplot as plt
import numpy as np
days = np.arange(1,11)
sales_in_cr=np.array([2.5,3.0,4.2,5.1,6.0,7.5,8.0,9.2,10.5,11.0])
plt.figure(figsize=(10,5))
plt.style.use('fast')
plt.plot(days,sales_in_cr,marker='o',color='blue')# marker
plt.title("Daily sales over 10 days")
plt.grid(True)
plt.xlabel("Days")
plt.ylabel("Sales (in crores)")
plt.show()