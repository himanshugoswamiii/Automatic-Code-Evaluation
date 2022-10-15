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