interface Plugin {
  // serves as a contract
  public void draw();
  public void save();

}

class TextEditorPlugin implements Plugin {
  // public void draw() {
  //   System.out.println("Drawing text");
  // }
  //
  // public void save() {
  //   System.out.println("Saved text");
  // }
}

// class PDFViewerPlugin implements Plugin {
//   public void draw() {
//     System.out.println("Showing PDF");
//   }
//
//   public void save() {
//     System.out.println("Saved PDF annotations");
//   }
// }


public class Runner09 {
  public static void main(String args[]) {
    // assume this is your atom editor

    Plugin p = new TextEditorPlugin();  // reference variable of interface can hold implementing class object
    // Plugin p = new PDFViewerPlugin();

    p.draw();
    p.save();

  }
}
