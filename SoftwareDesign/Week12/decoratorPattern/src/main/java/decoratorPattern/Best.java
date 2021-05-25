package decoratorPattern;

import java.util.function.Function;

class Candidate {
    final String _firstName;
    final String _lastName;
    final boolean _qualified;
    final String _evaluations;

    public Candidate(String firstName, String lastName, boolean qualified, String evaluations) {
        _firstName = firstName;
        _lastName = lastName;
        _qualified = qualified;
        _evaluations = evaluations;
    }

    public String getFirstName() { return _firstName; }
    public String getLastName() { return _lastName; }
    public boolean isQualified() { return _qualified; }
    public String getEvaluations() { return _evaluations; }

    @Override
    public String toString() {
        return String.format("%s %s Qualified: %b based on evaluations %s", _firstName, _lastName, _qualified, _evaluations);
    }
}

interface ResidenceEvaluator {

    public static Candidate evaluate(Candidate candidate) {
        boolean passed = true;
        if (Math.random() > 0.5) {
            passed = false;
        }

        return new Candidate(candidate.getFirstName(), candidate.getLastName(), candidate.isQualified() && passed, candidate.getEvaluations() + "\nResidenceEvaluator: " + passed);
    }
}

interface ExperienceEvaluator {
    
    public static Candidate evaluate(Candidate candidate) {
        boolean passed = true;
        if (Math.random() > 0.5) {
            passed = false;
        }

        return new Candidate(evaluatedCandidate.getFirstName(), evaluatedCandidate.getLastName(), evaluatedCandidate.isQualified() && passed, evaluatedCandidate.getEvaluations() + "\nExperienceEvaluator: " + passed);
    }
}

interface CrimeEvaluator {

    public static Candidate evaluate(Candidate candidate) {
        boolean passed = true;
        if (Math.random() > 0.5) {
            passed = false;
        }

        return new Candidate(evaluatedCandidate.getFirstName(), evaluatedCandidate.getLastName(), evaluatedCandidate.isQualified() && passed, evaluatedCandidate.getEvaluations() + "\nCrimeEvaluator: " + passed);
    }
}

interface CommunityEvaluator {

    public static Candidate evaluate(Candidate candidate) {
        boolean passed = true;
        if (Math.random() > 0.5) {
            passed = false;
        }

        return new Candidate(evaluatedCandidate.getFirstName(), evaluatedCandidate.getLastName(), evaluatedCandidate.isQualified() && passed, evaluatedCandidate.getEvaluations() + "\nCommunityEvaluator: " + passed);
    }
}


public class App 
{
    public static void applyAndPrint(Function<Integer, Integer> fun) {
        System.out.prinln(fun.apply(3));
    }

    public static void lambdasInJava() {
        Function<Integer, Integer> inc = value -> value + 1;
        Function<Integer, Integer> doubleIt = value -> value * 2;
        System.out.println(inc.apply(3)); // returns 4;
        System.out.println(doubleIt.apply(4)); // returns 8;

        int temp = inc.apply(3);
        System.out.println(doubleIt.apply(temp)); // returns 8; 

        System.out.println(doubleIt.apply(inc.apply(3))); // returns 8

        
        applyAndPrint(inc);
        applyAndPrint(doubleIt);
        applyAndPrint(inc.andThen(doubleIt)); // chains the lambdas
    }

    private static void evaluateCandidate(Candidate candidate, Function<Candidate, Candidate> evaluator) {
        System.out.println("Evaluating: " + candidate.getFirstName() + " " candidate.getLastName());
        System.out.println(evaluator.apply(candidate)));
    }

    private static Function<Candidate, Candidate> decorateEvaluators(Function<Candidate, Candidate>... evaluators) {
        return Stream.of(evaluators)
                .reduce(Function::andThen)
                .orElse(Function.identity()); // if no evaluators given, then just provide a passthrough
    }

    public static void main( String[] args )
    {
        Candidate candidate = new Candidate("John", "Doe", true, "");

        evaluateCandidate(candidate, decorateEvaluators(ResidenceEvaluator::evaluate,
                                                        ExperienceEvaluator::evaluate,
                                                        CrimeEvaluator::evaluate,
                                                        CommunityEvaluator::evaluate));
    }
}
