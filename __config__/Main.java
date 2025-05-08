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
                if (input.startsWith("configVars rendererToggle")) {
                    if (saveLoader.read()[0] == "render: True") {
                        saveLoader.saveDataReplace("render: False", 0);
                    } else {
                        saveLoader.saveDataReplace("render: True", 0);
                    }
                    System.out.println("The renderer has been toggled.");
                }
            }/* else if () {
            } else {
            }*/
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