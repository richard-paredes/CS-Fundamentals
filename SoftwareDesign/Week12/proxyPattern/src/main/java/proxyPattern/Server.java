package proxyPattern;

import java.rmi.Remote; //interface for Remote proxy
import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.rmi.server.UnicastRemoteObject;

interface Greeter extends Remote {
    String greet(String name) throws RemoteException;
}

public class Server implements Greeter
{
    @Override
    public String greet(String name) throws RemoteException {
        System.out.println("Greetings...");
        return "Hello " + name;
    }
    public static void main( String[] args ) throws RemoteException
    {
        Server server = new Server();
        System.setProperty("java.rmi.server.hostname", "127.0.0.1");
        
        Remote remote = UnicastRemoteObject.exportObject(server, 8002);

        Registry registry = LocateRegistry.createRegistry(8002);

        registry.bind("Server", remote);

        System.out.println("Server running...");
    }
}
