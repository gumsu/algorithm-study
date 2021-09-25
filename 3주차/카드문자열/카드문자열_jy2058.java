package 카드문자열;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 카드문자열_jy2058 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = null;
        int T = Integer.parseInt(br.readLine());
        for(int i=0; i<T; i++){
            int cardCnt = Integer.parseInt(br.readLine());
            String str = br.readLine().replaceAll(" ", "");
            sb = new StringBuilder();
            for(int j=0; j<str.length(); j++){
                char target = str.charAt(j);
                if(sb.length() < 1 || sb.charAt(0) >= target){
                    sb.insert(0, target);
                }else{
                    sb.append(target);
                }
            }
            System.out.println(sb.toString());
        }
    }
    /*
        1. 입력받은 문자열을 공백제거
        2. 문자열의 길이만큼 for문 돌면서 문자열의 첫번째 값과 현재 문자의 값을 비교
            -> 문자가 맨 앞 또는 맨뒤로만 추가 되기 떄문에 맨 앞과 비교.
        3. target 문자가 저장한 문자열의 첫 글자보다 작으면 제일 앞에 추가, 저장된 문자가 없을때도 앞에추가( 조건절 indexOutOf 방지)
           그 외의 경우는 모두 뒤에 추가
     */
}
