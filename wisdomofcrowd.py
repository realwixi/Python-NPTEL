import statistics

import matplotlib.pyplot as plt
Estimates=[234,500,356,450,500,600,700,400,300,340,256,386,500,200,100,700,600,658,750,300,345,359,340,200,160]
Estimates.sort()

tv=int(0.1*len(Estimates))
Estimates = Estimates[:len(Estimates) - tv]
Estimates = Estimates[tv:]

y=[]
for i in range(len(Estimates)):
    y.append(5)
plt.plot(Estimates,y,'--')
plt.plot([statistics.mean(Estimates)],[5],'bs')
plt.plot([statistics.median(Estimates)],[5],'ro')
plt.plot([375],[5],'ro')

