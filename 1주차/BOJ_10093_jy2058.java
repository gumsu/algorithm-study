import org.omg.Messaging.SyncScopeHelper;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_10093_jy2058 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        long A = Long.parseLong(st.nextToken());
        long B = Long.parseLong(st.nextToken());
        long start = 0, end = 0;
        if (A > B){
            System.out.println(A-B-1);
            start = B;
            end = A;
        }else if(A < B){
            System.out.println(B-A-1);
            start = A;
            end = B;
        }else{
            System.out.println(0);
        }
        for (long i = start + 1; i < end; i++) {
            System.out.print(i + " ");
        }
    }
}
