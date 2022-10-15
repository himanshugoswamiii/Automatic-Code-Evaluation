
import java.util.*;
import java.io.*;

class Solution{


   final int mod = 1_0000_00007;
	public int sum( int [] data  ){


		long sum = 0;

		for(int num : data)
			sum = ( sum + num )%mod ;

		return (int)sum;


	}



}