package 색종이;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class 색종이_jy2058 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Boolean[][] book = new Boolean[100][100];
        for(Boolean[] a : book){
            Arrays.fill(a, false);
        }

        StringTokenizer st = null;
        int num = Integer.parseInt(br.readLine());
        int cnt = 0;
        for(int i=0; i<num; i++){
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            for(int j=x; j<x+10; j++){
                if(j > 100) return;
                for(int k=y; k<y+10; k++){
                    if(k>100) return;
                    if(!book[j][k]){
                        cnt++;
                        book[j][k] = true;
                    }
                }
            }

        }
        System.out.println(cnt);
    }
    /*
        1. 100,100 의 배열 생성 ( 도화지 )
        2. 입력받은 색종이 수만큼 반복
        3. 색종이의 좌표 ( 첫번째-> X, 두번째 -> Y )를 각 +10까지 for문 돌면서 색종이 배열 true로 변경 및 cnt 증가
        4. 이미 true일 경우 || 위치가 100을 넘어갈때는 건너뚜기
     */
}
