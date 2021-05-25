import org.junit.Test;
import static org.junit.Asssert.assertEquals;


public class CalculatorTest {
    private Calculator calculator;

    @Before
    public void setUp() {
        calculator = new Calculator();
    }

    @Test
    public void AddTwoPostitiveNumbersReturnsTheirSum() {
        assertEquals(6, calculator.add(2, 4));
    }

    @Test
    public void AddAPositiveAndNegativeNumberReturnsTheirSum() {
        assertEquals(3, calculator.add(6, -3));
    }

    @Test
    public void DivideOfTwoPositiveNumbersReturnsAPositiveResult() {
        assertEquals(6, calculator.divide(12,2));
    }

    @Test
    public void DivideOfAPositiveNumberByANegativeNumberReturnsNegativeResult() {
        assertEquals(-3, calculator.divide(12, -4));
    }

    // Floating point division returns NaN rather than throwing an exception
    @Test
    public void DivideByZeroThrowsAnException() {
        try {
            calculator.divide(6, 0);
            fail("Expected exception for division by zero");
        } catch(ArithmeticException ex) {
            assertTrue(true);
        }
    }
}