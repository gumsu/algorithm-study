
import java.util.Scanner;

// 1978
public class 소수찾기_s2jung {
    public static void main(String[] args) {
        
        Scanner input = new Scanner(System.in);

        int n = input.nextInt();
        int[] num = new int[n];
        for (int i = 0; i < n; i++) {
            num[i] = input.nextInt();
        }
        input.close();

        // 입력받는 N개의 수가 1000 이하이므로 1000 크기의 배열 정의 및 초기화.
        int[] isPrime = new int[1001];
        isPrime[0] = isPrime[1] = 0;
        for (int i =2 ; i < 1001; i++) {
            isPrime[i] = i;
        }

        // 에라토스테네스의 체 - 소수판별
        for (int i = 2; i < 1001; i++) {
            if (isPrime[i] == 0) {
                continue;
            }
            for (int j = 2*i; j < 1001; j+=i) {
                isPrime[j] = 0;
            }
        }

        // 소수의 개수
        int count = 0;
        for (int i = 0; i < n; i++) {
            if (isPrime[num[i]] != 0) {
                count++;
            }
        }
        System.out.println(count);
    }
}
