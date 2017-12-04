
public class Animal02 {

  int legs = 4;     // class member

  // 01 add a method
  public int getLegs() {
    return this.legs;
  }

  void constructsTest() {
    int x = 5;
    if (x == 5)
      System.out.println("X is 5");

    for(int i = 0; i < 3; i++)
      System.out.println("Looping:" + i);
  }

  public static void main(String args[]) {
    System.out.println("Main function called ... ");
    Animal02 a = new Animal02();    // create an instance
    System.out.println("Legs: " + a.legs);

    // add call to method
    System.out.println("Legs from method: " + a.getLegs());


    a.constructsTest();
  }
}
