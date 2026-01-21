import java.util.*;
class Solution {
    public int solution(int[][] jobs) {
        Arrays.sort(jobs, Comparator.comparingInt(a->a[0]));
        PriorityQueue<int[]> q = new PriorityQueue<>(Comparator.comparingInt(a->a[1]));
        
        int time=0, index=0, total=0, done=0;
        while(done < jobs.length){
            while(index < jobs.length && jobs[index][0]<=time) q.offer(jobs[index++]);
            
            if(!q.isEmpty()){
                int[] job = q.poll();
                time += job[1];
                total += time - job[0];
                done++;
            }
            else time++;
        }
        return total/jobs.length;
    }
}