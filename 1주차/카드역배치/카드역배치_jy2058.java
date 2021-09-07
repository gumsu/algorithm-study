package 카드역배치;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 카드역배치_jy2058 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;
        int[] arr = new int[21];
        // 배열 1-20으로 초기화
        for(int i=1; i<21; i++){
            arr[i] = i;
        }

        for(int i=0; i<10; i++){
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            int cnt = (end - start) / 2;

            for(int j=0; j<=cnt; j++){
                int temp = arr[start + j];
                arr[start + j] = arr[end - j];
                arr[end - j ] = temp;
            }
        }
        for(int i=1; i<21; i++){
            System.out.print(arr[i]+ " ");
        }

    }
}
