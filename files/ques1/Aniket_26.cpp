#include<iostream>
#include<ctime>
using namespace std;

double solution(int n){

	double ans = 0;

	for( int i = 1;i<=n;i++)
		ans += i%2 == 0 ? -(1./i) : (1./i);

	return ans;


}

