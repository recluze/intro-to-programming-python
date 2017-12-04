
public class Student03 {
  static int num = 0;
  int rollNo;

  public static void main(String args[]) {

    Student03 s1 = new Student03();
    Student03 s2 = new Student03();

    System.out.println("num: " + Student03.num);

    Student03.num += 1;
    System.out.println("num: " + Student03.num);

    System.out.println("s1.num: " + s1.num);
    System.out.println("s2.num: " + s2.num);

    System.out.printlnt("rollNo:" + s1.rollNo);


  }
}
