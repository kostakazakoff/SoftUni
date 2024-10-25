import java.util.Scanner;

public class RectangleArea {
    public static void main(String[] args) {
        int w, h, area;
        Scanner scanner = new Scanner(System.in);

        w = Integer.parseInt(scanner.nextLine());
        h = Integer.parseInt(scanner.nextLine());

        area = w * h;
        System.out.println(area);
    }
}
