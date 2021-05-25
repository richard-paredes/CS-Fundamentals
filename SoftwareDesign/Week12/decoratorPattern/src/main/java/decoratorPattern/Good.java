package decoratorPattern;


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

interface Evaluator {
    public boolean evaluate(Candidate candidate);
}

abstract class EvaluatorDecorator implements Evaluator {
    private final Evaluator _next;
    public EvaluatorDecorator(Evaluator next) {
        _next = next;
    }

    protected abstract Candidate evaluateCandidate(Candidate candidate);

    @Override
    public final boolean evaluate(Candidate candidate) {
        Candidate evaluatedCandidate = candidate;
        if (_next != null) {
            evaluatedCandidate = _next.evaluate(candidate);
        }
        return evaluateCandidate(evaluatedCandidate);
    }
}
class ResidenceEvaluator implements Evaluator {
    public boolean evaluate(Candidate candidate) {
        boolean passed = true;
        if (Math.random() > 0.5) {
            passed = false;
        }

        return new Candidate(candidate.getFirstName(), candidate.getLastName(), candidate.isQualified() && passed, candidate.getEvaluations() + "\nResidenceEvaluator: " + passed);
    }
}

class ExperienceEvaluator extends EvaluatorDecorator {
    
    public ExperienceEvaluator(Evaluator next) {
        super(next);
    }

    @Override
    public Candidate evaluateCandidate(Candidate candidate) {
        boolean passed = true;
        if (Math.random() > 0.5) {
            passed = false;
        }

        return new Candidate(evaluatedCandidate.getFirstName(), evaluatedCandidate.getLastName(), evaluatedCandidate.isQualified() && passed, evaluatedCandidate.getEvaluations() + "\nExperienceEvaluator: " + passed);
    }
}

class CrimeEvaluator extends EvaluatorDecorator {
    public CrimeEvaluator(Evaluator next) {
        super(next);
    }

    @Override
    public Candidate evaluateCandidate(Candidate candidate) {
        boolean passed = true;
        if (Math.random() > 0.5) {
            passed = false;
        }

        return new Candidate(evaluatedCandidate.getFirstName(), evaluatedCandidate.getLastName(), evaluatedCandidate.isQualified() && passed, evaluatedCandidate.getEvaluations() + "\nCrimeEvaluator: " + passed);
    }
}

class CommunityEvaluator extends EvaluatorDecorator {
    public CommunityEvaluator(Evaluator next) {
        super(next);
    }

    @Override
    public Candidate evaluateCandidate(Candidate candidate) {
        boolean passed = true;
        if (Math.random() > 0.5) {
            passed = false;
        }

        return new Candidate(evaluatedCandidate.getFirstName(), evaluatedCandidate.getLastName(), evaluatedCandidate.isQualified() && passed, evaluatedCandidate.getEvaluations() + "\nCommunityEvaluator: " + passed);
    }
}


public class App 
{
    private static void evaluateCandidate(Candidate candidate, Evaluator evaluator) {
        System.out.println("Evaluating: " + candidate.getFirstName() + " " candidate.getLastName());
        System.out.println(evaluator.evaluate(candidate));

        System.out.println(evaluator.getClass()); // returns the parent node . . poor object identity from decorator!
    }

    public static void main( String[] args )
    {
        Candidate candidate = new Candidate("John", "Doe", true, "");

        evaluateCandidate(candidate, new ResidenceEvaluator());
        evaluateCandidate(candidate, new ExperienceEvaluator(ResidenceEvaluator));

        // smelly code...
        // Residence is the leaf
        // First evaluate experience, then criminal, then residence
        evaluateCandidate(candidate, new CrimeEvaluator(new ExperienceEvaluator(new ResidenceEvaluator())));

        // the capability of Evaluator keeps changing, but its type remains the same!
        evaluateCandidate(candidate, new CommunityEvaluator(new ExperienceEvaluator(new ResidenceEvaluator())));
    }
}
