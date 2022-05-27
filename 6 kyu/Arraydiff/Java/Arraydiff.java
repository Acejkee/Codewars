import java.util.Arrays;
public class Kata {

    public static int[] arrayDiff(int[] a, int[] b) {
        for(int i = 0; i < b.length;i++) {
            int count = 0;
            for (int j = 0 ; j < a.length;j++) {
                if (a[j] == b[i]) {
                    count++;
                }
                else {
                    a[j-count] = a[j];
                }
            }
            a = Arrays.copyOf(a, a.length - count);
        }
        return a;
    }
}