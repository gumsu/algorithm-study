package 특정거리의도시찾기;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class 특정거리의도시찾기_jy2058 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());    // 도시개수
        int m = Integer.parseInt(st.nextToken());    // 도로개수
        int k = Integer.parseInt(st.nextToken());    // 거리
        int x = Integer.parseInt(st.nextToken());    // 시작도시

        List<List<Integer>> adjList = new ArrayList<>();

        int dist[] = new int[n + 1];

        // 인접리스트 초기화
        for (int i=0; i<n+1; i++){
            adjList.add(new ArrayList<>());
        }

        for(int i=0; i<m; i++){
            st = new StringTokenizer(br.readLine());
            int v1 = Integer.parseInt(st.nextToken());
            int v2 = Integer.parseInt(st.nextToken());

            adjList.get(v1).add(v2);    // v1->v2 단방향
        }


        Queue<Integer> que = new LinkedList<>();
        que.offer(x);   // 시작도시
        dist[x] = 0;    // 시작도시->시작도시 거리 0

        // BFS
        while(!que.isEmpty()){
            int cur = que.poll();
            for(int i : adjList.get(cur)){
                if(dist[i] == 0){   // 방문한적 없으면
                    dist[i] = dist[cur] + 1;    // 출발도시에서 현재까지 거리 셋팅
                    que.offer(i);   // 큐에 다음 도시 추가
                }
            }
        }

        boolean check = false;
        for(int i=0; i<dist.length; i++){
            if(dist[i] == k && i != x){   // 최단거리이며 시작점이 아닐 때 도시 출력
                System.out.println(i);
                check = true;
            }
        }

        // 찾은도시 없으면 -1
        if(!check) System.out.println(-1);
    }
}
