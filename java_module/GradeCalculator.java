import java.util.Scanner;

public class GradeCalculator {

    public static String calculateGrade(int marks) {
        if (marks >= 75) return "A";
        else if (marks >= 60) return "B";
        else if (marks >= 45) return "C";
        else if (marks >= 33) return "D";
        else return "F";
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter marks: ");
        int marks = sc.nextInt();

        String grade = calculateGrade(marks);
        System.out.println("Grade: " + grade);
    }
}