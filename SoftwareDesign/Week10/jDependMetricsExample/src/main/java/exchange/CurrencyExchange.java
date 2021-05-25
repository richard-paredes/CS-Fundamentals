package exchange;

import service.RateService;

public class CurrencyExchange {
  private RateService service;
  
  public CurrencyExchange(RateService theService) { service = theService; }
    
  public double getRate(String currency) {
    //...do real work here...
    return service.getData(currency);
  }
}