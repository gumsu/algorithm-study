import java.util.Scanner;

// 1929
public class 소수구하기_s2jung {
    public static void main(String[] args) {
        
        Scanner input = new Scanner(System.in);

        int m = input.nextInt();
        int n = input.nextInt();
        input.close();

        //최대값+1 크기의 배열 선언 및 초기화.
        int[] num = new int[n+1];
        num[0] = num[1] = 0;
        for (int i = 2; i < n+1; i++) {
            num[i] = i;
        }

        //에라토스테네스의 체 - 소수판별
        for (int i = 2; i < n+1; i++) {
            if (num[i] == 0) {
                continue;
            }
            for (int j = 2*i; j < n+1; j+=i) {
                num[j] = 0;
            }
        }

        // m부터 배열 탐색 시작, 소수 출력
        for (int i = m; i < n+1; i++) {
            if (num[i] != 0) {
                System.out.println(num[i]);
            }
        }
    }
}