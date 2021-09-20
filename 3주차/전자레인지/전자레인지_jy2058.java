package 전자레인지;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 전자레인지_jy2058 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int time = Integer.parseInt(br.readLine());
        int[] btnArr = {60*5, 60, 10};
        StringBuilder sb = new StringBuilder();
        int cnt = 0;
        if(time % 10 != 0){
            sb.append("-1");
        }else{
            for(int i=0; i<btnArr.length; i++){
                cnt = time / btnArr[i];
                time %= btnArr[i];

                sb.append(cnt).append(" ");
            }
        }
        System.out.println(sb.toString());
    }
    /*
        1. 3개의 수로 time이 나누어 떨어지지 않으면 -1 출력
        -> 최소로 나눌 수가 10으로 나누어 떨어져야 되니까, 나누어떨어지지 않는 수는 -1 출력
        2. 시간을 최대의 시간으로 나눈 후 해당 시간 출력
        3. 시간의 나머지 시간을 그 다음 시간의 몫으로 설정
     */
}
