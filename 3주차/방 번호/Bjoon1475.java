package java_ddwu;

import java.util.Scanner;

public class Bjoon1475 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		String sNum = sc.next();
		int[] numArr = new int[sNum.length()]; // input 문자열 길이만큼 배열 준비.
		for (int i = 0; i < sNum.length(); i++) {
			numArr[i] = sNum.charAt(i) - '0'; // i=0 일때, '1' - '0' = 1 이됨.
		}

		int cnt0 = 0;
		int cnt1 = 0;
		int cnt2 = 0;
		int cnt3 = 0;
		int cnt4 = 0;
		int cnt5 = 0;
		int cnt6n9 = 0;
		int cnt7 = 0;
		int cnt8 = 0;

		for (int i = 0; i < sNum.length(); i++) {
			if (numArr[i] == 0) {
				cnt0++;
			} 
			else if (numArr[i] == 1) {
				cnt1++;
			} 
			else if (numArr[i] == 2) {
				cnt2++;
			} 
			else if (numArr[i] == 3) {
				cnt3++;
			} 
			else if (numArr[i] == 4) {
				cnt4++;
			} 
			else if (numArr[i] == 5) {
				cnt5++;
			} 
			else if (numArr[i] == 6) {
				cnt6n9++;
			} 
			else if (numArr[i] == 7) {
				cnt7++;
			} 
			else if (numArr[i] == 8) {
				cnt8++;
			} 
			else if (numArr[i] == 9) {
				cnt6n9++;
			}
		}

		int max = cnt0;
		
		if (max < cnt1) {
			max = cnt1;
		}
		if (max < cnt2) {
			max = cnt2;
		}
		if (max < cnt3) {
			max = cnt3;
		}
		if (max < cnt4) {
			max = cnt4;
		}
		if (max < cnt5) {
			max = cnt5;
		}
		if (max < cnt7) {
			max = cnt7;
		}
		if (max < cnt8) {
			max = cnt8;
		}
		if (max < cnt6n9) {
			max = cnt6n9;
		}
		
		System.out.println(max);
		
		sc.close();
	}

}
