




bool equal(double value1 , double value2){

	double diff = value1 - value2;

	if(diff<0)
		diff = -diff;


	return diff<0.0001;

}


void printLog(int n , int * input , double * student , double * expected , double second ){


	cout<<"#"<<endl;


	double score = 0;
	
	for( int i = 0;i<n;i++){
		
		bool result = equal(student[i],expected[i]);

		if(result)
			score++;

		cout<<"( " << input[i]<<" ) [ "<<student[i]<<" ]" <<" -> "<<(result?"Accepted":"Rejected")<<endl;


	}

	cout<<"#"<<endl;

	cout<<(score/n)*100<<endl;

	cout<<"#"<<endl;

	cout<<second*1000<<endl;



}


double teacher(int n ){

	double ans = 0;


	for( int i = 1;i<=n;i++)
		ans += i%2 == 0 ? -(1./i) : (1./i);

	return ans;
}


int main()
{
	int testcase ;

	cin>>testcase;

	int current = 0;

	int * input =  new int[testcase];

	double * student_result  = new double[testcase];

	double * expected = new double[testcase]; 

	double time_ = 0; 
	while(current<testcase){

		int n;
		
		cin>>n;

		double ex = teacher(n);
		
		int t1 = time(NULL); 


		double ans = solution(n);

		int t2 = time(NULL);


		time_+=t2 - t1; 

		input[current] = n;

		student_result[current] = ans;

		expected[current] = ex;

		current++;
	}

	time_/=testcase;

	printLog(testcase,input,student_result,expected,time_);

	return 0;
}

