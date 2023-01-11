#from csp import Constraint, CSP
from typing import Dict, List, Optional

from csp import CSP, Constraint


class SendMoreMoneyConstraint(Constraint[str, int]):
  def __init__(self, letters: List[str])->None:
    super().__init__(letters)
    self.letters:List[str] = letters

  def satisfied(self,assignment: Dict[str,int])-> bool:
    #値が重複した場合、解とならない
    if len(set(assignment.values())) < len(assignment):
      return False

    if len(assignment) == len(self.letters):
      s:int = assignment["S"]
      e:int = assignment["E"]
      n:int = assignment["N"]
      d:int = assignment["D"]
      m:int = assignment["M"]
      o:int = assignment["O"]
      r:int = assignment["R"]
      y:int = assignment["Y"]
      send: int = s * 1000 + e * 100 + n * 10 + d
      more: int = m * 1000 + o * 100 + r * 10 + e
      money: int = m * 10000 + o * 1000 + n * 100 + e * 10 + y
      return send + more == money
    return True # 矛盾しない

if __name__ == "__main__":
  letters: List[str] = ["S","E","N","D","M","O","R","Y",]
  possible_digits: Dict[str, List[int]] = {}
  for letter in letters:
    possible_digits["M"] = [1] #0で始まる解は出ない
    csp: CSP[str,int] = CSP(letters, possible_digits)
    csp.add_constraint(SendMoreMoneyConstraint(letters))
    solution: Optional[Dict[str,int]] = csp.backtracking_search()
    if solution is None:
      print("No solution found!")
    else:
      print(solution)
