class Money(val a:Int, val c:String) {
    var amount: Int = a
    var currency: String = c
    
    // override
    override def toString = amount.toString ++ " " ++ currency
}

// create instance of class
val money = new Money(220, "EUR")
money.amount, money.currency                // (220,EUR)

println(money)                              // 220 EUR

// subclasses
class VirtualMoney(override val a:Int, override val c:String, val d:String) extends Money(a, c) {
    var date: String = d
    
    // override
    override def toString = amount.toString ++ " " ++ currency ++ " (use before " ++ date ++ ")"
}

val virtual_money = new VirtualMoney(20, "DIS", "2018-12-31")

println(virtual_money)                      // 20 DIS (use before 2018-12-31)