Rock-Paper-Scissors-Lizard-Spock
================================

Rock-Paper-Scissors-Lizard-Spock game using modulo inspired by Coursera's "An Introduction to Interactive Programming in Python"
Game isn't case sensitive.
Entering a String that is not a valid game choice raises an Exception

issues:
try-except block is currently around the main function call and should probably be moved to where the exception-raising helper function is called (inside rpsls function)
