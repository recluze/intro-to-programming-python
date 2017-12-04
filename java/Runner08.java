class Polygon {
  int numSides;

  public Polygon(int numSides) {
    this.numSides = numSides;
  }

  // 01: add abstract, then make class abstract then don't instantiate 
  public double getArea() {
    return 2.0;     // no idea how to calculate this!
  }
}

class Rectangle extends Polygon {

  public Rectangle() {
    super(4);
  }

  double length;
  double width;
  public void setSides(double length, double width) {
    this.length = length;
    this.width = width;
  }

  @Override
  public double getArea() {
    return this.length * this.width;
  }
}


public class Runner08 {
  public static void main(String args[]) {
    Polygon p = new Polygon(3);
    System.out.println("Area of poly: " + p.getArea());  // this does not make sense

    Rectangle r = new Rectangle();
    // Polygon r = new Rectangle();    // 02 -- parent class reference var, child object 

    r.setSides(4, 4);
    System.out.println("Area of rect: " + r.getArea());

  }
}
