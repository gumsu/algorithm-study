import java.util.Arrays;
import java.util.Scanner;

// 1654
public class 랜선자르기_s2jung {
    public static void main(String[] args) {
        
        Scanner input = new Scanner(System.in);
        int k = input.nextInt();    // 가지고 있는 랜선의 개수
        int n = input.nextInt();    // 필요한 랜선의 개수
        long[] kLan = new long[k];  // 가지고 있는 랜선 길이들
        for (int i = 0; i < k; i++) {
            kLan[i] = input.nextLong();
        }
        input.close();

        Arrays.sort(kLan);
        long start = 1;
        long end = kLan[k-1];
        long mid, divNum;

        while (start <= end) {
            
            mid = (start + end)/2;
            divNum = 0;
            for (int i = 0; i < kLan.length; i++) {
                divNum += kLan[i]/mid;
            }
            
            if (n <= divNum) {
                start = mid+1;
            } else {
                end = mid-1;
            }
        }

        System.out.println(end);

        // int divLen = 0;

        // for (int i = 0; i < k; i++) {
        //     divLen += kLan[i];
        // }
        // divLen = divLen / n;

        // while(cutLan(kLan, divLen) != n) {
        //     divLen--;
        // }
        // => 시간 초과

    }

    // len 길이씩 랜선을 자르면 몇 개의 랜선이 생기는지.
    // public static int cutLan(int[] lan, int len, int start, int end) {

    //     int result = 0;

    //     for (int i = 0; i < lan.length; i++) {
    //         result += lan[i]/len;
    //     }
        
    //     return result;
    // }
}
