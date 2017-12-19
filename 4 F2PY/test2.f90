subroutine division(a,b,c,d)
  implicit none

  integer, intent(IN) :: a,b
  integer, intent(OUT) :: c,d

  c = a / b
  d = mod(a,b)
end subroutine division

program main
  integer :: c,d
  call division(10,7,c,d)
  print *, c,d
end program main
