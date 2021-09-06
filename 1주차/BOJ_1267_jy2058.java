import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_1267_jy2058 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int cnt = Integer.parseInt(br.readLine());
        StringTokenizer st = null;
        int Y_TIME = 30, Y_PRICE = 10, M_TIME = 60, M_PRICE = 15, y_sum = 0, m_sum = 0;
        st = new StringTokenizer(br.readLine());
        while (st.hasMoreTokens()) {
            int time = Integer.parseInt(st.nextToken());
            y_sum += (time / Y_TIME +1) * Y_PRICE;
            m_sum += (time / M_TIME +1) * M_PRICE;
        }
        if (y_sum < m_sum) {
            System.out.println("Y " + y_sum);
        } else if (y_sum > m_sum) {
            System.out.println("M " + m_sum);
        } else {
            System.out.println("Y M " + y_sum);
        }
    }
}
