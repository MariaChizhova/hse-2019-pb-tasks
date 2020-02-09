{-# LANGUAGE ScopedTypeVariables #-}
import Yat
import Test.HUnit
import System.Exit

checkGE name got expected = TestLabel name $ TestCase $ assertEqual "" expected got
group name elems = TestLabel name $ TestList elems

(/+) = BinaryOperation Add
(/*) = BinaryOperation Mul
(/-) = BinaryOperation Sub
(|||) = BinaryOperation Or
(===) = BinaryOperation Eq
iff = Conditional
(=:=) = Assign
c = Number
r = Reference
call = FunctionCall

infixl 6 /+
infixl 6 /-
infixl 7 /*
infixr 2 |||
infix 4 ===
infixr 1 =:=

program1 = ([("fib", ["a"], iff ((r "a" === c 0) ||| (r "a" === c 1)) (Block [c 1]) ((call "fib" [(r "a" /- c 1)]) /+ (call "fib" [(r "a" /- c 2)])))], call "fib" [c 25])
program2 = ([], Block ["a" =:= c 10, Block [], "b" =:= c 20, r "a" /+ (r "b" /* r "a")])
program3 = (
    [
        ("f", ["param"],
            Block [
            "a" =:= r "a" /+ c 1,
            "param" =:= r "param" /+ c 1,
            r "a" /* c 100 /+ r "b" /* c 10 /+ r "param"
            ]
        )
    ],
    Block [
        "a" =:= c 2,
        "b" =:= c 7,
        "res" =:= call "f" [BinaryOperation Add (c 1) (UnaryOperation Not ("a" =:= c 3))],
        "b" =:= r "b" /+ c 1,
        r "res" /* c 100 /+ r "b" /* c 10 /+ r "a"
    ]
 )
program4 = ([],
    Block [
        r "a" /+ iff
            (Block [("a" =:= c 3) /* c 4, r "a"])
            (c 4)
            (Block [
                Block [],
                Block [
                    "b" =:= ("c" =:= c 5)
                ],
                Block []
            ])
    ]
 )
program5 = ([],
    iff ("res" =:= (("a" =:= c 3) /* c 10 /+ ("a" =:= r "a" /+ (c 2 ||| ("b" =:= c 5)))))
    (Block [
        (r "res") /* c 1000 /+ r "a" /* c 100 /+ r "b" /* c 10 /+ (c 1 /+ Block [])
    ])
    (Block [])
 )

testAll = TestList [
    group "program1" [
      checkGE "output" (showProgram program1) $ concat [
        "func fib(a) = if ((a == 0) || (a == 1)) then {\n",
        "\t1\n",
        "} else (fib((a - 1)) + fib((a - 2))) fi\n",
        "fib(25)"
      ],
      checkGE "result" (eval program1) $ 121393
    ],
    group "program2" [
      checkGE "output" (showProgram program2) $ concat [
        "{\n",
        "\tlet a = 10 tel;\n",
        "\t{\n",
        "\t};\n",
        "\tlet b = 20 tel;\n",
        "\t(a + (b * a))\n",
        "}"
      ],
      checkGE "result" (eval program2) $ 210
    ],
    group "program3" [
      checkGE "output" (showProgram program3) $ concat [
        "func f(param) = {\n",
        "\tlet a = (a + 1) tel;\n",
        "\tlet param = (param + 1) tel;\n",
        "\t(((a * 100) + (b * 10)) + param)\n",
        "}\n",
        "{\n",
        "\tlet a = 2 tel;\n",
        "\tlet b = 7 tel;\n",
        "\tlet res = f((1 + !let a = 3 tel)) tel;\n",
        "\tlet b = (b + 1) tel;\n",
        "\t(((res * 100) + (b * 10)) + a)\n",
        "}"
      ],
      checkGE "result" (eval program3) $ 47283
    ],
    group "program4" [
      checkGE "output" (showProgram program4) $ concat [
        "{\n",
        "\t(a + if {\n",
        "\t\t(let a = 3 tel * 4);\n",
        "\t\ta\n",
        "\t} then 4 else {\n",
        "\t\t{\n",
        "\t\t};\n",
        "\t\t{\n",
        "\t\t\tlet b = let c = 5 tel tel\n",
        "\t\t};\n",
        "\t\t{\n",
        "\t\t}\n",
        "\t} fi)\n",
        "}"
      ]
    ],
    group "program5" [
      checkGE "output" (showProgram program5) $ concat [
        "if let res = ((let a = 3 tel * 10) + let a = (a + (2 || let b = 5 tel)) tel) tel then {\n",
        "\t((((res * 1000) + (a * 100)) + (b * 10)) + (1 + {\n",
        "\t}))\n",
        "} else {\n",
        "} fi"
      ],
      checkGE "result" (eval program5) $ 34451
    ]
  ]

main = do
  results <- runTestTT testAll
  exitWith $ if errors results + failures results == 0 then ExitSuccess else ExitFailure 1
