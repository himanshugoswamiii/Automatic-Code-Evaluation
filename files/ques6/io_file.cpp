
int   teacher(int * array1 , int m  ){

	int low = 0;
	
	int high = m-1;
	
	while(low<=high){
	
	
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
		
		int m,n;

		cin>>m>>n;

		int * array1 = new int[m];

		int * array2 = new int[n];

		for (int i = 0; i < m; ++i) cin>>array1[i];
		
		for (int i = 0; i < n; ++i) cin>>array2[i];



		int * result = teacher(array1,m,array2,n);

		int t1 = time(NULL);

		int * student_result = solution(array1 , m , array2,n);

		int t2 = time(NULL);

		time_+=t2-t1;

		bool equal = true;

		for (int i = 0; i < m+n; ++i)
		{
			if (result[i]!=student_result[i])
			{
				equal = false;
				break;
			}
		}

		if(equal)
			score++;

		cout<<"[ ";

		for (int i = 0; i < m-1; ++i)
		{
			cout<<array1[i]<<",";
		}

		cout<<array1[m-1]<<" ] , [";

		for (int i = 0; i < n-1; ++i)
		{
			cout<<array2[i]<<",";
		}

		cout<<array2[n-1]<<" ] --> [";

		for (int i = 0; i < m+n-1; ++i)
		{
			cout<<student_result[i]<<",";
		}

		cout<<student_result[m+n-1]<<" ] ( "<<(equal?"Accepted":"Rejected")<<" )"<<endl;


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
