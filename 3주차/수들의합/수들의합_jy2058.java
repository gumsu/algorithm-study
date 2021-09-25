package 수들의합;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 수들의합_jy2058 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long num = Long.parseLong(br.readLine());
        long sum = 0;
        int max = 0;
        for(int i=1; sum<=num; i++){
            sum += i;
            max = i;
        }
        System.out.println(max-1);
    }
    /*
        1. 입력받은 수보다 작거나 같을때까지 1부터 값을 더한다.
        2. 입력받은 값보다 크기 전까지 한번 더 for문 수행하기 때문에 결과를 -1 해준다.
     */
}
