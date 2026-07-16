// Last updated: 7/16/2026, 4:04:14 PM
 class Solution{
        public int secondsBetweenTimes(String startTime, String endTime){
            String[] start = startTime.split(":");
            String[] end = endTime.split(":");
            int sh = Integer.parseInt(start[0]);
            int sm = Integer.parseInt(start[1]);
            int ss = Integer.parseInt(start[2]);

            int eh = Integer.parseInt(end[0]);
            int em = Integer.parseInt(end[1]);
            int es = Integer.parseInt(end[2]);

            int startTotalSeconds = (sh * 3600) + (sm * 60) + ss;
            int endTotalSeconds = (eh * 3600) + (em * 60) + es;

            
            return Math.abs(endTotalSeconds - startTotalSeconds);
            
        }
    }