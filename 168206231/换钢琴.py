'''graph'''
	graph = {}
	graph["yuepu"] = {}
	graph["yuepu"]["changpian"] = 5
	graph["yuepu"]["chang"] = 5
	graph["yuepu"]["haibao"] = 0
	graph["changpian"] = {}
	graph["changpian"]["jita"] = 15
	graph["changpian"]["jiazigu"] = 20
	graph["chang"] = {}
	graph["chang"]["jita"] = 15
	graph["chang"]["jiazigu"] = 20
	graph["haibao"] = {}
	graph["haibao"]["jita"] = 30
	graph["haibao"]["jiazigu"] = 35
 @@ -18,21 +18,22 @@
	"""costs"""
	infinity = float("inf")#定义infinity为无穷'''
	costs = {}
	costs["changpian"] = 5
	costs["chang"] = 5
	costs["haibao"] = 0
	costs["jita"] = infinity
	costs["jiazigu"] = infinity
	costs["piano"] = infinity
	
	"""prenter"""
	parents = {}
	parents["cbangpian"] = "yuepu" 
	parents["haibao"] = "yuepu"
	parents["jita"] = None 
	parents["jiazigu"] = None
	parents["piano"] = None  
	parents['chang'] = 'yuepu' 
	parents['haibao'] = 'yuepu'
	parents['jita'] = None 
	parents['jiazigu'] = None
	parents['piano'] = None  
	
	processed = []
	lists = []
	def find_lowest_cost_node(costs):
		lowest_cost = float("inf")
		lowest_cost_node = None
 @@ -50,11 +51,27 @@ def find_lowest_cost_node(costs):
		for n in neighbors.keys():
			new_cost = cost + neighbors[n]
			if costs[n] > new_cost:
				print("start -> " + n + " 需要" + str(costs[n]) + "美分" +"改为")
				costs[n] = new_cost
				parents[n] =node
			print("start -> " + n + " 需要" + str(costs[n]) + "美分")
		processed.append(node)
		node = find_lowest_cost_node(costs)
	
	for n,m in costs.items():
		print(n + " : " + str(m))
	print("\n\n")
	
	"""mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm"""
	print("换钢琴最好路劲：")
	m = "piano"
	while 1:
		if m is "yuepu":
			break
		else:
			lists.append(parents[m] + " -> ") 
			m = parents[m]
	while len(lists):
		l = lists.pop()
		print(l)
	print("piano ")
	"""mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm"""