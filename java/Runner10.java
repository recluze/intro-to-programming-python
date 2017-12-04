/*
Download slf4j binary from: https://www.slf4j.org/download.html

Extract to get jar files:
 - slf4j-api-1.7.25.jar      (or whichever version they have)
 - slf4j-simple-1.7.25.jar

Copy them to your working_directory/lib/ folder

Compile: javac -cp .:lib/slf4j-api-1.7.25.jar:lib/slf4j-simple-1.7.25.jar Runner10.java   (replace colon with semicolon on Windows)

Execute: java -cp .:lib/slf4j-api-1.7.25.jar:lib/slf4j-simple-1.7.25.jar Runner10

*/

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;




public class Runner10 {


  public static void main(String args[]) {
    Logger logger = LoggerFactory.getLogger(Runner10.class);

    logger.info("A message with the info level");
    logger.warn("Warning level message ...");
  }
}
