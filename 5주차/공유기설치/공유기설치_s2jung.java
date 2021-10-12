import java.util.Scanner;
import java.util.Arrays;

// 2110
public class 공유기설치_s2jung {

    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);
        int n = input.nextInt();    // 집의 개수
        int c = input.nextInt();    // 공유기 개수
        int[] home = new int[n];    // 집의 좌표
        for (int i = 0; i < n; i++) {
            home[i] = input.nextInt();
        }
        input.close();

        Arrays.sort(home);
        long start = 1;
        long end = home[n-1];
        long mid, cnt;  // mid : 공유기 사이 최대거리, cnt : 사용된 공유기 개수

        while (start <= end) {
            
            mid = (start + end)/2;
            cnt = 1;
            for (int i = 0; i < home.length; i++) {
                for (int j = 1; i+j < home.length; j++) {
                    if (home[i] + mid <= home[i+j]) {    // 공유기 사이의 거리가 mid 이상
                        cnt++;
                        i = i+j-1;
                        break;
                    }
                }
            }
            
            if (c <= cnt) {
                start = mid+1;
            } else {
                end = mid-1;
            }
        }

        System.out.println(end);
    
    }
    
}

// https://blog.naver.com/gkfla1017/222238610330
