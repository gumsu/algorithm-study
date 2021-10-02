import java.util.Scanner;

// 13417
public class 카드문자열_s2jung {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);
        int t = input.nextInt();

        int n;
        String[] str = new String[t];
        for (int i = 0; i < t; i++) {
            n =  input.nextInt();
            char[] arr = new char[n];
            
            for (int j = 0; j < n; j++) {
                arr[j] = input.next().charAt(0);
            }

            str[i] = "";
            str[i] += arr[0];
            for (int j = 1; j < n; j++) {

                // str 맨 처음과 가져오는 문자를 비교해서 앞/뒤 배치를 결정.
                if (str[i].charAt(0) < arr[j]) {
                    str[i] += arr[j];
                } else {
                    str[i] = arr[j] + str[i];
                }
            }
        }
        input.close();

        for (int i = 0; i < t; i++) {
            System.out.println(str[i]);
        }
    }
}
