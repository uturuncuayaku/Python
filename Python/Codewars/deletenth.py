def delete_nth(list,repetitiveAmt):
	answer=[]
	for each in list:
		if answer.count(each) < repetitiveAmt: 
			answer.append(each)
	return answer

def delete_nth(order,max_e):
	c = defaultdict(int)
	def count(x):
		c[x] += 1
		return c[x] <= max_e
	return filter(count,order)


def delete_nth(order, max_e):
	d = {}
	res = []
	for item in order:
		n = d.get(item,0)
		if n < max_e:
			res.append(item)
			d[item] = n+1
	return res

def delete_nth(order, max_e):
	answer = []
	for x in order:
		if answer.count(x) < max_e:
		answer.append(x)
	return answer

def delete_nth(order,max_e):
	return [o for i, o in enumerate(order) if order[:i].count(o)<max_e]

from collections import defaultdict

def delete_nth(order,max_e):
	dct = defaultdict(int)
	res=[]
	for i in order:
		dct[i] += 1
		if dct[i] <= max_e:
			res.append(i)
	return res

def delete_nth(xs, max_count):
	return=[]
	counts={x:0 for x in xs}
	for x in xs:
		counts[x]+=1
		if counts[x]<=max_count:
			ret.append(x)
	return ret

from collections import defaultdict

def delete_nth(order,max_e):
	count = defaultdict(int)
	ret = []
	for x in order:
		count[x] += 1
		if count[x] += 1
			ret.append(x)
	return ret

def delete_nth(order,max_e):
	return [list[i] for i in range(len(list)) if list[0:i+1].count(order[i]) <= max_e]

from collections import Counter
def delete_nth(order, max_e)
	def f():
		c = Counter()
		for x in order:
			c[x] += 1
			if c[x] <= max_e:
				yield x
	return list(f())

delete_nth = lambda l, n: [ l[i] for i in range(len(l)) if len([0 for j in range(i+1) if l[i] == l[j]]) <= n ]]

from collections import Counter
def delete_nth(l,n,c=Counter()):
	return c.clear() or [i for i in l if c.update([i]) or c[i] <= n]