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

public static void main(String [] argc ){

	Scanner scanner = new Scanner ( System.in );

	System.out.println("Enter value of n ");

	int n = scanner.nextInt();

	int [] data = new int [ n ];

	for ( int i = 0 ;i<n;i++)
		data[i] = scanner.nextInt();

	System.out.println("Enter pass Number ");

	int pass = scanner .nextInt();



	int [] result = new Solution().sort(data,pass);

	for(int temp : result)
		System.out.println(temp);



}


}