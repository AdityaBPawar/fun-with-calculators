package basic_calculator;
import java.util.Scanner;
public class most_basic_calculator {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Welcome to the most basic calculator!");
        System.out.println("What operation would you like to do?");
        System.out.println("1. Addition");
        System.out.println("2. Subtraction");
        System.out.println("3. Multiplication");
        System.out.println("4. Division");

        int num = sc.nextInt();

        System.out.println("Enter the first number: ");
        int a = sc.nextInt();
        System.out.println("Enter the second number: ");
        int b = sc.nextInt();

        double result = 0;

        if (num == 1){
            result = addition(a,b);
            }
        else if (num == 2){
            result = subtraction(a,b);
        }
        else if (num == 3){
            result =multiplication(a,b);
        }
        else if (num == 4){
            result = division(a,b);
        }
        else {
            System.out.println("Invalid input!");
        }
        System.out.println("The result is: " + result);

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
    public static double division(int a, int b) {
        if (b == 0) {
            System.out.println("Error! Division by Zero!");
            return 0;
        }
        return (double) a / b;
    }
}
