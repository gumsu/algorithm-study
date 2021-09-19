import java.util.Scanner;

// 백준 10804
public class 카드역배치_s2jung {

    public static int[] card = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20};
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);
    
        int min, max;
        int n;

        for (int i = 0; i < 10; i++) {
            min = input.nextInt()-1;
            max = input.nextInt()-1;

            if ((max-min) % 2 == 0) {
                n = (max-min)/2;
            } else {
                n = (max-min)/2 + 1;
            }

            for (int j = 0; j < n; j++) {
                switch_card(min, max);
                min += 1;
                max -= 1;
                if (min == max || min > max) {
                    break;
                }
            }
        }
        
        input.close();

        for (int i = 0; i < card.length; i++) {
            System.out.print(card[i] + " ");
        }
    }

    public static void switch_card(int min, int max) {
        int temp;
        temp = card[min];
        card[min] = card[max];
        card[max] = temp;
    }
}
