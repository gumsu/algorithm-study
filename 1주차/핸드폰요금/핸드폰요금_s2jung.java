import java.util.Scanner;

//1267
public class 핸드폰요금_s2jung {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        int n = input.nextInt();
        int[] n_arr = new int[n];
        for (int i = 0; i < n; i++) {
            n_arr[i] = input.nextInt();
        }
        input.close();

        int y_sum = 0, m_sum = 0;
        for (int i = 0; i < n; i++) {
            y_sum += (n_arr[i]/30 + 1) * 10;
            m_sum += (n_arr[i]/60 + 1) * 15;
        }

        if (y_sum == m_sum) {
            System.out.println("Y M " + y_sum);
        } else if (y_sum < m_sum) {
            System.out.println("Y " + y_sum);
        } else {
            System.out.println("M " + m_sum);
        }
    }
}
