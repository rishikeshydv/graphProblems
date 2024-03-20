let rec power x n = 
  match n with
  | 0 -> 1
  | 1 -> x
  | _ -> x * power x (n-1)
