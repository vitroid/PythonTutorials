subroutine lattice(L, pos)
  implicit none

  integer, intent(IN)       :: L
  real(kind=8), intent(OUT) :: pos(L*L*L,3)

  integer :: n,i,j,k

  n = 0
  do i=1,L
     do j=1,L
        do k=1,L
           n = n + 1
           pos(n,1) = i
           pos(n,2) = j
           pos(n,3) = k
        end do
     end do
  end do
end subroutine lattice


subroutine distrib(N, pos, L, dmax, ndiv, d)
  implicit none

  integer, intent(IN)      :: N
  real(kind=8), intent(IN) :: pos(N,3)
  real(kind=8), intent(IN) :: L
  integer, intent(IN)      :: ndiv, dmax
  real(kind=8), intent(OUT) :: d(dmax*ndiv)
  
  integer      :: i, j, ir
  real(kind=8) :: p1(3), p2(3), dp(3), r
  
  do i=1,N
     p1(:) = pos(i,:)
     do j=i+1, N
        p2(:) = pos(j,:)
        dp(:) = p1(:) - p2(:)
        dp(:) = dp(:) - dnint(dp(:) / L)*L
        r = (dp(1)**2 + dp(2)**2 + dp(3)**2) ** 0.5
        ir = int(r*ndiv)
        if ( ir < dmax*ndiv ) then
           d(ir+1) = d(ir+1) + 1
        end if
     end do
  end do
end subroutine distrib


program main
  implicit none

  integer, parameter :: L=20
  real(kind=8) :: pos(L**3, 3)
  integer :: i
  real(kind=8) :: LL, d(50)

  LL = L
  call lattice(L, pos)
  call distrib(L**3, pos, LL, 5, 10, d)
  do i=1,50
     print *, i-1,d(i)
  end do
end program main
