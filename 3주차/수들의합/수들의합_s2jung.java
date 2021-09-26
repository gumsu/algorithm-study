import java.util.Scanner;

// 1789
public class 수들의합_s2jung {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);
        long s = input.nextLong();
        input.close();

        long sum = 0;
        int n = 1;
        while (sum <= s) {
            sum += n;
            n++;
        }
        
        System.out.println(n-2);
    }
}
// int로 받으면 런타임 에러
// sum+n > s이 된 후 while 문 나옴 => 하나 이전으로 돌아가기 위해 n-1, n++한거 되돌리기 위해 -1 한번 더.
// 근의 공식 풀이 - https://blog.naver.com/ajy7424/222447451349