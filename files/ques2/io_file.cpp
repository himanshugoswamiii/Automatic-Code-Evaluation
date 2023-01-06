
int   teacher(int * data , int n ){

	
	int total = 0;
    
    for(int i = 0;i<n;i++){
        
        bool present = false;
        
        for(int j = total-1;j>=0;j--){
            
            if(data[j]==data[i]){
                
                present = true;
                break;
            }
        
        }
        if(!present)
        {
            
            data[total] = data[i];
            total++;
        }
        
    }
    
    return total;

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
		
		int n;
		
		cin>>n;
		
		int * array1 = new int[n];

		int * array2 = new int[n];

		int * input = new int[n];
		
		for (int i = 0; i < n; ++i)
		{
			cin>>array1[i];
			input[i]=array2[i] = array1[i];

		}

		int size1 = teacher(array1,n);

		int t1 = time(NULL); 

		int size2 = student::solution(array2,n);

		int t2 = time(NULL);

		time_+=(t2-t1);

		bool equal = true;

		if(size2!=size1){
			equal = false;
		}
		else{
			for (int i = 0; i < size1; ++i)
			{
				if(array1[i]!=array2[i]){
					equal = false;
					break;

				}
			}
		}

		if(equal)
			score++;

		cout<<"[ ";
		for (int i = 0; i < n-1; ++i)
		{
			cout<<input[i]<<" ,";
		}
		cout<<input[n-1]<<" ] ---> ";

		cout<<"[ ";

		for (int i = 0; i < size2-1; ++i)
		{
			cout<<array2[i]<<" ,";
		}
		
		if(size2>=1)
		
		cout<<array2[size2-1];

		cout<<" ]  --> "<<(equal?"Accepted":"Rejected")<<endl;

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
