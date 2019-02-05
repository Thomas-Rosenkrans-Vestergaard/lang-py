from exceptions import RuntimeException
from runtime import ProgramExecutor
import sys

def run(code):
    try:
        # resource.setrlimit(resource.RLIMIT_STACK, [0x10000000, resource.RLIM_INFINITY])
        sys.setrecursionlimit(0x100000)
        executor = ProgramExecutor()
        executor.execute(code)
    except RuntimeException as e:
        print("An error occurred:")
        print(e.user_message)


run("""

class Person {
    
    var name;
    var age;
    
    new(name, age) {
        this.name = name;
        this.age = age;
    }
    
    func get_description() {
        return 'Name is ' + this.name + ', age is ' + as_string(this.age); 
    }
}

const NAME = 'Thomas';
const COOL = true;
const PI = 3.14;
const NULLABLE = null;

func list_map(list, callback) {
    var s = size(list);
    var result = [];
    for(var i = 0; i < s; i++)
        list_push(result, callback.(list[i], i, list));
        
    return result;
}

func list_each(list, callback) {
    var s = size(list);
    for(var i = 0; i < s; i++)
        callback.(list[i], i, list);
}

func list_reduce(list, initial, callback) {
    var s = size(list);
    var acc = initial;
    for(var i = 0; i < s; i++)
        acc = callback.(acc, list[i], i, list);
        
    return acc;
}

func fib(n) {
    if(n < 2)
        return n;
    
    return fib(n - 1) + fib(n - 2); 
}

func sum(a, b) {
    return a + b;
}

func recursive_sum(n) {
    if(n < 2)
        return n;
    
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

var names = ['Thomas', 'Alexander', 'Martin'];
for(var x = 0; x < size(names); ++x)
    print_ln(names[x]);


print_ln('Alexander' != names[1]);
print_ln(size('Alexander'));

var map = {
    'Thomas': 'Cool After School',
    'Alexander': 'Fat'
};

print_ln(map);
print_ln(map['Alexander']);
print_ln(size(map));

map['Kasper'] = 'Nice';
print_ln(map['Kasper']);
print_ln(map['Unknown']);

var person = new Person('Thomas', 21);
print_ln(person.get_description());

var cls = () => 'Alexander';
print_ln('result=' + cls.());

var numbers = [1, 2, 3, 4, 5];
var squared = list_map(numbers, (n) => n ^ 2);
list_each(squared, (n) => print_ln(n));
print_ln(type (n) => n);


print(list_reduce([1, 2, 3, 4, 5], 0, (acc, n) => acc + n));

""")