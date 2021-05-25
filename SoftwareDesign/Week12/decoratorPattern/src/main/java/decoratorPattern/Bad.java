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

class ResidenceEvaluator {
    public boolean evaluate(Candidate candidate) {
        boolean passed = true;
        if (Math.random() > 0.5) {
            passed = false;
        }

        return new Candidate(candidate.getFirstName(), candidate.getLastName(), candidate.isQualified() && passed, candidate.getEvaluations() + "\nResidenceEvaluator: " + passed);
    }
}

class ExperienceEvaluator extends ResidenceEvaluator {
    
    @Override
    public boolean evaluate(Candidate candidate) {
        Candidate evaluatedCandidate = super.evaluate(candidate);

        boolean passed = true;
        if (Math.random() > 0.5) {
            passed = false;
        }

        return new Candidate(evaluatedCandidate.getFirstName(), evaluatedCandidate.getLastName(), evaluatedCandidate.isQualified() && passed, evaluatedCandidate.getEvaluations() + "\nExperienceEvaluator: " + passed);
    }
}

class CrimeEvaluator extends ResidenceEvaluator {
    @Override
    public boolean evaluate(Candidate candidate) {
        Candidate evaluatedCandidate = super.evaluate(candidate);

        boolean passed = true;
        if (Math.random() > 0.5) {
            passed = false;
        }

        return new Candidate(evaluatedCandidate.getFirstName(), evaluatedCandidate.getLastName(), evaluatedCandidate.isQualified() && passed, evaluatedCandidate.getEvaluations() + "\nCrimeEvaluator: " + passed);
    }
}

/**
 * Hello world!
 *
 */
public class App 
{
    private static void evaluateCandidate(Candidate candidate, ResidenceEvaluator evaluator) {
        System.out.println("Evaluating: " + candidate.getFirstName() + " " candidate.getLastName());
        System.out.println(evaluator.evaluate(candidate));
    }

    public static void main( String[] args )
    {
        ResidenceEvaluator residenceEvaluator = new ResidenceEvaluator();
        ExperienceEvaluator experienceEvaluator = new ExperienceEvaluator(); 

        Candidate candidate = new Candidate("John", "Doe", true, "");

        evaluateCandidate(candidate, residenceEvaluator);
        evaluateCandidate(candidate, ExperienceEvaluator);

        evaluateCandidate(candidate, residenceEvaluator);
        evaluateCandidate(candidate, CrimeEvaluator);

        // ISSUE: what if we wanted to add a new evaluation and evaluate based on any combination of them??
        // we COULD multi-inherit (for languages that allow), but that would be a TERRIBLE approach
    }
}
