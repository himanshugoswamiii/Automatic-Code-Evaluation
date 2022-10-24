public class IO{




	private static  int [] sort( int [] data  , int pass ){
 	 
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





	private  static void printLog(int [][] data , int [] pass ,  int [][] expected_result , int [][] student_result,double time){

		double score = 0;

	    System.out.println("#");
	    
	    for(int i = 0 ;i<expected_result.length;i++){
	    	
	    	boolean flag = true;
	    	for( int j = 0;j<expected_result[i].length;j++){
	    		if(expected_result[i][j] != student_result[i][j]){
	    			flag = false;
	    			break;
	    		}
	    	}

	    	if(flag)
	    		score++;

	    	System.out.println("( "+Arrays.toString(data[i]) +" : "+pass[i]+" )   -> "+ (flag?"Accepted":"Rejected"));
	    
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

		int [] pass = new int[testcases];

		
		int [][]  student_result = new int[testcases][];

		int [][] expected_result = new int[testcases][];
		
		double time = 0;

		Solution solution = new Solution();
		
		int current = 0;


		while(current < testcases)
		{
			
			int n = scanner.nextInt();
			
			int [] data = new int[n];
			
			for( int i = 0 ; i < n; i++ ) 

				data [ i ] = scanner.nextInt();


			int passN = scanner.nextInt();


			try{

				inputs[current] = data;

				pass[current] = passN;

				double start = System.currentTimeMillis();
				
				student_result [current]  = solution.sort(data,passN);
				expected_result[current] = IO.sort(data,passN);

				double end = System.currentTimeMillis();

				time += ( end - start );
			

			}
			catch(Exception e){


			}



			current ++;
		}


		time = ( time / testcases );

		IO.printLog(inputs,pass,expected_result,student_result,time);

	}
	
}