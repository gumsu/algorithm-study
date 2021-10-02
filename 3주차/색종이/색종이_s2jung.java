import java.util.Scanner;

// 2563
public class 색종이_s2jung {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);
        int t = input.nextInt();

        int[][] board = new int[100][100];
        for (int i = 0; i < 100; i++) {
            for (int j = 0; j < 100; j++) {
                board[i][j] = 0;
            }
        }

        int w, h;
        for (int i = 0; i < t; i++) {
            w = input.nextInt();
            h = input.nextInt();
            for (int x = w; x < w+10; x++) {
                for (int y = h; y < h+10; y++) {
                    board[x][y]++;
                }
            }
        }
        input.close();

        int area = 0;
        for (int i = 0; i < 100; i++) {
            for (int j = 0; j < 100; j++) {
                if (board[i][j] != 0) {
                    area++;
                }
            }
        }
        System.out.println(area);
    }
}
