'''
Nutrient (units)
calories
carbohydrates
protein
fat
fiber
vitamin A
thiamin
riboflavin
niacin
vitamin B6
vitamin B12
folate
vitamin C
calcium
iron
magnesium
potassium
sodium
zinc
'''
#iodine removed from index 14 aka -6
orange= [86,21.62,1.73,.22,4.4,20,.16,.074,.519,.11,0,55,97.9,74,.18,18,333,0,.13]
spinach= [23,3.63,2.86,.39,2.2,469,.078,.189,.724,.195,0,194,28.1,99,2.71,79,558,79,.53]
raspberries= [64,14.69,1.48,.8,8,2,.039,.047,.736,.068,0,26,32.2,31,.85,27,186,1,.52]

nutrients= [1800,250,64,66,30,900,1.2,1.3,16,1.3,2.4,400,45,1000,8,400,3800,600,14]
'''
Nutrient (units)
0: calories (kcal)
1: fat (g)
2: saturated fat (g)
3: cholesterol (mg)
4: protein (g)
5: carbohydrates (g)
6: sugar (g)
7: fiber (g)
8: calcium (mg)
9: sodium (mg)
10:potassium (mg)
11:folic acid (μg)
12:vitamin C (mg)
'''

carrot=('carrot','carrots',[31,0,0,0,1,7,0,2,19,25,233,10,7])
yogurt=('yogurt','x5.3 ounces',[190,10,7,25,18,8,8,0,200,70,0,0,0])
ginger=('ginger','x5 slices',[9,0,0,0,0,2,0,0,2,1,46,1,1])
orange=('orange','oranges',[45,0,0,0,1,11,9,2,38,0,174,29,51])
honey=('honey','tablespoons',[64,0,0,0,0,17,17,0,1,1,11,0,0])
tomato=('tomato','tomatoes',[35,1,0,0,1,7,4,1,20,5,0,0,24])
potato=('potato','potatoes',[88,0,0,0,2,20,0,0,8,7,608,14,22])
spinach=('spinach','x1.5 cups',[20,0,0,0,2,3,0,2,80,65,0,160,24])
beans=('black beans','cups',[227,1,0,0,15,41,0,15,46,2,611,256,0])
sweetpotato=('sweet potato','sweet potatoes',[103,0,0,0,2,24,7,4,43,41,524,7,22])
broccoli=('broccoli','bunches',[207,2,0,0,17,40,10,16,286,201,1921,383,542])
berries=('blue berries','x0.5 cups',[41,0,0,0,1,11,7,2,4,1,56,4,7])
apple=('apple','apples',[72,0,0,0,0,19,14,3,8,1,148,4,6])
avocado=('avocado','avocadoes',[289,27,4,0,3,15,1,12,22,14,877,154,15])
almond=('almond','x0.25 cups',[206,18,1,0,8,7,2,4,92,117,257,11,0])
rice=('brown rice','cups',[216,2,0,0,5,45,0,4,20,10,84,8,0])
egg=('egg','eggs',[72,5,2,186,6,0,0,0,28,71,69,24,0])

#ginger after yogurt
#broccoli after sweetpotatos
foods= [carrot,yogurt,orange,honey,tomato,potato,spinach,beans,sweetpotato,broccoli,berries,apple,avocado,almond,rice,egg]
nutrients= [1850,60,10,50,70,250,20,30,1050,1500,3900,400,75]
limits=[(1800,2050),(42,75),(0,10),(40,200),(60,100),(200,300),(0,25),(25,38),(900,1500),(1000,2000),(3500,4500),(380,580),(70,1800)]

intake=[0]*len(broccoli[2])
for i in range(len(sweetpotato[2])):
	#intake[i]+=.05*sweetpotato[2][i]
	intake[i]+=1.5*broccoli[2][i]
	intake[i]+=2.6*almond[2][i]
	intake[i]+=4.6*rice[2][i]
	intake[i]+=.25*egg[2][i]

for i in range(len(intake)):
	print('{:.2%}'.format(intake[i]/nutrients[i]))
