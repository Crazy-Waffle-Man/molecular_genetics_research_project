import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
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

    public void saveDataReplace(String data, int lineNumber) {
        //replace the data at a line with the data arg
        String[] existingData = this.read();
        this.clearData();
        try {
            for (int i = 0; i < existingData.length; i++) {
                if (i == lineNumber) {
                    this.saveDataAppend(data);
                } else {
                    this.saveDataAppend(existingData[i]);
                }
            }
        } catch (ArrayIndexOutOfBoundsException e) {
            e.printStackTrace();
            System.out.println("Error: Array index out of bounds.");
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
            ArrayList<String> outputDynamicArray = new ArrayList<>();
            while (readScanner.hasNextLine()) {
                outputDynamicArray.add(readScanner.nextLine());
            }
            readScanner.close();
            String[] output = outputDynamicArray.toArray(new String[0]);
            return output;

        } catch (FileNotFoundException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
            String[] badOutput = {"Encountered an error."};
            return badOutput;
        }
    }
}