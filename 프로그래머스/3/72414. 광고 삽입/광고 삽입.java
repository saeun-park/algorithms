class Solution {
    public String solution(String play_time, String adv_time, String[] logs) {
        int play = toSec(play_time);
        int adv = toSec(adv_time);
        long[] times = new long[play + 2];

        for (String log : logs) {
            int start = toSec(log.split("-")[0]);
            int end = toSec(log.split("-")[1]);
            times[start]++;
            times[end]--;
        }

        for (int i = 1; i <= play; i++) times[i] += times[i - 1];
        for (int i = 1; i <= play; i++) times[i] += times[i - 1];

        long max = times[adv - 1], start = 0;
        for (int i = adv; i <= play; i++) {
            long total = times[i] - times[i - adv];
            if (total > max) {
                max = total;
                start = i - adv + 1;
            }
        }

        return toTime((int) start);
    }

    int toSec(String t) {
        String[] s = t.split(":");
        return Integer.parseInt(s[0]) * 3600 + Integer.parseInt(s[1]) * 60 + Integer.parseInt(s[2]);
    }

    String toTime(int sec) {
        int h = sec / 3600, m = (sec % 3600) / 60, s = sec % 60;
        return String.format("%02d:%02d:%02d", h, m, s);
    }
}