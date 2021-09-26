import java.util.Scanner;

// 1475
public class 방번호_s2jung {
    public static void main(String[] args) {
        
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        input.close();

        // 0일 때는 무조건 세트 1개 필요 -> 종료.
        if (n == 0) {
            System.out.println("1");
            return;
        }

        int[] num = new int[10];
        for (int i = 0; i < 10; i++) {
            num[i] = 0;
        }

        while (n > 0) {
            num[n%10]++;
            n = n / 10;
        }

        int max = 0;
        for (int i = 0; i < 10; i++) {
            if (i == 6 || i == 9) {
                continue;
            }
            if (max < num[i]) {
                max = num[i];
            }
        }

        int sn = num[6] + num[9];
        if (sn % 2 == 0) {
            if (sn/2 > max) {
                max = sn/2;
            }
        } else {
            if (sn/2+1 > max) {
                max= sn/2+1;
            }
        }
        System.out.println(max);
    }
    
}
