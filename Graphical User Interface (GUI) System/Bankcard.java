
/**
 * Bank card is a parent class which carry two sub classes(Debit_card and creditcard) and it has variable,methods,constructors and a 
 * display method
 *
 * @22067054 Arbin Rajbanshi
 * @26 jan 2023
 */
public class Bankcard
{
    //five instance variable is made with suitable data types 
  private String clientname;
  private String issuerbank;
  private int cardid;
  private double balanceamount;
  private String bankaccount;
  //a constructor is made with parameters
  public Bankcard (int cardid,String issuerbank,String bankaccount,double balanceamount)
  {
     
    this.clientname="";
    this.issuerbank=issuerbank;
    this.cardid=cardid;
    this.balanceamount=balanceamount;
    this.bankaccount=bankaccount;
  }
  /**
   * five getter method is created that returns the value of variable
   */
  public String getclientname()
  {
  return this.clientname;
  }
  public String getissuername()
  {
      return this.issuerbank;
  }
  public int getcardid()
  {
  return this.cardid;
  }
  public double getbalanceamount()
  {
      return this.balanceamount;
  }
  /**
   * Two setter method is created that gives new of instance variable
   */
  public String getbankaccount()
  {
      return this.bankaccount;
  }
  public void setclientname(String clientname)
  {
     this.clientname=clientname; 
  }
  public void setbalanceamount(double balanceamount)
  {
      this.balanceamount=balanceamount;
  }
  /**
   * A display method is to print the output
   */
  public void Display()
  {
      System.out.println("This is issuername " + issuerbank);
      System.out.println("This is cardid " + cardid);
      System.out.println("This is balanceaccount " + balanceamount);
      System.out.println("This is bankaccount " + bankaccount);
      
      if (clientname=="") 
      {
      System.out.println("This client_name attribute is empty");
    }
    else
    {
        System.out.println("This is your clientname " + clientname);
    }
    } 
    }
    
       
 
  
  
