class IO:
	def printLog(self,testcases,expected_result,student_result,time_):
		score = 0
		print("#")
		for i in range(len(testcases)):
			if expected_result[i] == student_result[i]:
				score+=1
			print(testcases[i]," : ",expected_result[i]==student_result[i])

		final = score/len(testcases)

		print("#")
		print(final)
		print("#")
		print(time_)







import time 

if __name__ == "__main__":

	testcases = int(input())
	expected_result = []
	student_result  = []
	inputs = []
	t = 0
	for i in range(testcases):
		temp = input().split()
		n = int(temp[0])
		data = []
		for tem_ in range(1,n):
			data.append(int(tem_))
		inputs.append(data)
		student = Solution()
		start = time.time()
		student_result.append(student.sum(data))
		end = time.time()
		t += (end-start)*1000

	for i in range(testcases):
		expected_result.append(int(input()))

	t = t / testcases

	IO().printLog(inputs,expected_result,student_result,t)




