{-# LANGUAGE ScopedTypeVariables #-}
import Exercises
import Test.HUnit
import System.Exit

check name a b = TestLabel name $ TestCase $ assertEqual "" a b
group name elems = TestLabel name $ TestList elems

testAll = TestList [
    group "First task" [
      check "sum''" 15 $ sum'' 10 [2, 3],
      check "concat''" "abc" $ concat'' "c" ["a", "b"],
      check "hash''" 4077 $ hash'' 10 "AB",
      check "foldr'" "(a,(b,end))" $ foldr' (\a b -> "(" ++ a ++ "," ++ b ++ ")") "end" ["a", "b"],
      check "map'" [1,4,9] $ map' (^2) [1,2,3]
    ],
    group "Second task" [
      group "thirdElementOfSecondList" [
        check "[]" Nothing $ thirdElementOfSecondList ([]::[String]),
        check "[abcd]" Nothing $ thirdElementOfSecondList ["abcd"],
        check "[[], [1,2], [3,4]]" Nothing $ thirdElementOfSecondList [[], [1, 2], [3, 4]],
        check "[[a], [b, c, d]]" (Just "d") $ thirdElementOfSecondList [["a"], ["b", "c", "d"]]
      ],
      group "fifthElement" [
        check "[]" Nothing $ fifthElement ([]::[String]),
        check "abcd" Nothing $ fifthElement "abcd",
        check "[1, 2, 3, 4, 5]" (Just 5) $ fifthElement [1, 2, 3, 4, 5]
      ],
      group "thirdElementOfSecondList'" [
        check "[]" Nothing $ thirdElementOfSecondList' ([]::[String]),
        check "[abcd]" Nothing $ thirdElementOfSecondList' ["abcd"],
        check "[[], [1,2], [3,4]]" Nothing $ thirdElementOfSecondList' [[], [1, 2], [3, 4]],
        check "[[a], [b, c, d]]" (Just "d") $ thirdElementOfSecondList' [["a"], ["b", "c", "d"]]
      ]
    ],
    group "Third task" [
      group "nubBy'" [
        check "[]" [] $ nubBy' (==) ([]::[String]),
        check "abaacbad" "abcd" $ nubBy' (==) "abaacbad",
        check "== or sum is 10" [2, 3, 5] $ nubBy' (\x y -> x == y || x + y == 10) [2, 3, 5, 7, 8, 2]
      ],
      group "quickSort'" [
        check "[]" [] $ quickSort' ([]::[Int]),
        check "[2, 3, 1, 2]" [1, 2, 2, 3] $ quickSort' [2, 3, 1, 2],
        check "babca" "aabbc" $ quickSort' "babca"
      ],
      group "weird'" [
        check "[]" 0 $ weird' [],
        check "[]" 5 $ weird' [[1, 2, 3], [4, 5], [1, 2, 11]],
        check "[]" 3 $ weird' [[1, 11, 12], [9, 10, 20]]
      ]
    ],
    group "Fourth task" [
      check "grep'" ["ab", "ac"] $ grep' (\_ s -> s) ((== 'a') . head) [("a.txt", ["ab", "b"]), ("b.txt", ["b", "ac"])],
      group "grepSubstringNoFilename" [
        check "short test" ["b"] $ grepSubstringNoFilename "b" [("a.txt", ["a", "b"])],
        check "long test" ["c", "c", "ccccc"] $ grepSubstringNoFilename "c" [("a.txt", ["a", "a"]), ("b.txt", ["b", "bab", "c"]), ("c.txt", ["c", "ccccc"])]
      ],
      group "grepExactMatchWithFilename" [
        check "short test" ["a.txt:b"] $ grepExactMatchWithFilename "b" [("a.txt", ["a", "b"])],
        check "long test" ["b.txt:c", "c.txt:c"] $ grepExactMatchWithFilename "c" [("a.txt", ["a", "a"]), ("b.txt", ["b", "bab", "c"]), ("c.txt", ["c", "ccccc"])]
      ]
    ]
  ]

main = do
  results <- runTestTT testAll
  exitWith $ if errors results + failures results == 0 then ExitSuccess else ExitFailure 1
