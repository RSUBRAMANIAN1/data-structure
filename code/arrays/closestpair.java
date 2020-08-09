package code.arrays;

import java.util.Arrays;

public class closestpair { public static void main(final String[] args) {
    // NOTE: You can use the following input values to test this function.
    final int[] a1 = { -1, 3, 8, 2, 9, 5 };
    final int[] a2 = { 4, 1, 2, 10, 5, 20 };
    final int aTarget = 24;
    // closestSumPair(a1, a2, aTarget) should return {5, 20} or {3, 20}

    final int[] b1 = { 7, 4, 1, 10 };
    final int[] b2 = { 4, 5, 8, 7 };
    final int bTarget = 13;
    // closestSumPair(b1, b2, bTarget) should return {4, 8}, {7, 7}, {7, 5}, or {10,
    // 4}

    final int[] c1 = { 6, 8, -1, -8, -3 };
    final int[] c2 = { 4, -6, 2, 9, -3 };
    final int cTarget = 3;
    // closestSumPair(c1, c2, cTarget) should return {-1, 4} or {6, -3}

    final int[] d1 = { 19, 14, 6, 11, -16, 14, -16, -9, 16, 13 };
    final int[] d2 = { 13, 9, -15, -2, -18, 16, 17, 2, -11, -7 };
    final int dTarget = -15;
    //
    final int[] pair = closestSumPair(d1, d2, dTarget);
    for (int i = 0; i < pair.length; i++) {
        System.out.println(pair[i]);
    }

}

// a1 and a2 are the given arrays, and target is the target sum.
// It should return an array of two numbers as the result,
// one from each array.
public static int[] closestSumPair(final int[] a1, final int[] a2, final int target) {
    final int[] a1Sorted = Arrays.copyOf(a1, a1.length);
    Arrays.sort(a1Sorted);
    final int[] a2Sorted = Arrays.copyOf(a2, a2.length);
    Arrays.sort(a2Sorted);

    int i = 0;
    int j = a2Sorted.length - 1;
    int smallestDiff = Math.abs(a1Sorted[0] + a2Sorted[0] - target);
    final int[] closestPair = { a1Sorted[0], a2Sorted[0] };

    while (i < a1Sorted.length && j >= 0) {
        final int v1 = a1Sorted[i];
        final int v2 = a2Sorted[j];
        final int currentDiff = v1 + v2 - target;
        if (Math.abs(currentDiff) < smallestDiff) {
            smallestDiff = Math.abs(currentDiff);
            closestPair[0] = v1; closestPair[1] = v2;
        }

        if (currentDiff == 0) {
            return closestPair;
        }
        else if (currentDiff < 0) {
            i += 1;
        }
        else {
            j -= 1;
        }
    }

    return closestPair;
}
    
}