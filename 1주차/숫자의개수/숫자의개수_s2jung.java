import java.util.Scanner;

//2577
public class 숫자의개수_s2jung {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);
        
        int n1 = input.nextInt();
        int n2 = input.nextInt();
        int n3 = input.nextInt();

        input.close();

        if (n1 < 100 || n2 < 100 || n3 < 100 || n1 > 1000 || n2 > 1000 || n3 > 1000) {
            return;
        }

        int n = n1*n2*n3;

        int[] num = new int[10];
        for (int i = 0; i < 10; i++) {
            num[i] = 0;
        }

        while (n > 0) {
            num[n%10]++;
            n = n/10;
        }
        
        for (int i = 0; i < 10; i++) {
            System.out.println(num[i]);
        }
    }
}
