package java_Programme;

import java.util.Scanner;
public class Weihnachtsbaum {

    public static void main(String[] args) {
        int spalten;
        boolean bestaetigen;
        Scanner scanner = new Scanner(System.in);
        System.out.print("Anzahl der gewünschten Spalten: ");
        spalten=scanner.nextInt();
        System.out.printf("Sie haben sich %d Spalten gewünscht, ist das richtig? ", spalten);
        bestaetigen = scanner.nextBoolean();

        if (bestaetigen) {
            System.out.print("ja");
        }

        scanner.close();
    }
    
}
