list = ["A", "B", "C", "D"]
	def find(list):
		    flag = 0   
		    for i in list:    
		        if (i !="A") + (i=="D") + (i=="B") + (i !="D") == 1:
		            flag = 1
		            print("小偷是"  + i)
		    if flag == 0:
		        print("找不到小偷")
	
	find(list)