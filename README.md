# 5-8-Paint-Job-Estimator
 Calculates a labor and material estimate using value-returning functions

 ## Scope
 A painting company has determined that for every 112 square feet of wall space, one gallon of paint and eight hours of labor will be required to paint the space. The company charges $35.00 per hour for labor. Write a program that asks the user to enter the square feet of wall space to be painted and the price of the paint per gallon. The program should display the following data:

*  The number of gallons of paint required
*  The hours of labor required
*  The cost of the paint
*  The labor charges
*  The total cost of the paint job

*Hints:* Create global constants for feet per gallon (112), labor hours (8), and labor charge (35). Use a function to print the results.

## Sample Run
    Enter wall space in square feet:  586
    Enter paint price per gallon:  38.50
    Gallons of paint:  6
    Hours of labor:  48
    Paint charges: $231.00
    Labor charges: $1,680.00
    Total cost: $1,911.00

## Pseudocode
### Program Flow
    START
      SET feet per gallon constant to 112
      SET labor hours constant to 8
      SET labor cost constant to 35.00
      CALL main function
    END

### main function
    START
      INPUT wall space in square feet
      INPUT price per gallon
      CALL cost_estimate function
    END

### cost_estimate function
    START
      PASS IN: wall space, price per gallon
      CALCULATE gallons of paint needed
        IF wall space % feet per gallon = 0
          divide wall space by feet per gallon
        ELSE
          divide wall space by feet per gallon and add 1
        ENDIF
      CALCULATE labor needed
        multiply gallons of paint needed by labor hours
      CALCULATE labor cost
        multiply labor needed by labor cost
      CALCULATE paint cost
        multiply gallons of paint needed by price per gallon
      CALCULATE total estimate
        labor cost + paint cost
      PRINT gallons of paint needed
      PRINT labor needed
      PRINT paint cost
      PRINT labor cost
      PRINT total estimate
    END
