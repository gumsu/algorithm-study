import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_2577_jy2058 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int A = Integer.parseInt(br.readLine());
        int B = Integer.parseInt(br.readLine());
        int C = Integer.parseInt(br.readLine());

        int[] arr = new int[10];
        String sum = String.valueOf(A*B*C);
        for(int i=0; i<sum.length(); i++){
            arr[(sum.charAt(i) - '0')]++;
        }
        for(int a : arr){
            System.out.println(a);
        }
    }
}
