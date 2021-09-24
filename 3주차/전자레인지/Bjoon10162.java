import java.util.Scanner;

public class Bjoon10162 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int T = sc.nextInt();
		int A = 300;
		int B = 60;
		int C = 10;
		int cntA = 0;
		int cntB = 0;
		int cntC = 0;
		int addTime = 0; // tNum과 값을 비교할 변수

		if (T % 10 == 0) {
			while (T != addTime) {
				if (T >= addTime + A) {
					addTime = addTime + A;
					cntA += 1;
					continue;
				}
				else if (T >= addTime + B) {
					addTime += B;
					cntB += 1;
					continue;
				}
				else if (T >= addTime + C) {
					addTime += C;
					cntC += 1;
					continue;
				}
			}
			
			System.out.println(cntA + " " + cntB + " " + cntC);
		}
		else {
			System.out.println("-1");
		}
		sc.close();
	}
}
