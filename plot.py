import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.cbook as cbook
import csv
import xlrd

headers=['ns','g','g1']
df = pd.read_csv('90.10_chyo_cyclic.csv', names = headers)

### Plots 2 data sets against same y axis

y1 = df['g']
y2 = df['g1']
x = df['ns']

def plot():

	fig, ax1 = plt.subplots()

	# Line options
	plt.plot(x,y1, linewidth = 1, label='Amount SURF-CHYO')
	plt.plot(x,y2, linewidth = 1, label='Ratio SURF-CHYO to PL')
	plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower right',
           		ncol=2, mode="expand", borderaxespad=0.)
	plt.title('SURF-CHYO (cyclic)', y=0.9)
	plt.ylim(0,7)
	plt.xlabel('Time (ns)')
	plt.show()

	# Save as:
	plt.savefig('90.10_surf_CHYO_cyclic.png')

plot()
print('Finished')