import java.util.*;

class Solution{


public int [] sort( int [] data  , int pass ){
 	 
 	 if(pass  == 0) return data;

	int mypass = 0;

	for ( int i = 1 ; i < data.length ; i++ ){


		mypass ++;

		int k = i - 1  ;

		int ele = data [ i ];

		while( k>=0 && ele<data[k])
		{
			data [ k + 1 ] = data[k];
			k--;
		}

		data[k+1] = ele;

		if(mypass == pass)
			return data;



	}

	return data;

}


}