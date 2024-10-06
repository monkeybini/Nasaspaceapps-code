import numpy as np
import pandas as pd
from obspy import read
import random
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import os
import math
import csv


#choose mars or lunar folder
planet = "lunar"
directory = './data/'+planet+'/test/'
if planet=='lunar':
	#Edit to get specific data set in Lunar data such as S12_GradeB or S15_GradeA 
	lunarfile_specific = "S12_GradeB"
	data_directory = directory+'data/'+lunarfile_specific

elif planet =="mars":
	data_directory = directory+'data/'

datalist =[]

#Mars folder

#cycling through all files
#calculating arrival line for each
#

for file in os.listdir(data_directory):
	with open(os.path.join(data_directory, file)) as f:
		if file.endswith(".csv"):
			datfile = pd.read_csv(f)

			#NOTE!:  for lunar data folders, certain files label relative time as time_rel or rel_time
			#You may have to change 'rel_time(sec)' into 'time_rel(sec)' and 'velocity(c/s)' into 'velocity(m/s)'
			if planet=='mars':
				csv_times = np.array(datfile['rel_time(sec)'].tolist())
				csv_data = np.array(datfile['velocity(c/s)'].tolist())
			elif planet == 'lunar':
				csv_times = np.array(datfile['time_rel(sec)'].tolist())
				csv_data = np.array(datfile['velocity(m/s)'].tolist())
			
			average = np.average(csv_data)
			#calculating arrival line
			arrival_time_rel = csv_times[np.where(csv_data==max(csv_data))[0]-5000]
			arrival_time_rel = arrival_time_rel[0]
			
			#put it all into datalist, which represents the final csv file catalog
			datalist.append({"filename":file, "time_rel(sec)": arrival_time_rel, "evid":file.split("_",1)[1]})

			fig,ax = plt.subplots(1,1,figsize=(10,3))
			ax.plot(csv_times,csv_data)

			ax.set_xlim([min(csv_times),max(csv_times)])
			ax.set_ylabel('Velocity (c/s)')
			ax.set_xlabel('Time (s)')
			ax.set_title(f'{file}', fontweight='bold')

			arrival_line = ax.axvline(x=arrival_time_rel, c='red', label='Rel. Arrival')
			ax.legend(handles=[arrival_line])
			fig.savefig(directory+"plots/"+file.split("_",1)[1]+".png")

			plt.close(fig)





#upload all data in datalist onto the final catalog file
with open(directory+'catalogs/'+planet+'_test_final.csv', 'w', newline='') as csvfile:
	fieldnames = ["filename", "time_rel(sec)", "evid"]
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()
	writer.writerows(datalist)


'''
fig,ax = plt.subplots(1,1,figsize=(10,3))
ax.plot(csv_times,csv_data)

ax.set_xlim([min(csv_times),max(csv_times)])
ax.set_ylabel('Velocity (m/s)')
ax.set_xlabel('Time (s)')
ax.set_title(f'{test_filename}', fontweight='bold')

arrival_line = ax.axvline(x=arrival_time_rel, c='red', label='Rel. Arrival')
ax.legend(handles=[arrival_line])

plt.show()'''