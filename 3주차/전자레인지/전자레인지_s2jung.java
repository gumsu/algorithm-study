import java.util.Scanner;

// 10162
public class 전자레인지_s2jung {
    public static void main(String[] args) {
        
        Scanner input = new Scanner(System.in);
        int t = input.nextInt();
        input.close();

        if (t % 10 != 0) {
            System.out.println("-1");
            return;
        }

        int[] t_arr = {300, 60, 10};
        int[] t_btn = {0, 0, 0};
        int t_sum = 0;
        
        for (int i = 0; i < t_arr.length; i++) {
            while (t_sum <= t) {
                t_sum += t_arr[i];
                t_btn[i]++;
            }
            t_btn[i]--;
            t_sum -= t_arr[i];
        }
        
        for (int i = 0; i < t_btn.length; i++) {
            System.out.print(t_btn[i] + " ");
        }
    }
}
