import java.util.*;
class Solution {
    public int solution(int n, int[][] wires) {
        int answer = 100;
        for(int i=0; i<wires.length; i++){
            List<List<Integer>> graph = new ArrayList<>();
            for(int j=0; j<=n; j++){
                graph.add(j, new ArrayList<>());
            }
            for(int j=0; j<wires.length; j++){
                if(i==j) continue;
                int a = wires[j][0];
                int b = wires[j][1];
                graph.get(a).add(b);
                graph.get(b).add(a);
            }
            boolean[] visited = new boolean[n+1];
            int count = dfs(1, graph, visited);
            int answer1 = Math.abs(n - 2*count);
            answer = Math.min(answer1, answer);
        }
        return answer;
    }
    private int dfs(int node, List<List<Integer>> graph, boolean[] visited){
        visited[node] = true;
        int count = 1;

        for(int next : graph.get(node)){
            if(!visited[next]){
                count += dfs(next, graph, visited);
            }
        }
        return count;
    }
}