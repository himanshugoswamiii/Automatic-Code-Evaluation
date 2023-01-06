
int**   teacher(int ** mat1 ,  int r1 , int c1 , int ** mat2 , int r2 , int c2,int option){

	if (option==0)
	{
		// Sum

		if (r1==r2&&c1==c2)
		{
			int ** result = new int*[r1];
			
			for (int i = 0; i < r1; ++i)
			
			{
				result[i] = new int[c1];
				for (int j = 0; j <c1 ; ++j)
				{
					result[i][j]=0;
				}
			}


			for (int i = 0; i < r1; ++i)
			{
				for (int j = 0; j < c1; ++j)
				{
					result[i][j]=mat1[i][j]+mat2[i][j];
				}
			}

			return result;


		}
		else return NULL;



	}

	else if (option==1)
	{
		if(c1==r1){
        
        // Multiplication 

		int ** result = new int*[r1];

		for (int i = 0; i < r1; ++i)
		{
			result[i] = new int[c2];
		}


		for (int i = 0; i < r1; ++i)
		{
			for (int j = 0; j < c2; ++j)
			{
				result[i][j]=0;
			}
		}

		for (int i = 0; i < r1; ++i)
		{
			for (int j = 0; j < c1; ++j)
			{
				for (int k = 0; k < c2; ++k)
				{
					result[i][k]+=mat1[i][j]*mat2[j][k];
				}
			}
		}


		return result;


		}
		else
			return NULL;
	}

	else if(option==2){

		int ** result = new int*[c1];

		for (int i = 0; i < c1; ++i)
		{
			result[i] = new int[r1];
		}

		for (int i = 0; i < r1; ++i)
		{
			for (int j = 0; j < c1; ++j)
			{
				result[j][i] = mat1[i][j];
			}
		}

		return result;



	}
	else{

		int ** result = new int*[c2];

		for (int i = 0; i < c2; ++i)
		{
			result[i] = new int[r2];
		}

		for (int i = 0; i < r2; ++i)
		{
			for (int j = 0; j < c2; ++j)
			{
				result[j][i] = mat2[i][j];
			}
		}

		return result;
		

	}



} 


bool check_matrix_equal(int ** mat1 , int ** mat2, int r,int c){
	
	if (mat1==NULL&&mat2==NULL)
	{
		return true;
	}
	else if (mat1==NULL||mat2==NULL)
	{
		return false;
	}
	else{

		for (int i = 0; i < r; ++i)
		{
			for (int j = 0; j < c ; ++j)
			{
				if (mat1[i][j]!=mat2[i][j])
				{
					return false;
				}
			}
		}
		return true;
	}
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
		
		int r1,c1,r2,c2;

		cin>>r1>>c1>>r2>>c2;

		
		int ** mat1 = new int*[r1];


		for (int i = 0; i < r1; ++i)
		{
			mat1[i] = new int[c1];

			for (int j = 0; j < c1; ++j)
			{
				cin>>mat1[i][j];		
			}
		}


		int ** mat2 = new int*[r2];


		for (int i = 0; i < r2; ++i)
		{
			mat2[i] = new int[c2];

			for (int j = 0; j < c2; ++j)
			{
				cin>>mat2[i][j];
			}
		}


		for (int i = 0; i < 4; ++i)
		{
			int ** result = teacher(mat1,r1,c1,mat2,r2,c2,i);
			
			int t1 = time(NULL);

			int ** student_result = student::solution(mat1,r1,c1,mat2,r2,c2,i);
			
			int t2 = time(NULL);

			time_+=t2-t1;

			int result_row,result_column;
			
			if(i<=1)
			{
				result_row = r1;
				result_column = c2;
			}
			else if (i==2)
			{
				result_row = c1;
				result_column = r1;
			}
			
			else
			{
				
				result_row = c2;
				result_column = r2;
			
			}

			bool equal = false;
			
			if(check_matrix_equal(result,student_result,result_row,result_column))
				{
					score++;
					equal = true;
				}
			string op;
			if(i==0)
				op = "Sum ";
			else if(i==1)
				op = "Product ";
			else if(i==2)
				op="Transpose matrix 1 ";
			else
				op = "Transpose matrix 2 ";

			cout<<"Testcase ["<<current+1<<" , "<<op<<"] -> "<<(equal?"Accepted":"Rejected")<<endl;
		}

		current++;
	}

	
	cout<<"#"<<endl;

	score = (score/(testcase*4))*100;

	cout<<score<<endl;

	cout<<"#"<<endl;

	time_=(time_/(testcase*4))*1000;

	cout<<time<<endl;

	
	return 0;
}