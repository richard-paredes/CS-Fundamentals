package example1;

import javax.swing.*;
import java.awt.event.*;

/**
 * Hello world!
 */
public final class App extends JFrame {

    private class HandleMouse implements MouseListener {
        @Override
        public void mouseClicked(MouseEvent e) {
            // TODO Auto-generated method stub
            //JOptionPane.showMessageDialog(e.getComponent(), "You clicked");
            throw new RuntimeException("You clicked...");
        }

        @Override
        public void mousePressed(java.awt.event.MouseEvent e) {
            // TODO Auto-generated method stub

        }

        @Override
        public void mouseReleased(java.awt.event.MouseEvent e) {
            // TODO Auto-generated method stub

        }

        @Override
        public void mouseEntered(java.awt.event.MouseEvent e) {
            // TODO Auto-generated method stub

        }

        @Override
        public void mouseExited(java.awt.event.MouseEvent e) {
            // TODO Auto-generated method stub

        }
    }

    private JButton jbutton;

    private App() {
    }

    @Override
    protected void frameInit() {
        // TODO Auto-generated method stub
        super.frameInit();
        jbutton = new JButton("click");
        getContentPane().add(jbutton);

        jbutton.addMouseListener(new HandleMouse());
    }

    /**
     * Says hello to the world.
     * @param args The arguments of the program.
     */
    public static void main(String[] args) {
        System.out.println("Hello World!");
        JFrame frame = new App();
        frame.setSize(100, 100);
        frame.setVisible(true);
    }
}
