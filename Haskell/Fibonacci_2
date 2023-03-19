-- Define the `fib` function, which generates the list of Fibonacci numbers up to `n`
fib :: Int -> [Int]
fib n = takeWhile (<=n) $ 0 : 1 : zipWith (+) fibs (tail fibs)
    where fibs = fib n

-- Define the `findFib` function, which finds the position of a number in the Fibonacci sequence
findFib :: Int -> Maybe Int
findFib n = elemIndex n (fib n)

-- Define the `main` function, which prompts the user for input, checks if the input is a Fibonacci number, and prints its position if it is
main :: IO ()
main = do
    -- Prompt the user to enter a number
    putStrLn "Enter a number:"

    -- Read the user's input as a string
    nStr <- getLine

    -- Convert the user's input to an `Int`
    let n = read nStr :: Int

    -- Check if the input number is a Fibonacci number
    let fibIndex = findFib n

    -- Print the result
    case fibIndex of
        Just i -> putStrLn $ show n ++ " is the " ++ show (i+1) ++ "th Fibonacci number."
        Nothing -> putStrLn $ show n ++ " is not a Fibonacci number."
