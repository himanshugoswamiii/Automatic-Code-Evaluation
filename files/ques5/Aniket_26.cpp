#include<iostream>
#include<ctime>
using namespace std;

namespace student

{

int *  solution(int * array1 , int m , int * array2 , int n ){

	int * result = new int[m+n];

	int i = 0,j=0;

	int k = 0;

	while(i<m&&j<n){

		if (array1[i]<=array2[j])
			result[k++] = array1[i++]; 
		else
			result[k++] = array2[j++];

	}

	while(i<m)
		result[k++] = array1[i++];

	while(j<n)
		result[k++] = array2[j++];

	return result;
}

}