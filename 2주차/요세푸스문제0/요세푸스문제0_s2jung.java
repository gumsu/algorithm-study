import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

// Queue 이용
public class 요세푸스문제0_s2jung {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        int k = input.nextInt();
        input.close();
        
        Queue<Integer> que = new LinkedList<Integer>();
        for (int i = 0; i < n; i++) {
            que.add(i+1);
        }
        
        int temp;
        System.out.print("<");
        while(!que.isEmpty()) {
            // k-1 번째까지의 값을 모두 뒤로 보내줌.
            for (int i = 0; i < k-1; i++) {
                temp = que.poll();
                que.offer(temp);
            }
            if (que.size() == 1) {
                System.out.print(que.poll() + ">");
                break;
            }
            System.out.print(que.poll() + ", ");
        }
    }
}
