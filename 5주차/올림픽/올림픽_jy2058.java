package 올림픽;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 올림픽_jy2058 {
    static int num;     // 국가 수
    static int k;    // 알고자하는 순위

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        num = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        Nation[] nation = new Nation[num];
        for(int i=0; i<num; i++){
            nation[i] = new Nation();   // 국가별 메달 객체 생성
            st = new StringTokenizer(br.readLine());
            nation[i].no = Integer.parseInt(st.nextToken());    // 국가 번호
            nation[i].gold = Integer.parseInt(st.nextToken());  // 금메달 수
            nation[i].silver = Integer.parseInt(st.nextToken());    // 은메달 수
            nation[i].bronze = Integer.parseInt(st.nextToken());    // 동메달 수
        }

        int result = rank(nation);
        System.out.println(result);
    }

    // 랭킹 구하는 함수
    public static int rank(Nation[] nation){
        int rank = 1;   // 랭킹
        int target = 0; // 랭킹 구해야 할 국가
        for(int i=0; i<num; i++){
            if(nation[i].no == k ){
                target = i;
            }
        }
        for(int j=0; j<num; j++){
            // target보다 금메달 많으면 rank++
            if(nation[j].gold > nation[target].gold){
                rank++;
            // 금메달 개수가 같고 은메달이 많으면 rank++
            }else if(nation[j].gold == nation[target].gold && nation[j].silver > nation[target].silver){
                rank++;
            // 금메달, 은메달 개수가 같고 동메달이 많으면 rank++
            }else if(nation[j].gold == nation[target].gold && nation[j].silver == nation[target].silver && nation[j].bronze > nation[target].bronze){
                rank++;
            }
        }
        return rank;
    }

    // 국가별 메달 정보 객체 클래스
    private static class Nation{
        int no;
        int gold;
        int silver;
        int bronze;
    }
}
