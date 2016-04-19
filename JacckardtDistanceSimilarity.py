#Author:Caner Yildirim
#caneryild163@gmail.com
def jaccardSim( features,featlineno,featsize):
	resultJacDist = [[0 for size1 in range(featlineno)] for size2 in range(featlineno)] 
	for index1 in range(0,featlineno):
		for index2 in range(0,featlineno):
			totsize=0
			jaccRet=0
			if(index1<index2):				
				for index3 in range(1,featsize):
					jaccRet+=features[index1][index3]*features[index2][index3]
					totsize+= features[index1][index3] or features[index2][index3] 
				if totsize !=0:
					jaccRet=float(jaccRet)/totsize
				else:
					jaccRet=0
				resultJacDist[index1][index2]=jaccRet
				resultJacDist[index2][index1]=jaccRet
	return resultJacDist
