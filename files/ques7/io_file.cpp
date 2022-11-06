
int   teacher(int a , int b ){

	if (b==0) return a;

	return teacher(b,a%b);
}


int main()
{
	int testcase ;

	cin>>testcase;

	int current = 0;

	cout<<"#"<<endl; //printing log as well

	double time_ = 0;

	double score = 0; 
	
	while(current<testcase){
		
		int a,b;

		cin>>a>>b;

		int  result = teacher(a,b);

		int t1 = time(NULL);

		int student_result = solution(a,b);

		int t2 = time(NULL);

		time_+=t2-t1;

		bool equal = result==student_result;

		if(equal)
			score++;

		cout<<"[ "<<a<<" , "<<b<<" ] --> "<<student_result<<" ("<<(equal?"Accepted":"Rejected")<<" )"<<endl;

		current++;
	}

	
	cout<<"#"<<endl;

	score = (score/testcase)*100;

	cout<<score<<endl;



	cout<<"#"<<endl;

	time_=(time_/testcase)*1000;

	cout<<time<<endl;

	
	return 0;
}
