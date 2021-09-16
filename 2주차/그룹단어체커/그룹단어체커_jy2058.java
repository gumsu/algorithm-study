package 그룹단어체커;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 그룹단어체커_jy2058 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int num = Integer.parseInt(br.readLine());
        boolean[] arr = null;   // 알파벳 배열
        int cnt = 0;
        for(int i=0; i<num; i++){
            String str = br.readLine();
            arr = new boolean[26];
            cnt++;
            for(int j=0; j<str.length(); j++){
                char c = str.charAt(j);
                if(j != str.length() -1 && arr[c-97] == false && c != str.charAt(j+1)){
                    arr[c-97] = true;
                }else if(arr[c-97] == true){
                    cnt--;
                    break;
                }
            }
        }
        System.out.println(cnt);
    }
    /*
        1. 단어의 마지막이 아니고 && 이전에 나오지 않은 알파벳이며 && 다음 알파벳과 다르면
        해당 배열 true로 변경
         2. 해당 배열이 true일때 이미 나왔던 알파벳이니까 그룹단어 X
     */
}
