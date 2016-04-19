#Author:Caner Yildirim
#caneryild163@gmail.com
def cosdist( features,featlineno,featsize):
	resultCosDist = [[0 for size1 in range(featlineno)] for size2 in range(featlineno)] 
	for index1 in range(0,featlineno):
		for index2 in range(0,featlineno):
			cosDist=0
			leftsize=0
			rightsize=0
			if(index1<index2):				
				for index3 in range(1,featsize):
					cosDist+=features[index1][index3]*features[index2][index3]
					leftsize+=features[index1][index3]
					rightsize+=features[index2][index3]
				leftsize=sqrt(leftsize)
				rightsize=sqrt(rightsize)
				if leftsize*rightsize !=0 : 
					cosDist=(float(cosDist))/(leftsize*rightsize)
				else:
					cosDist=0
				resultCosDist[index1][index2]=cosDist
				resultCosDist[index2][index1]=cosDist
	return resultCosDist
