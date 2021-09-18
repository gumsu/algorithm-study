package 수이어쓰기1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 수이어쓰기1_jy2058 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int cnt = 0;
        int sumNum = 1;
        int digit = 10;

        for(int i=1; i<=n; i++){
            if(i % digit == 0){
                sumNum++;
                digit *= 10;
            }
            cnt += sumNum;
        }
        System.out.println(cnt);
    }
}
