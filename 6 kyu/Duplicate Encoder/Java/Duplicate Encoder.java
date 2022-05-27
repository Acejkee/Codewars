public class DuplicateEncoder {
    static String encode(String word) {
        word = word.toLowerCase();
        String result = "";
        for (int i = 0; i < word.length(); i++) {
            int count = 0;
            for (int j = 0; j < word.length(); j++) {
                if (word.charAt(i) == word.charAt(j)) {
                    count++;
                }
            }
            if (count > 1) {
                result += ")";
            }
            else {
                result += "(";
            }
        }
        return result;
    }
}