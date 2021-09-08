import java.util.*;

public class Bjoon_1978 {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int num1 = sc.nextInt();	//수의 개수
		int sosuCnt = 0;
		int cnt = 0;
		
		for (int i=1; i<=num1; i++) {
			int num2 = sc.nextInt();	//입력받는 수
			sosuCnt = 0;
			
			for (int j=1; j<=num2; j++) {
				if(num2 % j == 0) {
					sosuCnt++;
				}
			}
			if(sosuCnt == 2)	//나눠지는 수가 1과 자기자신, 즉 2개만 있는 경우
				cnt++;
		}
		System.out.println(cnt);
	}
}
