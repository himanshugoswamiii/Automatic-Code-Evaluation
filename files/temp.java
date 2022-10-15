import java.util.*;
import java.io.*;


class Solution
{

	int sum( int [] data ){

		Random ran = new Random();


		int sum = 0;
		for(int i: data)
			sum+=i;
		return sum+ran.nextInt(0,2);

	}


}

public class IO{



	private  static void printLog(int [][] data , int [] expected_result , int [] student_result,double time){

		double score = 0;

	    System.out.println("#");
	    
	    for(int i = 0 ;i<data.length;i++){
	    	
	    	if(expected_result [i] == student_result[i])
	    		score++;
	    	System.out.println(Arrays.toString(data[i]) + "  :  "+(expected_result[i] == student_result[i]));
	    
	    }

	    double finalperc = (score/data.length)*100;

	    
	    System.out.println("#");
	    
	    System.out.println(finalperc);
	    
	    System.out.println("#");
	    
	    System.out.println(Math.abs(time));

	}


	public static void main(String argc[]){
		
		Scanner scanner = new Scanner(System.in);
		
		int testcases = scanner.nextInt();

		
		int [][]  inputs = new int[testcases][]; 
		
		int [] student_result = new int[testcases];

		int [] expected_result = new int[testcases];
		
		double time = 0;

		Solution solution = new Solution();
		
		int current = 0;


		while(current < testcases)
		{
			
			int n = scanner.nextInt();
			
			int [] data = new int[n];
			
			for( int i = 0 ; i < n; i++ ) 

				data [ i ] = scanner.nextInt();


				

			try{

				inputs[current] = data;

				double start = System.currentTimeMillis();
				
				student_result [current]  = solution.sum(data);

				double end = System.currentTimeMillis();

				time += ( end - start );
			

			}
			catch(Exception e){


			}



			current ++;
		}

        current = 0;

		while(current < testcases){

			expected_result[current ] = scanner.nextInt();
			
			current ++;

		}

		time = ( time / testcases );

		IO.printLog(inputs,expected_result,student_result,time);

	}
	
}
