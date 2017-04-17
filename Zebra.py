import itertools

Houses = ['Red','Green','Ivory','Yellow','Blue']
Nationalities = ['English','Spaniard','Ukrainian','Norwegian','Japanese']
Pets = ['Dog','Snails','Fox','Horse','Zebra']
Drinks = ['Coffee','Tea','Milk','Orange','Water']
Cigarettes = ['Old Gold','Kools','Chesterfields','Lucky Strike','Parliaments']

foundFlag = 0
count=0

for H in list(itertools.permutations(Houses)):
	if(H[1] != 'Blue'):
		continue
	if(H.index('Ivory') == 4 or H[H.index('Ivory')+1] != 'Green'):
		continue
	for N in list(itertools.permutations(Nationalities)):
		if(N.index('Norwegian') != 0):
			continue
		if(N.index('English') != H.index('Red')):
			continue
		for D in list(itertools.permutations(Drinks)):
			if(D.index('Coffee') != H.index('Green')):
				continue
			if(N.index('Ukrainian') != D.index('Tea')):
				continue
			if(D.index('Milk') != 2):
				continue
			for C in list(itertools.permutations(Cigarettes)):
				if(C.index('Kools') != H.index('Yellow')):
					continue
				if(C.index('Lucky Strike') != D.index('Orange')):
					continue
				if(N.index('Japanese') != C.index('Parliaments')):
					continue
				for P in list(itertools.permutations(Pets)):
					if(N.index('Spaniard') != P.index('Dog')):
						continue
					if(C.index('Old Gold') != P.index('Snails')):
						continue
					if((C.index('Chesterfields')+1 != P.index('Fox')) and (C.index('Chesterfields')-1 != P.index('Fox'))):
						continue
					if((C.index('Kools')+1 != P.index('Horse')) and (C.index('Kools')-1 != P.index('Horse'))):
						continue
					count+=1
					print('----------------------------------------------------------------------')
					print('Ok Found Solution so Far')
					print(H)
					print(N)
					print(D)
					print(C)
					print(P)
					print('----------------------------------------------------------------------')
					print('Solution1:',N[D.index('Water')],'Drinks Water')
					print('Solution2:',N[P.index('Zebra')],'Owns a Zebra')
					print('----------------------------------------------------------------------')
print('All possibilities =',count)				
print('----------------------------------------------------------------------')
