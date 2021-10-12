import java.util.Scanner;

// 2947
public class 나무조각_s2jung {

    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);
        int[] wood = new int[5];
        for (int i = 0; i < 5; i++) {
            wood[i] = input.nextInt();
        }
        input.close();

        int temp = 0;
        while (isOrder(wood) == false) {
            for (int i = 0; i < wood.length-1; i++) {
                if (wood[i] > wood[i+1]) {
                    temp = wood[i];
                    wood[i] = wood[i+1];
                    wood[i+1] = temp;
                    for (int j = 0; j < wood.length; j++) {
                        System.out.print(wood[j] + " ");
                    }
                    System.out.println();
                }
            }
        }

    }
    
    // 순서대로 일때 true
    public static boolean isOrder(int[] num) {

        for (int i = 0; i < num.length-1; i++) {
            if (num[i] > num[i+1]) {
                return false;
            }
        }
        return true;
    }
}
