#include<iostream>
#include<ctime>
using namespace std;


namespace student
{

int**   solution(int ** mat1 ,  int r1 , int c1 , int ** mat2 , int r2 , int c2,int option){

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

}