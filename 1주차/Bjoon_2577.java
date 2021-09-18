import java.util.*;

public class Bjoon_2577 {

	public static void main(String[] args) {
			Scanner sc = new Scanner(System.in);
			int [] num = new int [10];
			
			int A = sc.nextInt();
			int B = sc.nextInt();
			int C = sc.nextInt();
			int sum = A*B*C;
			
			while(sum>0) {
				num[sum%10]++;	//10으로 나눈 나머지를 통해 배열 자리에 해당하는 숫자를 1씩 더해줌
				sum /= 10;
			}
			for(int i=0; i<10; i++) {
			System.out.println(num[i]);
			}
		}
	}
