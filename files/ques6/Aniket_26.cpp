#include<iostream>
#include<ctime>
using namespace std;

namespace student
{
	int solution(int *array , int m  , int key ){

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

}