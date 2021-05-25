package proxyPatternClient;

import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;

interface Greeter extends Remote {
    String greet(String name) throws RemoteException;
}

class LocalGreeter implements Greeter {
    @Override
    public String greet(String name) throws RemoteException {
        return "Howdy " + name;
    }
}
public class Client 
{
    public static void useGreeter(Greeter greeter) throws RemoteException {
        System.out.println(greeter.greet("Earthling"));
    }
    public static void main( String[] args ) throws RemoteException
    {
        Registry registry = LocateRegistry.getRegistry(8002);
        
        Greeter remoteGreeter = (Greeter) registry.lookup("Server");
        LocalGreeter localGreeter = new LocalGreeter();
        
        useGreeter(remoteGreeter);
        useGreeter(localGreeter);

        System.out.print(localGreeter.getClass());
        System.out.println(remoteGreeter.getClass()); // prints out a proxy object... 
    }
}
