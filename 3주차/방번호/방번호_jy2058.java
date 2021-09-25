package 방번호;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class 방번호_jy2058 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String room = br.readLine();
        int[] arr = new int[9];
        for(int i=0; i<room.length(); i++){
            int num = room.charAt(i) - '0';
            if(num == 6 || num == 9){
                arr[6]++;
            }else {
                arr[num]++;
            }
        }

        int sixNine = arr[6];
        if(sixNine % 2 == 0){
            arr[6] = sixNine / 2;
        }else{
            arr[6] = sixNine / 2 + 1;
        }

        System.out.println(Arrays.stream(arr).max().getAsInt());
    }
    /*
        1. 6과 9는 같이 사용하니까 배열 6에 한번에 저장
        2. 0~8까지 9개의 배열 생성
        3. 입력받은 방번호 배열을 차례대로 돌면서 해당 번호를 arr 배열에 +1
            6또는 9일땐 arr[6] 배열에 +1
        4. 6또는 9의 셋트 갯수 구해서 arr[6]에 저장
            -> 6과 9를 합친 값이 2로 나누어 떨어지면 한세트를 사용하는 것이기 때문에 2로 나눈 값
            2로 나누어 떨어지지 않으면 두세트를 사용하는 거니까 +1
        5. 배열에서 max 값을 구하면 세트의 갯수가 됨.

     */
}
