import java.util.Scanner;

public class InchesToCentimeters {
    public static void main(String[] args) {
        double inch, cm;
        Scanner scanner = new Scanner(System.in);
    
        inch = Double.parseDouble(scanner.nextLine());
        cm = inch * 2.54;

        System.out.println(cm);
    }
}
