package basic_calculator;

public class most_basic_calculator {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Welcome to the most basic calculator!");
        System.out.println("What operation woould you like to do?");
        System.out.println("1. Addition");
        System.out.println("2. Subtraction");
        System.out.println("3. Multiplication");
        System.out.println("4. Division");

        int num = sc.nextInt();

        sc.close();
    }

    public static int addition(int a, int b) {
        return a + b;
    }
    public static int subtraction(int a, int b) {
        return a - b;
    }
    public static int multiplication(int a, int b) {
        return a * b;
    }
    public static int division(int a, int b) {
        return a / b;
    }
}
