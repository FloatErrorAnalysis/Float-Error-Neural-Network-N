; ModuleID = '../../cpp_raw/add/sqrt_minus2.cpp'
target datalayout = "e-p:64:64:64-i1:8:8-i8:8:8-i16:16:16-i32:32:32-i64:64:64-f32:32:32-f64:64:64-v64:64:64-v128:128:128-a0:0:64-s0:64:64-f80:128:128-n8:16:32:64-S128"
target triple = "x86_64-redhat-linux-gnu"

; Function Attrs: nounwind uwtable
define double @_Z16sqrt_minus_errord(double %x) #0 {
  %1 = alloca double, align 8
  store double %x, double* %1, align 8
  %2 = load double* %1, align 8
  %3 = fadd double %2, 3.000000e+00
  %4 = call double @sqrt(double %3) #2
  %5 = load double* %1, align 8
  %6 = fadd double %5, 2.000000e+00
  %7 = call double @sqrt(double %6) #2
  %8 = fsub double %4, %7
  ret double %8
}

; Function Attrs: nounwind
declare double @sqrt(double) #1

attributes #0 = { nounwind uwtable "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "stack-protector-buffer-size"="8" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #1 = { nounwind "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "stack-protector-buffer-size"="8" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #2 = { nounwind }

!llvm.ident = !{!0}

!0 = metadata !{metadata !"clang version 3.4.2 (tags/RELEASE_34/dot2-final)"}
