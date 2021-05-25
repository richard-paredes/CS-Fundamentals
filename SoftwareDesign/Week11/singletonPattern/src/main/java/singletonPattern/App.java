package singletonPattern;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class DBManager {
    private static DBManager _instance;
    private DBManager() {
        if (_instance != null) {
            throw new RuntimeException("Already exists.")
        }
        System.out.println("Creating."); 
    }
    // synchronized adds thread safety by adding critical section
    public static synchronized DBManager getInstance() {
        // lacks thread safety
        if (_instance == null) {
            System.out.println("Checking again.");
            // a double check
            synchronized (DBManager.class) {
                if (_instance == null)
                    _instance = new DBManager();
            }
        }
        return _instance;
    }
    @Override
    public String toString() {
        return String.format("%s %d", getClass(), hashCode());
    }
}

// use an enum . . . it's thread safe
public enum DBManagerSingleton {

}

public class App 
{
    public static void getDBManager() {
        DBManager dbManager = DBManager.getInstance();
        DBManager dbManager2 = DBManager.getInstance();

        System.out.println(dbManager);
        System.out.println(dbManager2);

    }

    public static void main( String[] args )
    {
        // // DBManager dbManager = new DBManager();
        // DBManager dbManager = DBManager.getInstance();
        // System.out.println(dbManager);

        // DBManager dbManagerCopy = DBManager.getInstance();
        // System.out.println(dbManagerCopy);

        // // DBManager.class.newInstance(); // illegal access

        // Constructor<DBManager> constructor = DBManager.class.getDeclaredConstructor();
        // constructor.setAccessible(true);
        // DBManager dbManager2 = constructor.newInstance();
        // System.out.println(dbManager2);

        ExecutorService executorService = Executors.newFixedThreadPool(10);

        executorService.submit(App::getDBManager);
        executorService.submit(App::getDBManager);

        Thread.sleep(2000);

        executorService.submit(App::getDBManager);
        Thread.sleep(1000);
        executorService.shutdown();
    }
}
