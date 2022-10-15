import java.util.Scanner;
public class aniket{
	public static void main(String argc[]){


		Scanner scanner = new Scanner(System.in);
		int n = scanner.nextInt();
		long sum = 0;
		for(int i=0;i<n;i++)
			sum+=scanner.nextInt();
		System.out.println(sum);
	}
}
