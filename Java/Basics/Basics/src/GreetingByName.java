import java.util.Scanner;

public class GreetingByName {
    public static void main(String[] args) {
        String name, greeting;
        Scanner scanner = new Scanner(System.in);

        name = scanner.nextLine();
        greeting = "Hello, " + name + "!";

        System.out.println(greeting);
    }
}
