
int teacher(int *array , int m  , int key ){

	int low = 0;
	
	int high = m-1;
	
	while(low<=high){

		int mid = (low+high)/2;

		if (array[mid]==key)  return mid;
		
		else if (array[mid]<key)
			low = mid + 1;
		
		else
			high = mid  - 1;
	}
	
	return -1;
	
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
		
		int m;

		cin>>m;

		int * array = new int[m];

	

		for (int i = 0; i < m; ++i) cin>>array[i];
		
		int key ;

		cin>>key;



		int  result = teacher(array,m,key);

		int t1 = time(NULL);

		int student_result = student::solution(array , m , key);

		int t2 = time(NULL);

		time_+=t2-t1;

		bool equal = true;

		if(result == student_result)
			score++;

		cout<<"[ ";

		for (int i = 0; i < m-1; ++i)
		{
			cout<<array[i]<<",";
		}

		if(m-1>=0)
		cout<<array[m-1];

		cout<<" ] "<<" [ "<<key<<" ] ( "<<student_result<<" ) "<<" ( "<<(student_result==result?"Accepted":"Rejected")<<" )"<<endl;


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
