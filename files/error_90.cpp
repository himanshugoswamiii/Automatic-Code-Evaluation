#include<iostream>
using namespace std;
int main(){
	int n;
	cin>>n;
	long long sum = 10;
	for(int i =0;i<n;i++)
	{
		int ele;
		cin>>ele;
		sum+=ele;
	}
	cout<<sum<<endl;

}
