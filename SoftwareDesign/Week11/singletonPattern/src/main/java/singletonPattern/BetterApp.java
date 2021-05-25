enum DBManager {
    INSTANCE;

    public void operation1() {

    }

    public void operation2() {

    }
}

// cannot extend an enum, so cant use enum if we want to extend
// enum SpecializedDBManager implements DBManager {

// }

public class BetterApp {
    public static void main(String[] args) {
        DBManager dbManager = DBManager.INSTANCE;
        System.out.println(dbManager);
        DBManager dbManager2 = DBManager.valueOf("INSTANCE");
        System.out.println(dbManager2);
        // DBManager dbManagerFail = DBManager.valueOf("INSTANCE1");

        dbManager.operation1();
        dbManager.operation2();
    }    
}
