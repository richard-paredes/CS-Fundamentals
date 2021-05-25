import java.util.*;
import java.util.function..Consumer;

class BadMailer {
    private void print(String msg) { System.out.println(msg); }
    public void from (String addr) { print("from"); }
    public void to(String addr) { print("to"); }
    public void subject(String line) { print("subject"); }
    public void message(String body) { print("message"); }
    public void send() { print("Sending..."); }
}

class CascadeMailer {
    private static void print(String msg) { System.out.println(msg); }
    public CascadeMailer from (String addr) { print("from"); return this; }
    public CascadeMailer to(String addr) { print("to"); return this; }
    public CascadeMailer subject(String line) { print("subject"); return this; }
    public CascadeMailer message(String body) { print("message"); return this; }
    public static void send(Consumer<CascadeMailer> block) { 
        CascadeMailer mailer = new CascadeMailer();
        block.accept(mailer);
        print("Sending..."); 
    } 
} 
 
// very no y BadMailer
public class BadExample {
    public static void main(String[] args ){ 
            
        BadMailer mailer = new Mailer();   
            
        mailer.from("builder@agiledevelop er.co m"); 
            
        mailer.to("venkat@agiledeveloper. com"); 
            
        mailer.subject("Your code sucks!" ); 
            
        mailer.message("...how...");  
            
        mailer.send();   
            
   
            
        // do we reuse the mailer now or discard it??
    }
}

public class GoodExample {
    public static void main(String[] args){
        // Still don't know whether to reuse or not
        // new CascadeMailer()
     

        // .subject("Your code sucks!")
    // .message("...how...");
    // 
    // d();

    CascadeMailer.send(mailer->
        mailer.from("builder@agiledeveloper.com")
        .to("venkat@agiledeveloper.com")
        .subject("Your code sucks!")
        .message("...how...")
    );

    
}}



 