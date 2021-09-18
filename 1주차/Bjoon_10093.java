import java.util.*;

public class Bjoon_10093 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		long a = sc.nextLong(); // int 안됨, 스캐너도 nextLong 으로!!!
		long b = sc.nextLong();

		if (a == b) {
			System.out.println("0");
		} else if (a > b) {
			System.out.println(a - b - 1);
			long tmp = a;	//a가 b보다 클 경우 a와 b의 순서를 바꾸는 작업
			a = b;
			b = tmp;
			for (long i = a + 1; i < b; i++) {
				System.out.print(i + " ");
			}
		} else {
			System.out.println(b - a - 1);
			for (long i = a + 1; i < b; i++) {
				System.out.print(i + " ");
			}
		}
	}
}
