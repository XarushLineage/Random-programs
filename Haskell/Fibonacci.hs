-- Define the `fib` function, which calculates the nth Fibonacci number
fib :: Int -> Int
fib 0 = 0
fib 1 = 1
fib n = fib (n-1) + fib (n-2)

-- Define the `main` function, which prompts the user for input, generates a list of the first `n` Fibonacci numbers, and prints them to the console
main :: IO ()
main = do
    -- Prompt the user to enter the number of Fibonacci numbers to display
    putStrLn "Enter the number of Fibonacci numbers to display:"

    -- Read the user's input as a string
    nStr <- getLine

    -- Convert the user's input to an `Int`
    let n = read nStr :: Int

    -- Generate a list of the first `n` Fibonacci numbers using `map` and `fib`
    let fibs = map fib [0..n-1]

    -- Print each Fibonacci number to the console using `mapM_` and `print`
    mapM_ print fibs
