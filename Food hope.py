import console
import random as r
from sympy.matrices import Matrix
import Food_data

def choose(A,k):
	if k==0:return [[]]
	if len(A)==k:return [A]
	return [[A[i]]+C for i in range(len(A)-k+1) for C in choose(A[i+1:],k-1)]
def nCr(a,b):
	ans=1
	for i in range(1,b+1):ans*=(a-i+1)/i
	return ans
def cost(items,qty):
	return sum([items[i][3]*qty[i] for i in range(len(items))])
def distance(items,qty,matches):
	dist=0.0
	for i in range(len(nutrients)):
		if i not in matches:
			dist+=(nutrients[i]-sum([items[j][2][i]*qty[j] for j in range(len(items))]))**2
	return dist**.5

nutrients= Food_data.nutrients
foods= Food_data.foods

def getHealthyCombos(cheap,categories=list(range(len(nutrients))),fileIndex=0):
	#each combo is a list of foods, the amounts, and maybe the total cost or distance
	combos=[]
	n=len(categories)
	total=nCr(len(foods),n)
	percent=fileIndex/total
	
	C=choose(foods,n)
	progress=open('%s_progress.txt'%str(categories),'a+')
	solutions=open('%s_indexes.txt'%str(categories),'a+')
	for c in range(fileIndex,int(total)):
		progress.write('%d\n'%c)
		percent+=100/total
		console.clear()
		print('Progress: %f%%'%percent)
		print('|%s%s|\n'%('-'*int(percent),' '*(100-int(percent))))
		M = Matrix([[]]*n)
		for f in C[c]:
			fax=[f[2][i] for i in categories]
			M=M.row_join(Matrix(fax))
		fax=[nutrients[i] for i in categories]
		M=M.row_join(Matrix(fax))
		amounts=[a[0] for a in M.rref()[0][:,-1].tolist()]
		if 0 not in [x>=0 for x in amounts] and sum(amounts)!=1:
			solutions.write(str(c))
			combos+=[(C[c],amounts)]
			if cheap:combos[-1]+=(cost(c,amounts),)
			if n<len(nutrients):combos[-1]+=(distance(C[c],amounts,categories),)
	progress.close()
	solutions.close()
	
	results=open('%s_results_2.txt'%str(categories),'w+')
	if cheap or n<len(nutrients):
		combos=sorted(combos,key=lambda x:x[2])
	for combo in combos:
		for i in range(len(combo[0])):
			results.write('%s: %f %s\n'%(combo[0][i][0],combo[1][i],combo[0][i][1]))
		if cheap or n<len(nutrients):results.write('\nCost/Distance: %.2f\n\n'%combo[2])
		
		intake=[0]*len(nutrients)
		for i in range(len(combo[0])):
			for j in range(len(nutrients)):
				intake[j]+=combo[0][i][2][j]*combo[1][i]
		names=['calories','fat','saturated fat','cholesterol','protein','carbohydrates','sugar','fiber','calcium','sodium','potassium','folic acid','vitamin C']
		for i in range(len(intake)):
			results.write('%s: %.2f%%\n'%(names[i],100*intake[i]/nutrients[i]))
		results.write('\n%s\n\n'%('-'*20))
	
	results.close()
	print('Done!')
	return combos

getHealthyCombos(False,[0,1,3,4,6,7])
