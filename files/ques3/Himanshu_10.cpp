#include<iostream>
#include<ctime>
using namespace std;

int solution(string in , char character ){

	int ans = 0;

	for(int i = 0;i<in.length();i++){

		if(in[i]==character)
			ans++;
	
	}
	return ans+1;

}