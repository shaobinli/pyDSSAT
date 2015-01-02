#!/usr/bin/env python

import	numpy			as np
import	matplotlib.pyplot	as plt
import	process_CDE		as pCDE

baseDir	= '/Users/hexg/Dropbox/Study/Princeton_2014-2015_Fall/APC524/APC_Project_HEXG/Data'
varName	= 'HWAH'

def	processOut(fileName):
	FILE	= file('%s/%s'%(baseDir,fileName)).readlines()
	outData	= FILE[4:]
	varId	= FILE[3]					# Read the raw variables 
	varId	= map(str,str.split(varId)[12:])		# Only get the useful variables
	bType	= map(str,str.split(FILE[4]))[5:7]		# Basic type: crop and model
	crpType	= bType[0]
	modType	= bType[1]
	nYear	= np.size(outData)
	dataArr	= np.array([map(float,str.split(outData[i])[11:]) for i in range(nYear)])	# Convert the raw data to numpy array
	dataDic	= {varId[i]:dataArr[:,i] for i in range(len(varId))} 
	sYear	= int(round(dataDic['PDAT'][0]/1000))
	eYear	= sYear+nYear
	Year	= np.arange(sYear,eYear)

	plt.figure()
	plt.plot(dataDic[varName],linewidth=1.5)
	plt.xlim([-1,nYear])
	plt.xticks(range(nYear)[::5],Year[::5])
	plt.xlabel('Year',fontsize=15)
	varDes	= pCDE.getVarDes(baseDir,'SUMMARYOUT.CDE')[varName][1]
	plt.title(varDes,fontsize=20)
	plt.show()
	
	return dataDic, sYear, eYear
	#return dataDic, sYear, eYear

# fileName= 'Summary.OUT'
#####	processOut('Summary.OUT','HWAH')[0].keys()	: See variables
#####	processOut('Summary.OUT','HWAH')[0]['PDAT']	: Data for specific variable

print	processOut('Summary.OUT')[1]

