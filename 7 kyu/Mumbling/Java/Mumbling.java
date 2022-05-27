public class Accumul {

    public static String accum(String s) {
        String result = "";
        for(int i = 0; i < s.length();i++) {
            String word = "";
            for(int j = 0 ; j <= i;j++) {
                word += s.toLowerCase().charAt(i);
                if (j == 0) {
                    word = word.toUpperCase();
                }
                if (j == i && i != s.length() - 1) {
                    word += "-";
                }
            }
            result+= word;
        }
        return result;
    }
}