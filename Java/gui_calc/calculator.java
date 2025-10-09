package gui_calc;
import java.util.Arrays;
import java.util.Scanner;
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import javax.swing.border.LineBorder;

public class calculator {
    int windowwidth = 360;
    int windowheight = 540;

    Color lilac = new Color(153, 85, 187);
    Color pink = new Color(255, 105, 179);
    Color yellow = new Color(255, 255, 153);
    Color turquoise = new Color(43, 217, 198);

    JFrame frame =  new JFrame("Calculator");

    calculator(){
      frame.setVisible(true);
      frame.setSize(windowwidth, windowheight);
      frame.setLocationRelativeTo(null);
      frame.setResizable(false);
      frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      frame.setLayout(new BorderLayout());
    }
}
