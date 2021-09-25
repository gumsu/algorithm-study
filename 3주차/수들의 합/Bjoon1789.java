package java_ddwu;

import java.util.Scanner;

public class Bjoon1789 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		long S = sc.nextLong(); // 주어진 수, 넥스트롱 으로 해야함.
		long add = 0; // S와 비교할 수
		long cnt = 0; // 자연수의 갯수

		while (S > add) {
			for (long i = 1; ; i++) {	//범위를 지정 안해주니 1을 입력해도 풀력됨.
				add += i;
				cnt++;
				if (add > S) { // 더해간 합이 S를 처음으로 초과할 경우 현재까지 더한 자연수의 갯수에서 -1
					cnt--;
					break;
				}
			}
		}

		System.out.println(cnt);
	}

}