package 바이러스;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 바이러스_jy_2058 {
    static int cnt = 0; // 감염된 pc 개수
    static int[][] arr;    // 그래프 행렬
    static boolean[] check;     // 방문여부 배열
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int pcCnt = Integer.parseInt(br.readLine()); // pc 개수
        int lineCnt = Integer.parseInt(br.readLine()); // 간선 개수

        arr = new int[pcCnt+1][pcCnt+1];
        check = new boolean[pcCnt+1];

        StringTokenizer st = null;
        for(int i=0; i<lineCnt; i++){   // 연결정보 저장
            st = new StringTokenizer(br.readLine());
            int v1 = Integer.parseInt(st.nextToken());
            int v2 = Integer.parseInt(st.nextToken());

            arr[v1][v2] = 1;
            arr[v2][v1] = 1;
        }
        dfs(1);
        System.out.println(cnt-1);  // 펏번째 pc 제외
    }

    // 깊이 탐색 메서드
    private static void dfs(int v) {
        if(check[v]) return;    // 방문했을경우 종료
        check[v] = true;    // 방문처리
        cnt++;
        for(int i=1; i<arr[v].length; i++){ // 인접행렬 탐색
            if(arr[v][i] == 1 && !check[i]) // 연결된 정점이면서 방문하지 않았을경우
            dfs(i); // 재귀
        }
    }
}
