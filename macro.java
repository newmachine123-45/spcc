import java.util.ArrayList;
import java.util.List;

public class macro {
    public static void main(String[] args) {
        String inputSourceCode = "MOV R\n" +
                                 "JOHN\n" +
                                 "DCR R\n" +
                                 "AND R\n" +
                                 "JOHN\n" +
                                 "MUL 88\n" +
                                 "HALT";

        String macroDefinition = "MACRO\n" +
                                 "JOHN\n" +
                                 "ADD 30\n" +
                                 "SUB 25\n" +
                                 "OR R\n" +
                                 "MEND";

        System.out.println("Input source code:");
        System.out.println(inputSourceCode);

        String[] inputLines = inputSourceCode.split("\n");
        String[] macroLines = macroDefinition.split("\n");

        String macroName = macroLines[1];
        List<String> outputCode = new ArrayList<>();
        int macroCalls = 0;
        int macroInstructions = 0;

        // Count number of instructions in macro
        for (int i = 2; i < macroLines.length - 1; i++) {
            macroInstructions++;
        }

        // Expand macro calls
        for (String line : inputLines) {
            if (line.equals(macroName)) {
                macroCalls++;
                for (int i = 2; i < macroLines.length - 1; i++) {
                    outputCode.add(macroLines[i]);
                }
            } else {
                outputCode.add(line);
            }
        }

        int totalInstructions = outputCode.size();

        System.out.println("\nOutput source code after Macro expansion:");
        for (String line : outputCode) {
            System.out.println(line);
        }

        System.out.println("\nStatistical output:");
        System.out.println("Number of instructions in input source code (excluding Macro calls) = " +
                           (inputLines.length - macroCalls));
        System.out.println("Number of Macro calls = " + macroCalls);
        System.out.println("Number of instructions defined in the Macro call = " + macroInstructions);
        System.out.println("Total number of instructions in the expanded source code = " +
                           totalInstructions);
    }
}
