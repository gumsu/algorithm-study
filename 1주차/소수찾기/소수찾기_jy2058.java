package 소수찾기;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 소수찾기_jy2058 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int inputCnt = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int cnt = 0;
        while(st.hasMoreTokens()){
            int num = Integer.parseInt(st.nextToken());
            boolean yn = true;
            if(num == 1) continue;
            for(int i=2; i*i <= num; i++){
                if(num % i == 0){
                    yn = false;
                    break;
                }
            }
            if(yn){
                cnt++;
            }
        }
        System.out.println(cnt);

        /*
            소수 : 2부터 판별하는 수까지 나눠서 나머지가 0이 안 나오는 수 (약수가 2개 - 1과 자기자신)
            풀이 1. 해당 숫자의 절반까지 확인 -> 절반을 초과하는 숫자에서 나머지가 0인 숫자는 없다.
            풀이 2. 해당 숫자의 루트값까지 확인 -> 약수의 중심을 구함.
         */
    }
}
