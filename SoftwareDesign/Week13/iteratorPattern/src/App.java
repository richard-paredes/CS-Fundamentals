class Person {
    private String _firstName;
    private String _lastName;
    public Person(String firstName, string lastName) {
        _firstName = firstName;
        _lastName = lastName;
    }

    @Override
    public String toString() {
        return String.format("%s %s", _firstName, _lastName);
    }
}

public class App {
    // iterator completely abstracts out the iteration! 
    public static void iterateAndPrint(Iterator<Person> iterator) {
        while (iterator.hasNext()) {
            System.out.println(iterator.next());
        }
    }

    public static void main(String[] args) throws Exception {
        List<Person> people = Arrays.asList(
            new Person("John", "Smith"),
            new Person("Sarah", "Smith"),
            new Person("Bob", "Walker")
        );

        // external iterator
        for(int i = 0; i < people.size(); i++) {
            System.out.println(people.get(i));
        }

        // using the internal iterator; rarely done this way
        Iterator<Person> iterator = people.iterator();
        while (iterator.hasNext()) { 
            System.out.println(iterator.next());
        }

        // normal usage of iterator; literally syntactic sugar for iterator
        for(Person person : people) {
            System,out.println(person);
        }

        
        Set<Person> peopleSet = new HashSet<>();
        peopleSet.add(new Person("Sara", "Smith"));
        peopleSet.add(new Person("Jill", "Walker"));
        
        // This is a factory method!
        iterateAndPrint(people.iterator());
        iterateAndPrint(peopleSet.iterator());

        // These will be different implementations because the collection is different
        System.out.println(people.iterator());
        System.out.println(peopleSet .iterator());


        for (int i = 0; i < people.size(); i++) {
            System.out.println(people.get(i));
        }
        for (int i = 0; i < peopleSet.size(); i++) {
            System.out.println(peopleSet...);// there's no way to navigate the Set
        }
    }
}
