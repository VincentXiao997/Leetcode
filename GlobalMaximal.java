import java.util.*;
// import collections


public class GlobalMaximal
{
	public static int solve(List<Integer> a, int m) {
	    Collections.sort(a);
        int n = a.size();
        int left = 1, right = a.get(n-1) - a.get(0);

        while(left + 1 < right) {
            int mid = left + (right - left) / 2;
            boolean valid = check(a, m, mid, n);
            if (valid) {
                left = mid;
            } else {
                right = mid - 1;
            }
        }
        boolean valid = check(a, m, right, n);
        if (valid) {
            return right;
        } else {
            return left;
        }
	}


    // 2 3 5 9
    private static boolean check(List<Integer> a, int m, int mid, int n) {
        int val = a.get(0), idx = 0;
        m--;
        while (m > 0) {
            idx = bs(a, idx+1, val+mid, n);
            if (idx < 0 || (m > 1 && idx >= n - 1)) {
                return false;
            }
            m--;
            val = a.get(idx);
        }    
        return true;
    }

    private static int bs(List<Integer> a, int idx, int val, int n) {

        int left = idx, right = n - 1;
        while (left + 1 < right) {
            int mid = left + (right - left) / 2;
            if (a.get(mid) == val) {
                right = mid;
            } else if (a.get(mid) > val) {
                right = mid;
            } else {
                left = mid;
            }
        }
        if (a.get(left) >= val) {
            return left;
        } else if (a.get(right) >= val) {
            return right;
        } else {
            return -1;
        }
    }
    
	public static void main(String[] args) {
	    List<Integer> a = new ArrayList<Integer>();
        a.add(2);
        a.add(3);
        a.add(1);
        a.add(4);
        a.add(6);
        a.add(5);
        System.out.println(solve(a, 3));
	}
}




// 1-7
// 4
// 4-7
// 1-3

// 2 3 5 9



// 3

// mlogn * log(max-min)