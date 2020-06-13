#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) The assignment of a is constant O(1) time. The while loop will run O(n) times. The variable `a` is incremented each time by n\*n, which should be constant time. The total time complexity should be O(1 + n + 1) which would reduce to O(n).

b) The assignment of the `sum` variable is constant time O(1). The outer loop time complexity is O(n), multiplied by the time complexities of the operations inside it. The assignment of `j` inside the for loop is also O(1). The while loop will double in each iteration, making it O(log n). The assignments inside of the loop are each O(1). When you add everything together you end up with O(1 + O(n) _ O(log n) _ O(1 + 1)) -> O(n log n)

c) This should run in O(n) time because the counter will reduce by one on each iteration of the loop, meaning that the function will be called recursively n times.

## Exercise II

Unlimited amount of eggs:
I think we could treat this problem like the phonebook example that we talked about in class. We can set the min at floor 1, and the max at floor f. We can find the midpoint using math (min + max) / 2. And we drop an egg from the midpoint. If the egg breaks, we know we need to move lower. So we can find a new midpoint using the previous midpoint as the new max, and repeat the process. If the egg doesn't break on the intial drop, then we can select a new higher midpoint. Because we're eliminating half of the options with each drop this should run in O(log n) time.

Limited amount of eggs:
If the amount of eggs is finite, then we need to start from the first floor and drop an egg to see if it breaks, and then work our way up from the bottom. This requires us to "iterate" through each floor until we find the floor where the egg breaks, and then we know we're one floor too high. This would run in O(n) time, which is considerably slower than if we have no limit on the eggs we can drop.
