import java.util.Scanner;

public class Main {
    private static SaveLoader saveLoader = new SaveLoader("config_vars.config");
    public static void main(String[] vars) {
        setDefaults();
        System.out.println("Welcome to the Java config command line for molecular_genetics_research_project.");
        System.out.println("Type \u001b[38;2;255;0;255mhelp\u001b[0m for help or view the documentation in README.md");
        Scanner scanner = new Scanner(System.in);
        boolean running = true;
        while (running) {
            String input = scanner.nextLine();
            if (input.startsWith("configVars")) {
                if (input.startsWith("render", 11)) {
                    if (input.startsWith("True", 17)) {
                        saveLoader.saveDataReplace("render: True", 0);
                    } else {
                        saveLoader.saveDataReplace("render: False", 0);
                    }
                } else if (input.startsWith("print_output", 11)) {
                    if (input.startsWith("True", 24)) {
                        saveLoader.saveDataReplace("print_output: True", 1);
                    } else {
                        saveLoader.saveDataReplace("print_output: False", 1);
                    }
                }
            } else if (input.startsWith("exit")) {
                running = false;
            } else {
                System.out.println("Malformed input: \""+ input+ "\" is not a recognized command.");
            }
        }
        scanner.close();
    }

    public static void setDefaults() {
        //set default values here
        saveLoader.clearData();
        saveLoader.saveDataAppend("render: True");
        saveLoader.saveDataAppend("print_output: False");
    }
}