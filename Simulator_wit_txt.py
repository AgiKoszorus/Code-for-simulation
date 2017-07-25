# simulacije za In eksperiment 
# reading in an excel file with A and B parameters
# txt filewith the masses
from peak_detect import detect_peaks
import os
import numpy as np
import matplotlib.pyplot as plt 
from sys import argv
import satlas as s 
import pandas as pd 

c =299792458

def doppler1(V,mass):
	beta = np.sqrt(1-((mass* 931.494095*10**6)**2/(V+mass* 931.494095*10**6)**2))
	dop = np.sqrt((1+beta)/(1-beta))
	return dop

def doppler2(V,m):
	beta = np.sqrt(1-((m* 931.494095*10**6)**2/(V+m* 931.494095*10**6)**2))
	dop = np.sqrt((1+beta)/(1-beta))
	return dop

Info = pd.read_csv ('C:\\Users\\MyStuff\\OneDrive\\Documents\\CRIS\\K\\Data_exl.csv')

centroid_at_rest = 389286074.578447

Spins = Info.SPIN

mass_list=[]

v_iscool  = 10002
diff=[]


for i in range (len(Spins)):
	I = Info.SPIN[i]
	isotope= float(Info.K[i])
	m= float(Info.MASS[i])
	if 44<m<45:


		Isotope_shif = float(Info.Isotope_shift[i])
		#IS = float(Info.IS_abs[i])



		fwhm = [5,5]
		A_L =float(Info['A_Lower'][i])
		B_L =float(0)
		A_U =float( Info['A_upper'][i])
		B_U =0

		centroid  = doppler1(v_iscool, m) *(centroid_at_rest + Isotope_shif+860)


		diff.append( centroid-389813520.659)
		print(m,centroid)
		#print(centroid/c* 10**4)
		x = np.linspace(centroid-2000,centroid+3500,10000)
		J = [0.5,0.5]
		ABC = [A_L,A_U , B_L,B_U , 0,0]
		model = s.HFSModel(I=I,J=J,fwhm=fwhm,centroid=centroid,ABC=ABC,scale=100,background_params = [0])


		plt.axvline((centroid/10**3-389813.520659)/30, color = 'k', linewidth=0.5 )
		plt.plot(((x)/10**3 - 389813.520659)/30,model(x)+i*50,linewidth=3 )
		plt.title('Offset 12985.185724 1/cm')
		plt.xlable  = ('1/cm')
		#plt.text (centroid/10**3-389813.520659,i*50, '{} MHz'.format(IS), fontsize=20)
		mass_list.append(m)

plt.show()