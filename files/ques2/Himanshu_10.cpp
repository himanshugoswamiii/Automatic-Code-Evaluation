#include<iostream>
#include<ctime>
using namespace std;

int   solution(int * data , int n ){

	
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
    
    return total+1;

}
