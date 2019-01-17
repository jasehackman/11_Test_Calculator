class Calculator():
    """Performs the four basic mathematical operations

    Methods:
     add(number, number)
     subtract(number, number)
     multiply(number, number)
     divide(number,number)
    """

    def add(self, firstOperand, secondOperand):
      """Adds two numbers together

      Arguments:
        firstOperand - Any number
        secondOperand - An number
      """
      if isinstance(firstOperand, int) & isinstance(secondOperand, int):
        return firstOperand + secondOperand
      else:
        return "not a number"

    def subtract(self, firstOperand, secondOperand):
      """Subtracts two numbers together

      Arguments:
        firstOperand - Any number
        secondOperand - An number
      """
      if isinstance(firstOperand, int) & isinstance(secondOperand, int):
        return firstOperand - secondOperand
      else:
        return "not a number"

    def mult(self, firstOperand, secondOperand):
      """Multiply two numbers together

      Arguments:
        firstOperand - Any number
        secondOperand - An number
      """
      if isinstance(firstOperand, int) & isinstance(secondOperand, int):
        return firstOperand * secondOperand
      else:
        return "not a number"

    def div(self, firstOperand, secondOperand):
      """Divide two numbers together

      Arguments:
        firstOperand - Any number
        secondOperand - An number
      """
      if isinstance(firstOperand, int) & isinstance(secondOperand, int):
        return firstOperand / secondOperand
      else:
        return "not a number"

# if __name__ == '__main__':
