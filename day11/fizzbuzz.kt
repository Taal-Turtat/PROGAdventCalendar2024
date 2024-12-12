
fun main(){
    var n = readLine()?.toInt()

    n = n ?: 15
    for (i in 1..n){
        if(i % 3 == 0) {print("fizz")}
        if(i % 5 == 0) {print("buzz")}
        print("\n")
    }
}