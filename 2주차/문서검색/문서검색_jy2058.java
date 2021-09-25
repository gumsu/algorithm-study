package 문서검색;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 문서검색_jy2058 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String book = br.readLine();
        String word = br.readLine();
        int wordLen = word.length();
        int cnt = 0;

        for(int i=0; i<book.length()-wordLen+1; i++){
            if(book.substring(i, i+wordLen).equals(word)){
                cnt++;
                i += wordLen -1;
            }
        }
        System.out.println(cnt);
    }
    /*
        1. 문서 전체 길이에서 단어 크기를 뺀 크기만큼 for문 수행
        2. 해당 인덱스부터 단어크기만큼 문서에서 추출후 단어와 같은 문자열인지 비교
        3. 같을 경우 cnt 1 증가, 인덱스를 단어크기만큼 증가
            -> 단어의 끝 다음부터 찾으면 되니까
        4. for 증감식에 의해 인덱스가 증가하니까 인덱스를 -1 해줌.
     */
}
