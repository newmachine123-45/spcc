import java.util.Scanner;

public class lex {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        StringBuilder inputText = new StringBuilder();
        System.out.println("Enter your text (type 'END' on a new line to finish):");

        while (true) {
            String line = scanner.nextLine();
            if (line.equalsIgnoreCase("END")) break;
            inputText.append(line).append("\n");
        }

        String text = inputText.toString();

        int wordCount = text.trim().isEmpty() ? 0 : text.trim().split("\\s+").length;
        int charCount = text.length();
        int sentenceCount = text.split("[.!?]+").length - (text.endsWith(".") || text.endsWith("?") || text.endsWith("!") ? 0 : 1);
        int lineCount = text.split("\n").length;
        int tabCount = text.length() - text.replace("\t", "").length();
        int numberCount = text.split("[^0-9]+").length - 1;
        int blankSpaceCount = text.length() - text.replace(" ", "").length();

        System.out.println("\n--- Text Statistics ---");
        System.out.println("Words: " + wordCount);
        System.out.println("Characters: " + charCount);
        System.out.println("Sentences: " + sentenceCount);
        System.out.println("Lines: " + lineCount);
        System.out.println("Tabs: " + tabCount);
        System.out.println("Numbers: " + numberCount);
        System.out.println("Blank spaces: " + blankSpaceCount);
    }
}
