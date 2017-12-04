
public class Animal05 {
  int legs;

  // String msg = "Test message";  // 03 add this and change msg below

  public int getLegs() {    // 02 make this private
    return this.legs;
  }

  public void printLegCount(String msg) {
    System.out.println(msg + ": " + getLegs());
  }

  // java doesn't have a destructor

  public static void main(String args[]) {
    Animal05 a = new Animal05();

    a.printLegCount("Legs are");

    // 01
    a.legs += 1;
    a.printLegCount("Legs are");
  }
}
