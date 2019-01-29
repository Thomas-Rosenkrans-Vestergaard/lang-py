from runtime import ProgramExecutor


def run(code):
    executor = ProgramExecutor()
    executor.execute(code)


run("""

const NAME = 'Thomas';
const COOL = true;
const PI = 3.14;
const NULLABLE = null;

func some_function(a1, a2, a3){
    a1();
    b2();
    c3();
}
func some_other_function(a4, a5, a6){}

var name = 'Thomas';
var age = 21;
var cond = true;

if (condition) {
    a4();
} else if (condition) {
    b5();
} else {
    c6();
}

""")
