list = ["A", "B", "C", "D"]
	def find(list):
		    flag = 0   
		    for i in list:    
		        if (i !="A") + (i=="D") + (i=="B") + (i !="D") == 1:
		            flag = 1
		            print("С͵��"  + i)
		    if flag == 0:
		        print("�Ҳ���С͵")
	
	find(list)