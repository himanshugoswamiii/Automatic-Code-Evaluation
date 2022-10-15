import java.util.Scanner;
import java.util.Random;
public class testcase{
	public static void main(String argc[]){
		Scanner scanner = new Scanner(System.in);
		int n = scanner.nextInt();
		Random ran = new Random();
		System.out.println(n);
		for(int i =0;i<n;i++){
			System.out.println(ran.nextInt(1,100));
		}
	}
}
