/**
 * creditcard is a superclass of Bankcard which extend Bankcard. it has variable,methods,constructors and a 
 * display method
 * @22067054 Arbin Rajbanshi
 * @26 jan 2023
 */

public class creditcard extends Bankcard
{
    //seven instance variable is created with suitable data types
   private int CVCnumber;
   private double CreditLimit;
   private double InterestRate;
   private String ExpirationDate;
   private int GracePeriod;
   private boolean isGranted;
   //a constructor is created with parameters
   public creditcard(int cardid,String issuerbank,String bankaccount,double balanceamount,int CVCnumber,double InterestRate,String ExpirationDate,String clientname)
    {
        
       super(cardid,issuerbank,bankaccount,balanceamount);
       super.setclientname(clientname);
       this.ExpirationDate=ExpirationDate;
       this.CVCnumber=CVCnumber;
       this.InterestRate=InterestRate;
       this.isGranted=false;
   }
   /**
    * seven getter method is created that returns the value of variable
   */
   public int getCVCnumber()
   {
       return this.CVCnumber;
   }
   public double getCreditLimit()
   {
      return this.CreditLimit; 
   }
   public double getInterestRate()
   {
       return this.InterestRate;
   }
   public String getExpiritionDate()
   {
       return this.ExpirationDate;
    }
  
   public int getGracePeriod()
    {
        return this.GracePeriod;
    }
   public boolean isGranted()
    {
        return this.isGranted;
    }
    /**
   * Two setter method is created that gives new of instance variable
   */
    public void setCreditLimit(double newCreditLimit,int newGraceperiod)
    {
        if(this.CreditLimit<=2*super.getbalanceamount())
        {this.CreditLimit=CreditLimit;
         this.GracePeriod=GracePeriod;
         this.isGranted=true;
         System.out.println("credit card granted");
    }
    else
    {
        System.out.println("sorry sir/maam please try again later");
    }
    }
    public void cancelcreditcard()
    {
        this.CVCnumber=0;
        this.CreditLimit=0;
        this.GracePeriod=0;
        this.isGranted=false;
    }
     
    public void display()
    {
       super.Display(); 
        if(isGranted == true)
    {
       System.out.println("CreditLimit is " + CreditLimit);
       System.out.println("Graceperiod is " + GracePeriod);
       
    }
    else
    {
       
       System.out.println("Your CVCnumber is:" + CVCnumber);
       System.out.println("Your InterestRate is:" + InterestRate);
       System.out.println("Your card ExpirationDate is:" + ExpirationDate);
       System.out.println("your card is granted"+ isGranted);
       
        
        
    }
}
}