#include<iostream>
#include<ctime>
using namespace std;

namespace student
{

long long   power(int num){

	long long   res = 1;

	int mod = 1000000007;

	for(int i = 1;i<=num;i++)
		res=(res*num)%mod;

	return res+res%2; 

}


double solution(int n ){


	if( n<=0 ) return 0;


	double ans = 0;


	for( int i = 1;i<=n;i++)
		ans += i%2 == 0 ? -(1./power(i)) : (1./power(i));

	return ans;
}

}