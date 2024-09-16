/**
 * Debit_card is a subclass of Bankcard and also extends Bankcard.it has variable,methods,constructors and a 
 * display method
 * @22067054 Arbin Rajbanshi
 * @26 jan 2023
 */
public class Debit_card extends Bankcard
{   
    //four instance variable is created with suitable data types
    private double withdrawalamount;
    private String dateofwithdrawal;
    private boolean haswithdrawn;
    private int pinnumber;
    
    // a constructor is created with paramters
    public Debit_card (String issuerbank,int cardid,double balanceamount,String bankaccount,String clientname,int pinnumber)
  {
   
   super(cardid,issuerbank,bankaccount,balanceamount);
   super.setclientname(clientname);
   this.pinnumber=pinnumber;
   this.haswithdrawn=false;
}
/**
 * four getter method is created that returns the value of variable
 */
   public int getpinNumber()
   {
       return this.pinnumber;
   }
   public double getwithdrawalamount()
   {
     return this.withdrawalamount;
   }
   public String getdateofwithdrawal()
   {
        return this.dateofwithdrawal;
   }
   public boolean gethaswithdrawn()
   {   
        return this.haswithdrawn;
   }
   /**
    * Two setter method is created that gives new of instance variable
    */
   public void setwithdrawalamount(double withdrawalamount)
   {
       this.withdrawalamount=withdrawalamount;
   }
   public void withdrawn(double withdrawalamount, String dateofwithdrawal,int pinnumber)
   {
       if(this.pinnumber==pinnumber&&withdrawalamount<=getbalanceamount())
       {
           this.haswithdrawn=true;
           this.setbalanceamount(this.getbalanceamount()-withdrawalamount);
           this.withdrawalamount=withdrawalamount;
           this.dateofwithdrawal=dateofwithdrawal;
           
           System.out.println("Transaction succesfull");
           System.out.println("withdrawal amount is;"+ withdrawalamount);
           System.out.println("balance is"+ super.getbalanceamount());
           System.out.println("Date of transaction"+ getdateofwithdrawal());
       }
       else
       {
           System.out.println("you may have insufficient balance in your account or you may entered wrong number");
       }
    }
    public void Display()
    {
        super.Display();
        if(haswithdrawn == true)
        {
            System.out.println("pinnumber is" + pinnumber);
            System.out.println("withdrawalamount is" + withdrawalamount);
            System.out.println("dateofwithdrawn is" + dateofwithdrawal );
        }
        else
        { 
            System.out.println("Your balanceamount is " + getbalanceamount());
    }
}
}
