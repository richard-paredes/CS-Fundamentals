package builderPattern;

class Crust {}
class Sauce {}
class Pizza {
    private Crust _crust;
    private Sauce _sauce;
    private String _cheese;
    private String _toppings;
    public void createCrust() {
        _crust = new Crust();
    }
    public void spreadSauce() {
        _sauce = new Sauce();
    }
    public void addCheese() {
        _cheese =  "Mozzarella";
    }
    public void addToppings(String... toppings) {
        _toppings = toppings;
    }
    public void bake() {
        System.out.println("Baking.");
    }
    @Override
    public String toString() {
        String toppings = Stream.of(_toppings).collect(joining(","));
        return _crust + ":" + _sauce + ":" + _cheese + ":" + toppings; 
    }
}
abstract class PizzaBuilder {
    private Pizza _pizza = new Pizza();
    public abstract void createCrust();
    public abstract void spreadSauce();
    public abstract void addCheese();
    public abstract void addToppings();
    public abstract void bake();
    protected Pizza getPizza() {
        return _pizza;
    }
    public Pizza create() {
        return _pizza;
    }
}

// preserves the steps in order
class PizzaMaker {
    public void makePizza(PizzaBuilder pizzaBuilder) {
        pizzaBuilder.createCrust();
        pizzaBuilder.spreadSauce();
        pizzaBuilder.addCheese();
        pizzaBuilder.addToppings();
        pizzaBuilder.bake();
    }
}

class CheesePizzaBuilder extends PizzaBuilder {
    @Override
    public void createCrust() {
        getPizza().createCrust();
    }
    @Override
    public void spreadSauce() {
        getPizza().spreadSauce();
    }
    @Override
    public void addCheese() {
        getPizza().addCheese();
    }
    @Override
    public void addToppings() {
        getPizza().addToppings("...Cheese...");
    }
    @Override
    public void bake() {
        getPizza().bake();
    }
}

class VeggiePizzaBuilder extends PizzaBuilder {
    @Override
    public void createCrust() {
        getPizza().createCrust();
    }
    @Override
    public void spreadSauce() {
        getPizza().spreadSauce();
    }
    @Override
    public void addCheese() {
        getPizza().addCheese();
    }
    @Override
    public void addToppings() {
        getPizza().addToppings("Black olives", "Green olives", "Jalapenos");
    }
    @Override
    public void bake() {
        getPizza().bake();
    }
}

// kinda violates DRY principle by re-implementing the same crusts and stuff since they don't differ
class HawaiianPizzaBuilder extends PizzaBuilder {
    @Override
    public void createCrust() {
        getPizza().createCrust();
    }
    @Override
    public void spreadSauce() {
        getPizza().spreadSauce();
    }
    @Override
    public void addCheese() {
        getPizza().addCheese();
    }
    @Override
    public void addToppings() {
        getPizza().addToppings("Ham", "Pineapple");
    }
    @Override
    public void bake() {
        getPizza().bake();
    }
}

public class App 
{
    public static void main( String[] args )
    {
        PizzaMaker pizzaMaker = new PizzaMaker();
        PizzaBuilder cheesePizzaBuilder = new CheesePizzaBuilder();
        pizzaMaker.makePizza(cheesePizzaBuilder)
        System.out.println(cheesePizzaBuilder.create());

        VeggiePizzaBuilder veggiePizzaBuilder = new VeggiePizzaBuilder();
        pizzaMaker.makePizza(veggiePizzaBuilder);
        System.out.println(veggiePizzaBuilder.create());

        HawaiianPizzaBuilder hawaiianPizzaBuilder = new HawaiianPizzaBuilder();
        pizzaMaker.makePizza(hawaiianPizzaBuilder);
        System.out.println(hawaiianPizzaBuilder.create());
    }
}
