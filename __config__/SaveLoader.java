import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class SaveLoader {
    File file;
    public SaveLoader(String filepath){
        file = new File(filepath);
        if (!file.exists()){
            System.out.println(filepath+" does not exist. Creating file.");
            try {
            if (file.createNewFile()) {
                System.out.println("File created at "+filepath);
            }
            } catch (IOException e){
                System.out.println("An error occurred: ");
                e.printStackTrace();
            }
        }
    }

    public void saveDataAppend(String data) {
        String existingData = "";
        try {
            Scanner readScanner = new Scanner(this.file);
            while (readScanner.hasNextLine()) {
                existingData += readScanner.nextLine()+"\n";
            }
            readScanner.close();
        } catch (FileNotFoundException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
        try {
            FileWriter fileWriter = new FileWriter(this.file.getAbsolutePath());
            fileWriter.write(existingData+data+"\n");
            fileWriter.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void clearData() {
        this.file.delete();
        try {
            this.file.createNewFile();
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
        System.out.println(this.file.getName()+" has been reset.");
    }


    //todo: fix this method
    public String[] read() {
        try {
            Scanner readScanner = new Scanner(this.file);
            String output = "";
            String[] file;
            while (readScanner.hasNextLine()) {
                readScanner.nextLine();
            }
            readScanner.close();
            return output;
        } catch (FileNotFoundException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
            String[] badOutput = {"Encountered an error."};
        }
    }
