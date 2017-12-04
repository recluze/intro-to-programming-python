class Polygon {
  int numSides;

  public Polygon(int numSides) {
    this.numSides = numSides;
  }

  public double getArea() {
    return 2.0; // no idea how to calculate this!
  }
}

// 01 -- add a class
// class Rectangle extends Polygon {
//   // 02 add a constructor
//   // public Rectangle() {
//   //   super(4);
//   // }
//
//   // double length;
//   // double width;
//   // public void setSides(double length, double width) {
//   //   this.length = length;
//   //   this.width = width;
//   // }
//   //
//   // // 03 overriding
//   // // 04 @Override // and change fn name to get error
//   // public double getArea() {
//   //   return this.length * this.width;
//   // }
// }


public class Runner07 {
  public static void main(String args[]) {
    Polygon p = new Polygon();        // error because no default constructor
    System.out.println("Area of poly: " + p.getArea());  // this does not make sense

    // Rectangle r = new Rectangle();    // also an error due to no default constructor
    //
    // r.setSides(4, 4);
    // System.out.println("Area of rect: " + r.getArea());  // this does not make sense

  }
}
