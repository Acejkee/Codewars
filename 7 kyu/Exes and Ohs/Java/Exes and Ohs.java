public class XO {
  
  public static boolean getXO (String str) {
    int count_x = 0;
    int count_o = 0;
    str = str.toLowerCase();
    for (int i = 0; i < str.length();i++) {
      if (str.charAt(i) == 'x') {
        count_x++;
      }
      if (str.charAt(i) == 'o') {
        count_o++;
      }
    }
    return count_x == count_o;
  }
}