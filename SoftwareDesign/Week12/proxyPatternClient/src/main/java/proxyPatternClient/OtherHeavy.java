package proxyPatternClient;

public class OtherHeavy {
    public static void main(String[] args) {
        HeavyImpl spy = spy(new HeavyImpl());

        System.out.println(spy.someMethod());// still returns real implementation

        System.out.println(new HeavyImpl().getClass()); // returns real implementation class

        System.out.println(spy.getClass()); // its a spy proxy from Moqito
    }
}
