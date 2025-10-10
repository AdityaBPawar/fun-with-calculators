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

    String[] buttonValues = {
            "AC", "+/-", "%", "÷",
            "7", "8", "9", "×",
            "4", "5", "6", "-",
            "1", "2", "3", "+",
            "0", ".", "√", "="
    };
    String[] rightSymbols = {"÷", "×", "-", "+", "="};
    String[] topSymbols = {"AC", "+/-", "%"};

    JFrame frame =  new JFrame("Calculator");
    JLabel displaylabel = new JLabel();
    JPanel displaypanel = new JPanel();
    JPanel buttonpanel = new JPanel();

    calculator(){
      frame.setVisible(true);
      frame.setSize(windowwidth, windowheight);
      frame.setLocationRelativeTo(null);
      frame.setResizable(false);
      frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      frame.setLayout(new BorderLayout());

      displaylabel.setBackground(turquoise);
      displaylabel.setForeground(yellow);
      displaylabel.setFont(new Font("Arial", Font.PLAIN, 80));
      displaylabel.setHorizontalAlignment(JLabel.RIGHT);
      displaylabel.setText("0");
      displaylabel.setOpaque(true);

      displaypanel.setLayout(new BorderLayout());
      displaypanel.add(displaylabel);
      frame.add(displaypanel, BorderLayout.NORTH);

      buttonpanel.setLayout(new GridLayout(5,4));
      buttonpanel.setBackground(pink);
      frame.add(buttonpanel);

      for (int i = 0; i < buttonValues.length; i++) {
          JButton button = new JButton();
          String buttonValue = buttonValues[i];
          button.setFont(new Font("Arial", Font.PLAIN, 30));
          button.setText(buttonValue);
          buttonpanel.add(button);
      }
    }
}
