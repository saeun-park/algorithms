import java.util.*;
class Solution {
    
    class Word{
        String word;
        int count;
        Word(String word, int count){
            this.word = word;
            this.count = count;
        }
    }
    private int getDiffCount(String word1, String word2){
        int diff = 0;
        for(int i=0; i<word1.length(); i++){
            if(word1.charAt(i) != word2.charAt(i)){
                diff++;
            }
        }
        return diff;
    }
    
    public int solution(String begin, String target, String[] words) {
        Queue<Word> q = new ArrayDeque<>();
        q.offer(new Word(begin, 0));
        boolean[] visited = new boolean[words.length];
        
        while(!q.isEmpty()){
            Word cur = q.poll();
            String word = cur.word;
            int count = cur.count;
            
            for(int i=0; i<words.length; i++){
                if(word.equals(target)) return count;
                if(!visited[i] && getDiffCount(word, words[i])==1){
                    visited[i] = true;
                    q.offer(new Word(words[i], count+1));
                    
                }
            }
        }
        return 0;
    }
}