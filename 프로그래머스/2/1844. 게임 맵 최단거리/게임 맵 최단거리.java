import java.util.*;

class Solution {
    public int solution(int[][] maps) {
        int n = maps.length;
        int m = maps[0].length;
        int[] dr = new int[]{0, 0, 1, -1};
        int[] dc = new int[]{1, -1, 0, 0};
        
        boolean[][] visited = new boolean[n][m];
        visited[0][0] = true;
        
        Queue<int[]> q = new ArrayDeque<>();
        q.offer(new int[]{0, 0, 1});
        
        // 노드 저장
        while(!q.isEmpty()){
            int[] cur = q.poll();
            int r = cur[0];
            int c = cur[1];
            int dist = cur[2];
            
            if(r == n-1 && c == m-1) return dist;
            for(int i=0; i<4; i++){
                int nr = r + dr[i];
                int nc = c + dc[i];
                
                if(nr>=0 && nc>=0 && nr<n && nc<m && maps[nr][nc]==1){
                    if(!visited[nr][nc]){
                        visited[nr][nc] = true;
                        q.offer(new int[]{nr, nc, dist+1});
                    }
                }
            }
        }
        
        
        return -1;
        
    }
}