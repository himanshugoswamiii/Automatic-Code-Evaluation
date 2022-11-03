
void printLog(int n , string * input , char * input_ , int * student , int * expected , double second ){


	cout<<"#"<<endl;


	double score = 0;
	
	for( int i = 0;i<n;i++){
		
		bool result = student[i]==expected[i];

		if(result)
			score++;

		cout<<"( " << input[i]<<" , "<<input_[i]<<" ) [ "<<student[i]<<" ]" <<" -> "<<(result?"Accepted":"Rejected")<<endl;


	}

	cout<<"#"<<endl;

	cout<<(score/n)*100<<endl;

	cout<<"#"<<endl;

	cout<<second*1000<<endl;



}


int  teacher(string in  , char character ){

	int ans = 0;

	for(int i = 0;i<in.length();i++){

		if(in[i]==character)
			ans++;
	
	}
	return ans;
}


int main()
{
	int testcase ;

	cin>>testcase;

	int current = 0;

	string * input =  new string[testcase];

	char * input_ = new char[testcase];

	int * student_result  = new int[testcase];

	int  * expected = new int[testcase]; 

	double time_ = 0; 
	
	while(current<testcase){
		
		string in;
		
		cin>>in;

		char character;

		cin>>character;



		int ex = teacher(in,character);
		
		int t1 = time(NULL); 


		int ans = solution(in,character);

		int t2 = time(NULL);


		time_+=t2 - t1; 

		input[current] = in;

		input_[current] = character;

		student_result[current] = ans;

		expected[current] = ex;

		current++;
	}

	time_/=testcase;

	printLog(testcase,input,input_,student_result,expected,time_);

	return 0;
}

