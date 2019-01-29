from runtime import ProgramExecutor


def run(code):
    executor = ProgramExecutor()
    executor.execute(code)


run("""

const NAME = 'Thomas';
const COOL = true;
const PI = 3.14;
const NULLABLE = null;

func sum(a, b) {
    return a + b;
}

func recursive_sum(n) {
    if(n < 2)
        return 1;
    
    return n + recursive_sum(n - 1);
}

func some_function(a1, a2, a3){
    a1();
    b2();
    c3();
}

func some_other_function(a4, a5, a6){}

var name = 'Thomas';
var age = 21;
var condition = false;

if (condition) {
    print_ln('The condition is true');
} else {
    print_ln('The condition is false');
}

print_ln('while test');
var n = 5;
while (n > 0) {
    print_ln(n);
    n = n - 1;
}

print_ln('arithmetic test');
print_ln(5 + 4 * 2);

print_ln('for test');
for (var b = 0; b < 5; ++b)
    print_ln(b);

print_ln(type 'Thomas');
print_ln(!true);
print_ln(!false);
print_ln(8 ^ 3);

print_ln(sum(5, 6));

var sum = 0;
for (var o = 1; o <= 10; ++o) {
    sum = sum(sum, o);
}

print_ln(sum);
print_ln(recursive_sum(10));

""")
