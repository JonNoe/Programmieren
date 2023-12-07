package java_Programme;
import java.util.Scanner;

public class chatgpt {
     // Method to draw the Christmas tree
    private static void drawChristmasTree(int height) {
        for (int i = 0; i < height; i++) {
            // Print spaces before the '*' to center the tree
            for (int j = 0; j < height - i - 1; j++) {
                System.out.print(" ");
            }

            // Print '*' for the current level
            for (int j = 0; j < 2 * i + 1; j++) {
                System.out.print("*");
            }

            // Move to the next line for the next level
            System.out.println();
        }

        // Print the tree trunk
        for (int i = 0; i < height / 3; i++) {
            for (int j = 0; j < height - 1; j++) {
                System.out.print(" ");
            }
            System.out.println("|");
        }
        
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Get the height of the Christmas tree from the user
        System.out.print("Enter the height of the Christmas tree: ");
        int height = scanner.nextInt();

        // Draw the Christmas tree
        drawChristmasTree(height);
    }     
}
