subroutine sqrt_sum(n, sum)
  implicit none

  integer, intent(IN) :: n
  real(kind=8), intent(OUT) :: sum

  integer :: i

  sum = 0.0
  do i=1,n
    sum = sum + i**0.5
 end do
end subroutine sqrt_sum

program main
  real(kind=8) :: sum
  call sqrt_sum(100000000, sum)
  print *, sum
end program main
