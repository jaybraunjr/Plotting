import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.cbook as cbook
import csv
import xlrd

headers=['c','g']
df = pd.read_csv('chyo.csv', names = headers)

### One data set 

y1 = df['g']
x = df['c']

def plot():

	plt.plot(x,y1, linewidth = 1)
	plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower right',
           		ncol=2, mode="expand", borderaxespad=0.)

	plt.ylim(0.0,0.1)
	plt.title('CHYO Tail Order Parameter',y=0.9)
	plt.ylabel('Scd')
	plt.xlabel('Carbon')
	plt.show()

	# Save as:
	plt.savefig('chyo.png')

plot()
print('Finished')