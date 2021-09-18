import java.util.Scanner;

public class Bjoon_2960 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();
		int K = sc.nextInt();
		boolean[] primeNum = new boolean[N + 1]; // 2부터 N까지 숫자가 필요한데 N까지만 하면 숫자상으로는 N-1 까지만 등록되기때문

		for (int i = 2; i <= N; i++) {
			primeNum[i] = true; // 초기화되지 않은 boolean (primitive) 멤버의 기본값은 false
		}

		int count = 0;

		for (int i = 2; i <= N; i++) {
			for (int j = i; j <= N; j += i) { // j는 한 번 돌 때마다 크기를 i 만큼 증가시켜 배수로 만들어 줌

				if (!primeNum[j]) { // N까지의 배수자리의 배열을 false로, !primeNum[j]의 의미는?
					continue;		//왜 여기서 컨티뉴를 해줘야하는거지?
				}

				count++;
				primeNum[j] = false;

				if (count == K) {
					System.out.println(j);
				}
			}
		}
	}

}
