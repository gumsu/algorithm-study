import java.util.*;

public class Bjoon_1267 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int call = sc.nextInt(); // 통화 갯수
		int[] calltime = new int[call]; // 통화 개수에 해당하는 양의 통화시간 배열 생성

		for (int i = 0; i < call; i++) { // calltime배열에 각 시간 입력
			calltime[i] = sc.nextInt();
		}
		
		int Y = 0;
		int M = 0;
		
		for (int i=0; i<call; i++) {
			Y +=  ((calltime[i] / 30) + 1) * 10;
			M +=  ((calltime[i] / 60) + 1) * 15;
		}
		
		if (Y > M) {
			System.out.println("M " +M);
		} else if (M > Y) {
			System.out.println("Y " +Y);
		} else {
			System.out.println("Y M " +M);
		}
	}

}
