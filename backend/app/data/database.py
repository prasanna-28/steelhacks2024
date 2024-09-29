from data.dataparser import *

DATABASE_textbook = {
    "PHYS 2373": {
        "content": """
CONTENTS
Preface xi
1 Vector Analysis 1
1.1 Definitions, Elementary Approach ..................... 1
1.2 Rotation of the Coordinate Axes ...................... 7
1.3 Scalar or Dot Product . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
1.4 Vector or Cross Product . . . . . . . . . . . . . . . . . . . . . . . . . . 18
1.5 Triple Scalar Product, Triple Vector Product . . . . . . . . . . . . . . . 25
1.6 Gradient, ∇ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
1.7 Divergence, ∇ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
1.8 Curl, ∇× . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43
1.9 Successive Applications of ∇ . . . . . . . . . . . . . . . . . . . . . . . 49
1.10 Vector Integration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54
1.11 Gauss’ Theorem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60
1.12 Stokes’ Theorem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64
1.13 Potential Theory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68
1.14 Gauss’ Law, Poisson’s Equation . . . . . . . . . . . . . . . . . . . . . . 79
1.15 Dirac Delta Function . . . . . . . . . . . . . . . . . . . . . . . . . . . . 83
1.16 Helmholtz’s Theorem . . . . . . . . . . . . . . . . . . . . . . . . . . . . 95
Additional Readings . . . . . . . . . . . . . . . . . . . . . . . . . . . . 101
2 Vector Analysis in Curved Coordinates and Tensors 103
2.1 Orthogonal Coordinates in R
3
. . . . . . . . . . . . . . . . . . . . . . . 103
2.2 Differential Vector Operators . . . . . . . . . . . . . . . . . . . . . . . 110
2.3 Special Coordinate Systems: Introduction . . . . . . . . . . . . . . . . 114
2.4 Circular Cylinder Coordinates . . . . . . . . . . . . . . . . . . . . . . . 115
2.5 Spherical Polar Coordinates . . . . . . . . . . . . . . . . . . . . . . . . 123
v
vi Contents
2.6 Tensor Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 133
2.7 Contraction, Direct Product . . . . . . . . . . . . . . . . . . . . . . . . 139
2.8 Quotient Rule . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 141
2.9 Pseudotensors, Dual Tensors . . . . . . . . . . . . . . . . . . . . . . . 142
2.10 General Tensors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 151
2.11 Tensor Derivative Operators . . . . . . . . . . . . . . . . . . . . . . . . 160
Additional Readings . . . . . . . . . . . . . . . . . . . . . . . . . . . . 163
3 Determinants and Matrices 165
3.1 Determinants . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 165
3.2 Matrices . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 176
3.3 Orthogonal Matrices . . . . . . . . . . . . . . . . . . . . . . . . . . . . 195
3.4 Hermitian Matrices, Unitary Matrices . . . . . . . . . . . . . . . . . . 208
3.5 Diagonalization of Matrices . . . . . . . . . . . . . . . . . . . . . . . . 215
3.6 Normal Matrices . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 231
Additional Readings . . . . . . . . . . . . . . . . . . . . . . . . . . . . 239
4 Group Theory 241
4.1 Introduction to Group Theory . . . . . . . . . . . . . . . . . . . . . . . 241
4.2 Generators of Continuous Groups . . . . . . . . . . . . . . . . . . . . . 246
4.3 Orbital Angular Momentum . . . . . . . . . . . . . . . . . . . . . . . . 261
4.4 Angular Momentum Coupling . . . . . . . . . . . . . . . . . . . . . . . 266
4.5 Homogeneous Lorentz Group . . . . . . . . . . . . . . . . . . . . . . . 278
4.6 Lorentz Covariance of Maxwell’s Equations . . . . . . . . . . . . . . . 283
4.7 Discrete Groups . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 291
4.8 Differential Forms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 304
Additional Readings . . . . . . . . . . . . . . . . . . . . . . . . . . . . 319
5 Infinite Series 321
5.1 Fundamental Concepts . . . . . . . . . . . . . . . . . . . . . . . . . . . 321
5.2 Convergence Tests . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 325
5.3 Alternating Series . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 339
5.4 Algebra of Series . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 342
5.5 Series of Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 348
5.6 Taylor’s Expansion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 352
5.7 Power Series . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 363
5.8 Elliptic Integrals . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 370
5.9 Bernoulli Numbers, Euler–Maclaurin Formula . . . . . . . . . . . . . . 376
5.10 Asymptotic Series . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 389
5.11 Infinite Products . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 396
Additional Readings . . . . . . . . . . . . . . . . . . . . . . . . . . . . 401
6 Functions of a Complex Variable I Analytic Properties, Mapping 403
6.1 Complex Algebra . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 404
6.2 Cauchy–Riemann Conditions . . . . . . . . . . . . . . . . . . . . . . . 413
6.3 Cauchy’s Integral Theorem . . . . . . . . . . . . . . . . . . . . . . . . . 418
Contents vii
6.4 Cauchy’s Integral Formula . . . . . . . . . . . . . . . . . . . . . . . . . 425
6.5 Laurent Expansion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 430
6.6 Singularities . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 438
6.7 Mapping . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 443
6.8 Conformal Mapping . . . . . . . . . . . . . . . . . . . . . . . . . . . . 451
Additional Readings . . . . . . . . . . . . . . . . . . . . . . . . . . . . 453
7 Functions of a Complex Variable II 455
7.1 Calculus of Residues . . . . . . . . . . . . . . . . . . . . . . . . . . . . 455
7.2 Dispersion Relations . . . . . . . . . . . . . . . . . . . . . . . . . . . . 482
7.3 Method of Steepest Descents . . . . . . . . . . . . . . . . . . . . . . . . 489
Additional Readings . . . . . . . . . . . . . . . . . . . . . . . . . . . . 497
8 The Gamma Function (Factorial Function) 499
8.1 Definitions, Simple Properties . . . . . . . . . . . . . . . . . . . . . . . 499
8.2 Digamma and Polygamma Functions . . . . . . . . . . . . . . . . . . . 510
8.3 Stirling’s Series . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 516
8.4 The Beta Function . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 520
8.5 Incomplete Gamma Function . . . . . . . . . . . . . . . . . . . . . . . 527
Additional Readings . . . . . . . . . . . . . . . . . . . . . . . . . . . . 533
9 Differential Equations 535
9.1 Partial Differential Equations . . . . . . . . . . . . . . . . . . . . . . . 535
9.2 First-Order Differential Equations . . . . . . . . . . . . . . . . . . . . 543
9.3 Separation of Variables . . . . . . . . . . . . . . . . . . . . . . . . . . . 554
9.4 Singular Points . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 562
9.5 Series Solutions—Frobenius’ Method . . . . . . . . . . . . . . . . . . . 565
9.6 A Second Solution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 578
9.7 Nonhomogeneous Equation—Green’s Function . . . . . . . . . . . . . 592
9.8 Heat Flow, or Diffusion, PDE . . . . . . . . . . . . . . . . . . . . . . . 611
Additional Readings . . . . . . . . . . . . . . . . . . . . . . . . . . . . 618
10 Sturm–Liouville Theory—Orthogonal Functions 621
10.1 Self-Adjoint ODEs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 622
10.2 Hermitian Operators . . . . . . . . . . . . . . . . . . . . . . . . . . . . 634
10.3 Gram–Schmidt Orthogonalization . . . . . . . . . . . . . . . . . . . . . 642
10.4 Completeness of Eigenfunctions . . . . . . . . . . . . . . . . . . . . . . 649
10.5 Green’s Function—Eigenfunction Expansion . . . . . . . . . . . . . . . 662
Additional Readings . . . . . . . . . . . . . . . . . . . . . . . . . . . . 674
11 Bessel Functions 675
11.1 Bessel Functions of the First Kind, Jν (x) . . . . . . . . . . . . . . . . . 675
11.2 Orthogonality . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 694
11.3 Neumann Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . 699
11.4 Hankel Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 707
11.5 Modified Bessel Functions, Iν (x) and Kν (x) . . . . . . . . . . . . . . . 713
viii Contents
11.6 Asymptotic Expansions . . . . . . . . . . . . . . . . . . . . . . . . . . . 719
11.7 Spherical Bessel Functions . . . . . . . . . . . . . . . . . . . . . . . . . 725
Additional Readings . . . . . . . . . . . . . . . . . . . . . . . . . . . . 739
12 Legendre Functions 741
12.1 Generating Function . . . . . . . . . . . . . . . . . . . . . . . . . . . . 741
12.2 Recurrence Relations . . . . . . . . . . . . . . . . . . . . . . . . . . . . 749
12.3 Orthogonality . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 756
12.4 Alternate Definitions . . . . . . . . . . . . . . . . . . . . . . . . . . . . 767
12.5 Associated Legendre Functions . . . . . . . . . . . . . . . . . . . . . . 771
12.6 Spherical Harmonics . . . . . . . . . . . . . . . . . . . . . . . . . . . . 786
12.7 Orbital Angular Momentum Operators . . . . . . . . . . . . . . . . . . 793
12.8 Addition Theorem for Spherical Harmonics . . . . . . . . . . . . . . . 797
12.9 Integrals of Three Y’s . . . . . . . . . . . . . . . . . . . . . . . . . . . . 803
12.10 Legendre Functions of the Second Kind . . . . . . . . . . . . . . . . . . 806
12.11 Vector Spherical Harmonics . . . . . . . . . . . . . . . . . . . . . . . . 813
Additional Readings . . . . . . . . . . . . . . . . . . . . . . . . . . . . 816
13 More Special Functions 817
13.1 Hermite Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 817
13.2 Laguerre Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 837
13.3 Chebyshev Polynomials . . . . . . . . . . . . . . . . . . . . . . . . . . 848
13.4 Hypergeometric Functions . . . . . . . . . . . . . . . . . . . . . . . . . 859
13.5 Confluent Hypergeometric Functions . . . . . . . . . . . . . . . . . . . 863
13.6 Mathieu Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 869
Additional Readings . . . . . . . . . . . . . . . . . . . . . . . . . . . . 879
14 Fourier Series 881
14.1 General Properties . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 881
14.2 Advantages, Uses of Fourier Series . . . . . . . . . . . . . . . . . . . . 888
14.3 Applications of Fourier Series . . . . . . . . . . . . . . . . . . . . . . . 892
14.4 Properties of Fourier Series . . . . . . . . . . . . . . . . . . . . . . . . 903
14.5 Gibbs Phenomenon . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 910
14.6 Discrete Fourier Transform . . . . . . . . . . . . . . . . . . . . . . . . 914
14.7 Fourier Expansions of Mathieu Functions . . . . . . . . . . . . . . . . 919
Additional Readings . . . . . . . . . . . . . . . . . . . . . . . . . . . . 929
15 Integral Transforms 931
15.1 Integral Transforms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 931
15.2 Development of the Fourier Integral . . . . . . . . . . . . . . . . . . . . 936
15.3 Fourier Transforms—Inversion Theorem . . . . . . . . . . . . . . . . . 938
15.4 Fourier Transform of Derivatives . . . . . . . . . . . . . . . . . . . . . 946
15.5 Convolution Theorem . . . . . . . . . . . . . . . . . . . . . . . . . . . . 951
15.6 Momentum Representation . . . . . . . . . . . . . . . . . . . . . . . . . 955
15.7 Transfer Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 961
15.8 Laplace Transforms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 965
Contents ix
15.9 Laplace Transform of Derivatives . . . . . . . . . . . . . . . . . . . . . 971
15.10 Other Properties . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 979
15.11 Convolution (Faltungs) Theorem . . . . . . . . . . . . . . . . . . . . . 990
15.12 Inverse Laplace Transform . . . . . . . . . . . . . . . . . . . . . . . . . 994
Additional Readings . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1003
16 Integral Equations 1005
16.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1005
16.2 Integral Transforms, Generating Functions . . . . . . . . . . . . . . . . 1012
16.3 Neumann Series, Separable (Degenerate) Kernels . . . . . . . . . . . . 1018
16.4 Hilbert–Schmidt Theory . . . . . . . . . . . . . . . . . . . . . . . . . . 1029
Additional Readings . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1036
17 Calculus of Variations 1037
17.1 A Dependent and an Independent Variable . . . . . . . . . . . . . . . . 1038
17.2 Applications of the Euler Equation . . . . . . . . . . . . . . . . . . . . 1044
17.3 Several Dependent Variables . . . . . . . . . . . . . . . . . . . . . . . . 1052
17.4 Several Independent Variables . . . . . . . . . . . . . . . . . . . . . . . 1056
17.5 Several Dependent and Independent Variables . . . . . . . . . . . . . . 1058
17.6 Lagrangian Multipliers . . . . . . . . . . . . . . . . . . . . . . . . . . . 1060
17.7 Variation with Constraints . . . . . . . . . . . . . . . . . . . . . . . . . 1065
17.8 Rayleigh–Ritz Variational Technique . . . . . . . . . . . . . . . . . . . 1072
Additional Readings . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1076
18 Nonlinear Methods and Chaos 1079
18.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1079
18.2 The Logistic Map . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1080
18.3 Sensitivity to Initial Conditions and Parameters . . . . . . . . . . . . . 1085
18.4 Nonlinear Differential Equations . . . . . . . . . . . . . . . . . . . . . 1088
Additional Readings . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1107
19 Probability 1109
19.1 Definitions, Simple Properties . . . . . . . . . . . . . . . . . . . . . . . 1109
19.2 Random Variables . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1116
19.3 Binomial Distribution . . . . . . . . . . . . . . . . . . . . . . . . . . . 1128
19.4 Poisson Distribution . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1130
19.5 Gauss’ Normal Distribution . . . . . . . . . . . . . . . . . . . . . . . . 1134
19.6 Statistics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1138
Additional Readings . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1150
General References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1150
Index 1153
                """,
        "url"    : "https://msashigri.wordpress.com/wp-content/uploads/2016/11/methods-of-mathemacial-for-physicists.pdf"
    },
    "MATH 1020": {
        "content": """
Contents
Preface xi
Acknowledgements xvii
0 Getting started 1
0.E Chapter 0 exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
I Core concepts 23
1 Logical structure 25
1.1 Propositional logic . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
1.2 Variables and quantifiers . . . . . . . . . . . . . . . . . . . . . . . . . 49
1.3 Logical equivalence . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63
1.E Chapter 1 exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . 81
2 Sets 85
2.1 Sets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 86
2.2 Set operations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 98
v
vi Contents
2.E Chapter 2 exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . 108
3 Functions 113
3.1 Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 114
3.2 Injections and surjections . . . . . . . . . . . . . . . . . . . . . . . . . 130
3.E Chapter 3 exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . 145
4 Mathematical induction 151
4.1 Peano’s axioms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 152
4.2 Weak induction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 159
4.3 Strong induction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 174
4.E Chapter 4 exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . 182
5 Relations 185
5.1 Relations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 186
5.2 Equivalence relations and partitions . . . . . . . . . . . . . . . . . . . 196
5.E Chapter 5 exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . 208
6 Finite and infinite sets 211
6.1 Finite sets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 212
6.2 Countable and uncountable sets . . . . . . . . . . . . . . . . . . . . . . 222
6.E Chapter 6 exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . 236
II Topics in pure mathematics 237
7 Number theory 239
7.1 Division . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 240
vi
Contents vii
7.2 Prime numbers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 255
7.3 Modular arithmetic . . . . . . . . . . . . . . . . . . . . . . . . . . . . 264
7.E Chapter 7 exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . 290
8 Enumerative combinatorics 293
8.1 Counting principles . . . . . . . . . . . . . . . . . . . . . . . . . . . . 294
8.2 Alternating sums . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 314
8.E Chapter 8 exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . 330
9 Real numbers 333
9.1 Inequalities and means . . . . . . . . . . . . . . . . . . . . . . . . . . 334
9.2 Completeness and convergence . . . . . . . . . . . . . . . . . . . . . . 353
9.3 Series and sums . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 378
9.E Chapter 9 exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . 401
10 Infinity 405
10.1 Cardinality . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 406
10.2 Cardinal arithmetic . . . . . . . . . . . . . . . . . . . . . . . . . . . . 415
10.E Chapter 10 exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . 427
11 Discrete probability theory 431
11.1 Discrete probability spaces . . . . . . . . . . . . . . . . . . . . . . . . 432
11.2 Discrete random variables . . . . . . . . . . . . . . . . . . . . . . . . 451
11.E Chapter 11 exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . 468
12 Additional topics 469
12.1 Orders and lattices . . . . . . . . . . . . . . . . . . . . . . . . . . . . 470
vii
viii Contents
12.2 Inductively defined sets . . . . . . . . . . . . . . . . . . . . . . . . . . 482
12.E Chapter 12 exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . 504
""",
        "url": "https://infinitedescent.xyz/dl/infdesc.pdf",
        "page_buffer": 18
    },
    "ECE 1150":{
        "content":"""
PREFACE xix
1 INTRODUCTION 1
1.1 USES OF COMPUTER NETWORKS, 3
1.1.1 Business Applications, 3
1.1.2 Home Applications, 6
1.1.3 Mobile Users, 10
1.1.4 Social Issues, 14
1.2 NETWORK HARDWARE, 17
1.2.1 Personal Area Networks, 18
1.2.2 Local Area Networks, 19
1.2.3 Metropolitan Area Networks, 23
1.2.4 Wide Area Networks, 23
1.2.5 Internetworks, 28
1.3 NETWORK SOFTWARE, 29
1.3.1 Protocol Hierarchies, 29
1.3.2 Design Issues for the Layers, 33
1.3.3 Connection-Oriented Versus Connectionless Service, 35
1.3.4 Service Primitives, 38
1.3.5 The Relationship of Services to Protocols, 40
1.4 REFERENCE MODELS, 41
1.4.1 The OSI Reference Model, 41
1.4.2 The TCP/IP Reference Model, 45
1.4.3 The Model Used in This Book, 48
1.4.4 A Comparison of the OSI and TCP/IP Reference Models*, 49
1.4.5 A Critique of the OSI Model and Protocols*, 51
1.4.6 A Critique of the TCP/IP Reference Model*, 53
1.5 EXAMPLE NETWORKS, 54
1.5.1 The Internet, 54
1.5.2 Third-Generation Mobile Phone Networks*, 65
1.5.3 Wireless LANs: 802.11*, 70
1.5.4 RFID and Sensor Networks*, 73
1.6 NETWORK STANDARDIZATION*, 75
1.6.1 Who’s Who in the Telecommunications World, 77
1.6.2 Who’s Who in the International Standards World, 78
1.6.3 Who’s Who in the Internet Standards World, 80
1.7 METRIC UNITS, 82
1.8 OUTLINE OF THE REST OF THE BOOK, 83
1.9 SUMMARY, 84
2 THE PHYSICAL LAYER 89
2.1 THE THEORETICAL BASIS FOR DATA COMMUNICATION, 90
2.1.1 Fourier Analysis, 90
2.1.2 Bandwidth-Limited Signals, 90
2.1.3 The Maximum Data Rate of a Channel, 94
2.2 GUIDED TRANSMISSION MEDIA, 95
2.2.1 Magnetic Media, 95
2.2.2 Twisted Pairs, 96
2.2.3 Coaxial Cable, 97
2.2.4 Power Lines, 98
2.2.5 Fiber Optics, 99
2.3 WIRELESS TRANSMISSION, 105
2.3.1 The Electromagnetic Spectrum, 105
2.3.2 Radio Transmission, 109
2.3.3 Microwave Transmission, 110
2.3.4 Infrared Transmission, 114
2.3.5 Light Transmission, 114
2.4 COMMUNICATION SATELLITES*, 116
2.4.1 Geostationary Satellites, 117
2.4.2 Medium-Earth Orbit Satellites, 121
2.4.3 Low-Earth Orbit Satellites, 121
2.4.4 Satellites Versus Fiber, 123
2.5 DIGITAL MODULATION AND MULTIPLEXING, 125
2.5.1 Baseband Transmission, 125
2.5.2 Passband Transmission, 130
2.5.3 Frequency Division Multiplexing, 132
2.5.4 Time Division Multiplexing, 135
2.5.5 Code Division Multiplexing, 135
2.6 THE PUBLIC SWITCHED TELEPHONE NETWORK, 138
2.6.1 Structure of the Telephone System, 139
2.6.2 The Politics of Telephones, 142
2.6.3 The Local Loop: Modems, ADSL, and Fiber, 144
2.6.4 Trunks and Multiplexing, 152
2.6.5 Switching, 161
2.7 THE MOBILE TELEPHONE SYSTEM*, 164
2.7.1 First-Generation (coco1G) Mobile Phones: Analog Voice, 166
2.7.2 Second-Generation (2G) Mobile Phones: Digital Voice, 170
2.7.3 Third-Generation (3G) Mobile Phones: Digital Voice and Data, 174
2.8 CABLE TELEVISION*, 179
2.8.1 Community Antenna Television, 179
2.8.2 Internet over Cable, 180
2.8.3 Spectrum Allocation, 182
2.8.4 Cable Modems, 183
2.8.5 ADSL Versus Cable, 185
2.9 SUMMARY, 186
3 THE DATA LINK LAYER 193
3.1 DATA LINK LAYER DESIGN ISSUES, 194
3.1.1 Services Provided to the Network Layer, 194
3.1.2 Framing, 197
3.1.3 Error Control, 200
3.1.4 Flow Control, 201
3.2 ERROR DETECTION AND CORRECTION, 202
3.2.1 Error-Correcting Codes, 204
3.2.2 Error-Detecting Codes, 209
3.3 ELEMENTARY DATA LINK PROTOCOLS, 215
3.3.1 A Utopian Simplex Protocol, 220
3.3.2 A Simplex Stop-and-Wait Protocol for an Error-Free Channel, 221
3.3.3 A Simplex Stop-and-Wait Protocol for a Noisy Channel, 222
3.4 SLIDING WINDOW PROTOCOLS, 226
3.4.1 A One-Bit Sliding Window Protocol, 229
3.4.2 A Protocol Using Go-Back-N, 232
3.4.3 A Protocol Using Selective Repeat, 239
3.5 EXAMPLE DATA LINK PROTOCOLS, 244
3.5.1 Packet over SONET, 245
3.5.2 ADSL (Asymmetric Digital Subscriber Loop), 248
3.6 SUMMARY, 251
4 THE MEDIUM ACCESS CONTROL SUBLAYER 257
4.1 THE CHANNEL ALLOCATION PROBLEM, 258
4.1.1 Static Channel Allocation, 258
4.1.2 Assumptions for Dynamic Channel Allocation, 260
4.2 MULTIPLE ACCESS PROTOCOLS, 261
4.2.1 ALOHA, 262
4.2.2 Carrier Sense Multiple Access Protocols, 266
4.2.3 Collision-Free Protocols, 269
4.2.4 Limited-Contention Protocols, 274
4.2.5 Wireless LAN Protocols, 277
4.3 ETHERNET, 280
4.3.1 Classic Ethernet Physical Layer, 281
4.3.2 Classic Ethernet MAC Sublayer Protocol, 282
4.3.3 Ethernet Performance, 286
4.3.4 Switched Ethernet, 288
4.3.5 Fast Ethernet, 290
4.3.6 Gigabit Ethernet, 293
4.3.7 10-Gigabit Ethernet, 296
4.3.8 Retrospective on Ethernet, 298
4.4 WIRELESS LANS, 299
4.4.1 The 802.11 Architecture and Protocol Stack, 299
4.4.2 The 802.11 Physical Layer, 301
4.4.3 The 802.11 MAC Sublayer Protocol, 303
4.4.4 The 802.11 Frame Structure, 309
4.4.5 Services, 311
4.5 BROADBAND WIRELESS*, 312
4.5.1 Comparison of 802.16 with 802.11 and 3G, 313
4.5.2 The 802.16 Architecture and Protocol Stack, 314
4.5.3 The 802.16 Physical Layer, 316
4.5.4 The 802.16 MAC Sublayer Protocol, 317
4.5.5 The 802.16 Frame Structure, 319
4.6 BLUETOOTH*, 320
4.6.1 Bluetooth Architecture, 320
4.6.2 Bluetooth Applications, 321
4.6.3 The Bluetooth Protocol Stack, 322
4.6.4 The Bluetooth Radio Layer, 324
4.6.5 The Bluetooth Link Layers, 324
4.6.6 The Bluetooth Frame Structure, 325
4.7 RFID*, 327
4.7.1 EPC Gen 2 Architecture, 327
4.7.2 EPC Gen 2 Physical Layer, 328
4.7.3 EPC Gen 2 Tag Identification Layer, 329
4.7.4 Tag Identification Message Formats, 331
4.8 DATA LINK LAYER SWITCHING, 332
4.8.1 Uses of Bridges, 332
4.8.2 Learning Bridges, 334
4.8.3 Spanning Tree Bridges, 337
4.8.4 Repeaters, Hubs, Bridges, Switches, Routers, and Gateways, 340
4.8.5 Virtual LANs, 342
4.9 SUMMARY, 349
5 THE NETWORK LAYER 355
5.1 NETWORK LAYER DESIGN ISSUES, 355
5.1.1 Store-and-Forward Packet Switching, 356
5.1.2 Services Provided to the Transport Layer, 356
5.1.3 Implementation of Connectionless Service, 358
5.1.4 Implementation of Connection-Oriented Service, 359
5.1.5 Comparison of Virtual-Circuit and Datagram Networks, 361
5.2 ROUTING ALGORITHMS, 362
5.2.1 The Optimality Principle, 364
5.2.2 Shortest Path Algorithm, 366
5.2.3 Flooding, 368
5.2.4 Distance Vector Routing, 370
5.2.5 Link State Routing, 373
5.2.6 Hierarchical Routing, 378
5.2.7 Broadcast Routing, 380
5.2.8 Multicast Routing, 382
5.2.9 Anycast Routing, 385
5.2.10 Routing for Mobile Hosts, 386
5.2.11 Routing in Ad Hoc Networks, 389
5.3 CONGESTION CONTROL ALGORITHMS, 392
5.3.1 Approaches to Congestion Control, 394
5.3.2 Traffic-Aware Routing, 395
5.3.3 Admission Control, 397
5.3.4 Traffic Throttling, 398
5.3.5 Load Shedding, 401
5.4 QUALITY OF SERVICE, 404
5.4.1 Application Requirements, 405
5.4.2 Traffic Shaping, 407
5.4.3 Packet Scheduling, 411
5.4.4 Admission Control, 415
5.4.5 Integrated Services, 418
5.4.6 Differentiated Services, 421
5.5 INTERNETWORKING, 424
5.5.1 How Networks Differ, 425
5.5.2 How Networks Can Be Connected, 426
5.5.3 Tunneling, 429
5.5.4 Internetwork Routing, 431
5.5.5 Packet Fragmentation, 432
5.6 THE NETWORK LAYER IN THE INTERNET, 436
5.6.1 The IP Version 4 Protocol, 439
5.6.2 IP Addresses, 442
5.6.3 IP Version 6, 455
5.6.4 Internet Control Protocols, 465
5.6.5 Label Switching and MPLS, 470
5.6.6 OSPF—An Interior Gateway Routing Protocol, 474
5.6.7 BGP—The Exterior Gateway Routing Protocol, 479
5.6.8 Internet Multicasting, 484
5.6.9 Mobile IP, 485
5.7 SUMMARY, 488
6 THE TRANSPORT LAYER 495
6.1 THE TRANSPORT SERVICE, 495
6.1.1 Services Provided to the Upper Layers, 496
6.1.2 Transport Service Primitives, 498
6.1.3 Berkeley Sockets, 500
6.1.4 An Example of Socket Programming: An Internet File Server, 503
6.2 ELEMENTS OF TRANSPORT PROTOCOLS, 507
6.2.1 Addressing, 509
6.2.2 Connection Establishment, 512
6.2.3 Connection Release, 517
6.2.4 Error Control and Flow Control, 522
6.2.5 Multiplexing, 527
6.2.6 Crash Recovery, 527
6.3 CONGESTION CONTROL, 530
6.3.1 Desirable Bandwidth Allocation, 531
6.3.2 Regulating the Sending Rate, 535
6.3.3 Wireless Issues, 539
6.4 THE INTERNET TRANSPORT PROTOCOLS: UDP, 541
6.4.1 Introduction to UDP, 541
6.4.2 Remote Procedure Call, 543
6.4.3 Real-Time Transport Protocols, 546
6.5 THE INTERNET TRANSPORT PROTOCOLS: TCP, 552
6.5.1 Introduction to TCP, 552
6.5.2 The TCP Service Model, 553
6.5.3 The TCP Protocol, 556
6.5.4 The TCP Segment Header, 557
6.5.5 TCP Connection Establishment, 560
6.5.6 TCP Connection Release, 562
6.5.7 TCP Connection Management Modeling, 562
6.5.8 TCP Sliding Window, 565
6.5.9 TCP Timer Management, 568
6.5.10 TCP Congestion Control, 571
6.5.11 The Future of TCP, 581
6.6 PERFORMANCE ISSUES*, 582
6.6.1 Performance Problems in Computer Networks, 583
6.6.2 Network Performance Measurement, 584
6.6.3 Host Design for Fast Networks, 586
6.6.4 Fast Segment Processing, 590
6.6.5 Header Compression, 593
6.6.6 Protocols for Long Fat Networks, 595
6.7 DELAY-TOLERANT NETWORKING*, 599
6.7.1 DTN Architecture, 600
6.7.2 The Bundle Protocol, 603
6.8 SUMMARY, 605
7 THE APPLICATION LAYER 611
7.1 DNS—THE DOMAIN NAME SYSTEM, 611
7.1.1 The DNS Name Space, 612
7.1.2 Domain Resource Records, 616
7.1.3 Name Servers, 619
7.2 ELECTRONIC MAIL*, 623
7.2.1 Architecture and Services, 624
7.2.2 The User Agent, 626
7.2.3 Message Formats, 630
7.2.4 Message Transfer, 637
7.2.5 Final Delivery, 643
7.3 THE WORLD WIDE WEB, 646
7.3.1 Architectural Overview, 647
7.3.2 Static Web Pages, 662
7.3.3 Dynamic Web Pages and Web Applications, 672
7.3.4 HTTP—The HyperText Transfer Protocol, 683
7.3.5 The Mobile Web, 693
7.3.6 Web Search, 695
7.4 STREAMING AUDIO AND VIDEO, 697
7.4.1 Digital Audio, 699
7.4.2 Digital Video, 704
7.4.3 Streaming Stored Media, 713
7.4.4 Streaming Live Media, 721
7.4.5 Real-Time Conferencing, 724
7.5 CONTENT DELIVERY, 734
7.5.1 Content and Internet Traffic, 736
7.5.2 Server Farms and Web Proxies, 738
7.5.3 Content Delivery Networks, 743
7.5.4 Peer-to-Peer Networks, 748
7.6 SUMMARY, 757
8 NETWORK SECURITY 763
8.1 CRYPTOGRAPHY, 766
8.1.1 Introduction to Cryptography, 767
8.1.2 Substitution Ciphers, 769
8.1.3 Transposition Ciphers, 771
8.1.4 One-Time Pads, 772
8.1.5 Two Fundamental Cryptographic Principles, 776
8.2 SYMMETRIC-KEY ALGORITHMS, 778
8.2.1 DES—The Data Encryption Standard, 780
8.2.2 AES—The Advanced Encryption Standard, 783
8.2.3 Cipher Modes, 787
8.2.4 Other Ciphers, 792
8.2.5 Cryptanalysis, 792
8.3 PUBLIC-KEY ALGORITHMS, 793
8.3.1 RSA, 794
8.3.2 Other Public-Key Algorithms, 796
8.4 DIGITAL SIGNATURES, 797
8.4.1 Symmetric-Key Signatures, 798
8.4.2 Public-Key Signatures, 799
8.4.3 Message Digests, 800
8.4.4 The Birthday Attack, 804
8.5 MANAGEMENT OF PUBLIC KEYS, 806
8.5.1 Certificates, 807
8.5.2 X.509, 809
8.5.3 Public Key Infrastructures, 810
8.6 COMMUNICATION SECURITY, 813
8.6.1 IPsec, 814
8.6.2 Firewalls, 818
8.6.3 Virtual Private Networks, 821
8.6.4 Wireless Security, 822
8.7 AUTHENTICATION PROTOCOLS, 827
8.7.1 Authentication Based on a Shared Secret Key, 828
8.7.2 Establishing a Shared Key: The Diffie-Hellman Key Exchange, 833
8.7.3 Authentication Using a Key Distribution Center, 835
8.7.4 Authentication Using Kerberos, 838
8.7.5 Authentication Using Public-Key Cryptography, 840
8.8 EMAIL SECURITY*, 841
8.8.1 PGP—Pretty Good Privacy, 842
8.8.2 S/MIME, 846
8.9 WEB SECURITY, 846
8.9.1 Threats, 847
8.9.2 Secure Naming, 848
8.9.3 SSL—The Secure Sockets Layer, 853
8.9.4 Mobile Code Security, 857
8.10 SOCIAL ISSUES, 860
8.10.1 Privacy, 860
8.10.2 Freedom of Speech, 863
8.10.3 Copyright, 867
8.11 SUMMARY, 869
9 READING LIST AND BIBLIOGRAPHY 877
9.1 SUGGESTIONS FOR FURTHER READING*, 877
9.1.1 Introduction and General Works, 878
9.1.2 The Physical Layer, 879
9.1.3 The Data Link Layer, 880
9.1.4 The Medium Access Control Sublayer, 880
9.1.5 The Network Layer, 881
9.1.6 The Transport Layer, 882
9.1.7 The Application Layer, 882
9.1.8 Network Security, 883
9.2 ALPHABETICAL BIBLIOGRAPHY*, 884
INDEX 905
""", "url":"https://csc-knu.github.io/sys-prog/books/Andrew%20S.%20Tanenbaum%20-%20Computer%20Networks.pdf", "page_buffer":24
    },
    "REHSCI 1219":{
        "content": """
        1 Structure and Function of Exercising Muscle 27
Functional Anatomy of Skeletal Muscle 29
Skeletal Muscle and Exercise 37
2 Fuel for Exercise: Bioenergetics
and Muscle Metabolism 49
Energy Substrates 50
Controlling the Rate of Energy Production 52
Storing Energy: High-Energy Phosphates 54
The Basic Energy Systems 55
Interaction Among the Energy Systems 64
The Oxidative Capacity of Muscle 64
3 Neural Control of Exercising Muscle 69
Structure and Function of the Nervous System 70
Central Nervous System 78
Peripheral Nervous System 80
Sensory-Motor Integration 83
4 Hormonal Control During Exercise 91
The Endocrine System 92
Hormones 93
Endocrine Glands and Their Hormones: An Overview 96
Hormonal Regulation of Metabolism During Exercise 100
Hormonal Regulation of Fluid and Electrolytes During Exercise 104
5 Energy Expenditure and Fatigue 113
Measuring Energy Expenditure 114
Energy Expenditure at Rest and During Exercise 120
Fatigue and Its Causes 128
6 The Cardiovascular System and Its Control 139
Heart 140
Vascular System 152
Blood 157
7 The Respiratory System and Its Regulation 163
Pulmonary Ventilation 164
Pulmonary Volumes 166
Pulmonary Diffusion 167
Transport of Oxygen and Carbon Dioxide in the Blood 172
Gas Exchange at the Muscles 175
Regulation of Pulmonary Ventilation 177
8 Cardiorespiratory Responses to Acute Exercise 181
Cardiovascular Responses to Acute Exercise 182
Respiratory Responses to Acute Exercise 196
9 Principles of Exercise Training 209
Terminology 210
General Principles of Training 212
Resistance Training Programs 214
Anaerobic and Aerobic Power Training Programs 220
10 Adaptations to Resistance Training 227
Resistance Training and Gains in Muscular Fitness 228
Mechanisms of Gains in Muscle Strength 228
Muscle Soreness and Cramps 237
Resistance Training for Special Populations 242
11 Adaptations to Aerobic and Anaerobic Training 247
Adaptations to Aerobic Training 248
Adaptations to Anaerobic Training 272
Specificity of Training and Cross-Training 275
12 Exercise in Hot and Cold Environments 283
Body Temperature Regulation 284
Physiological Responses to Exercise in the Heat 291
Health Risks During Exercise in the Heat 294
Acclimation to Exercise in the Heat 299
Exercise in the Cold 301
Physiological Responses to Exercise in the Cold 304
Health Risks During Exercise in the Cold 305
13 Exercise at Altitude 309
Environmental Conditions at Altitude 310
Physiological Responses to Acute Altitude Exposure 313
Exercise and Sport Performance at Altitude 317
Acclimation: Chronic Exposure to Altitude 319
Altitude: Optimizing Training and Performance 322
Health Risks of Acute Exposure to Altitude 325
14 Training for Sport 333
Optimizing Training: A Model 334
Overtraining 338
Tapering for Peak Performance 345
Detraining 346
15 Body Composition and Nutrition for Sport 355
Body Composition in Sport 356
Nutrition and Sport 367
16 Ergogenic Aids and Sport 395
Researching Ergogenic Aids 397
Pharmacological Agents 399
Hormonal Agents 405
Physiological Agents 411
Nutritional Agents 417
17 Children and Adolescents in Sport and Exercise 425
Growth, Development, and Maturation 426
Physiological Responses to Acute Exercise 430
Physiological Adaptations to Exercise Training 437
Motor Ability and Sport Performance 440
Special Issues 440
18 Aging in Sport and Exercise 447
Height, Weight, and Body Composition 449
Physiological Responses to Acute Exercise 452
Physiological Adaptations to Exercise Training 461
Sport Performance 463
Special Issues 465
19 Sex Differences in Sport and Exercise 471
Body Size and Composition 473
Physiological Responses to Acute Exercise 474
Physiological Adaptations to Exercise Training 480
Sport Performance 482
Special Issues 482
20 Prescription of Exercise for Health and Fitness 499
Health Benefits of Exercise: The Great Awakening 500
Medical Clearance 501
Exercise Prescription 508
Monitoring Exercise Intensity 510
Exercise Program 516
Exercise and Rehabilitation of People With Diseases 518
21 Cardiovascular Disease and Physical Activity 521
Forms of Cardiovascular Disease 523
Understanding the Disease Process 527
Determining Individual Risk 530
Reducing Risk Through Physical Activity 533
Risk of Heart Attack and Death During Exercise 538
Exercise Training and Rehabilitating Patients With Heart Disease 539
22 Obesity, Diabetes, and Physical Activity 545
Obesity 546
Diabetes 565
Glossary 573
References 591
Index 608
About the Authors 620
""",
"url":"https://www.mdthinducollege.org/ebooks/exercise_Physiology/Physiology_of_Sport_and_Exercise_5th_Edition.pdf",
"page_buffer": 20
    },
    "MSE 2111": {
"content":"""
Preface ............................................................ v
1 Introduction . ........................................... v
2 Applications of Electrochemical Energy Storage . . . . . . . . . . . . . . vi
3 Changes That Have Taken Place in Recent Years. . . . . . . . . . . . . . ix
4 Objectives of This Book . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . x
5 Thinking Tools . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . xi
6 Terminology and Conventions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . xii
1 Introductory Material ........................................... 1
1.1 Introduction . ........................................... 1
1.2 Simple Chemical and Electrochemical Reactions . . . .......... 1
1.3 Major Types of Reaction Mechanisms . ..................... 6
1.3.1 Reconstitution Reactions . . . ..................... 6
1.3.2 Insertion Reactions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
1.4 Important Practical Parameters . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
1.4.1 The Operating Voltage and the Concept
of Energy Quality . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
1.4.2 The Charge Capacity . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
1.4.3 The Maximum Theoretical Specific Energy (MTSE) . 13
1.4.4 Variation of the Voltage as Batteries are Discharged
and Recharged . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
1.4.5 Cycling Behavior . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
1.4.6 Self-Discharge . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
1.5 General Equivalent Circuit of an Electrochemical Cell . . . . . . . . . 17
1.5.1 Influence of Impedances to the Transport of Ionic
and Atomic Species within the Cell . . . . . . . . . . . . . . . 18
1.5.2 Influence of Electronic Leakage within
the Electrolyte . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
1.5.3 Transference Numbers of Individual Species
in an Electrochemical Cell . . . . . . . . . . . . . . . . . . . . . . . 19
1.5.4 Relation between the Output Voltage and the Values
of the Ionic and Electronic Transference Numbers . . . 20
1.5.5 Joule Heating to Due to Self-Discharge
in Electrochemical Cells . . . . . . . . . . . . . . . . . . . . . . . . 21
1.5.6 What If Current is Drawn from the Cell? . . . . . . . . . . . 21
References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
2 Principles Determining the Voltages and Capacities
of Electrochemical Cells . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
2.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
2.2 Thermodynamic Properties of Individual Species . . . . . . . . . . . . . 25
2.3 A Simple Example: The Lithium/Iodine Cell . . . . . . . . . . . . . . . . . 27
2.3.1 Calculation of the Maximum Theoretical
Specific Energy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
2.3.2 The Temperature Dependence of the Cell Voltage . . . 29
2.4 The Shape of Discharge Curves and the Gibbs Phase Rule . . . . . . 30
2.5 The Coulometric Titration Technique . . . . . . . . . . . . . . . . . . . . . . . 36
References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
3 Binary Electrodes Under Equilibrium or Near-Equilibrium
Conditions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
3.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
3.2 Binary Phase Diagrams . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
3.2.1 The Lever Rule . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44
3.2.2 Examples of Binary Phase Diagrams . . . . . . . . . . . . . . 44
3.3 A Real Example, The Lithium: Antimony System Again . . . . . . . 46
3.4 Stability Ranges of Phases . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51
3.5 Another Example, The Lithium: Bismuth System . . . . . . . . . . . . . 51
3.6 Coulometric Titration Measurements on Other Binary Systems. . 53
3.7 Temperature Dependence of the Potential . . . . . . . . . . . . . . . . . . . . 53
3.8 Application to Oxides and Similar Materials . . . . . . . . . . . . . . . . . 55
3.9 Ellingham Diagrams . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56
3.10 Liquid Binary Electrodes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57
3.11 Comments on Mechanisms and Terminology . . . . . . . . . . . . . . . . . 60
3.12 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 62
References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 62
4 Ternary Electrodes Under Equilibrium or Near-Equilibrium
Conditions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65
4.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65
4.2 Ternary Phase Diagrams and Phase Stability Diagrams . . . . . . . . 65
4.3 Comments on the Influence of SubTriangle Configurations
in Ternary Systems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67
4.4 An Example: The Sodium/Nickel Chloride “Zebra” System . . . . 70
4.5 A Second Example: The Lithium–Copper–Chlorine Ternary
System . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 72
4.5.1 Calculation of the Voltages in This System . . . . . . . . . 74
4.5.2 Experimental Arrangement for Lithium/Copper
Chloride Cells . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 77
4.6 Calculation of the Maximum Theoretical Specific Energies
of Li/Cucl and Li/CuCl2 Cells . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 77
4.7 Specific Capacity and Capacity Density in Ternary Systems . . . . 78
4.8 Another Group of Examples: Metal Hydride Systems
Containing Magnesium . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 78
4.9 Further Ternary Examples: Lithium–Transition
Metal Oxides . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 85
4.10 Ternary Systems Composed of Two Binary Metal Alloys . . . . . . . 90
4.10.1 An Example: The Li–Cd–Sn System at Ambient
Temperature . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 90
4.11 What About the Presence of Additional Components? . . . . . . . . . 91
4.12 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 91
References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 91
5 Electrode Reactions That Deviate From Complete Equilibrium . . . . . . 93
5.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 93
5.2 Stable and Metastable Equilibrium . . . . . . . . . . . . . . . . . . . . . . . . . 93
5.3 Selective Equilibrium . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 95
5.4 Soft Chemistry (Chimie Douce) . . . . . . . . . . . . . . . . . . . . . . . . . . . . 96
5.5 Formation of Amorphous vs. Crystalline Structures . . . . . . . . . . . 96
5.6 The Conversion of Crystalline to Amorphous Structures
by Insertion Reactions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 98
5.7 Deviations from Equilibrium for Kinetic Reasons . . . . . . . . . . . . . 98
References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 99
6 Insertion Reaction Electrodes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 101
6.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 101
6.2 Examples of the Insertion of Guest Species
into Layer Structures . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103
6.3 Floating and Pillared Layer Structures . . . . . . . . . . . . . . . . . . . . . . 104
6.4 More on Terminology Related to the Insertion of Species
into Solids . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 104
6.5 Types of Inserted Guest Species Configurations . . . . . . . . . . . . . . 105
6.6 Sequential Insertion Reactions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107
6.7 Coinsertion of Solvent Species . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 110
6.8 Insertion into Materials with Parallel Linear Tunnels . . . . . . . . . . 110
6.9 Changes in the Host Structure Induced by Guest Insertion
or Extraction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 111
6.9.1 Conversion of the Host Structure from Crystalline
to Amorphous . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 111
6.9.2 Dependence of the Product upon the Potential . . . . . . 113
6.9.3 Changes upon the Initial Extraction of the Mobile
Species . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 114
6.10 The Variation of the Potential with Composition in Insertion
Reaction Electrodes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 114
6.10.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 114
6.10.2 The Variation of the Electrical Potential
with Composition in Simple Metallic Solid
Solutions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 116
6.10.3 Configurational Entropy of the Guest Ions. . . . . . . . . . 116
6.10.4 The Concentration Dependence of the Chemical
Potential of the Electrons in a Metallic Solid
Solution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 117
6.10.5 Sum of the Effect of These Two Components
upon the Electrical Potential of a Metallic
Solid Solution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 118
6.10.6 The Composition: Dependence of the Potential
in the Case of Insertion Reactions that Involve
a Two-Phase Reconstitution Reaction . . . . . . . . . . . . . 119
6.11 Final Comments . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 122
References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 122
7 Negative Electrodes in Lithium Cells. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 123
7.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 123
7.2 Elemental Lithium Electrodes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 123
7.3 Problems with the Rechargeability of Elemental Electrodes . . . . . 124
7.3.1 Deposition at Unwanted Locations . . . . . . . . . . . . . . . . 124
7.3.2 Shape Change . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 124
7.3.3 Dendrites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 125
7.3.4 Filamentary Growth . . . . . . . . . . . . . . . . . . . . . . . . . . . . 125
7.3.5 Thermal Runaway . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 126
7.4 Alternatives . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 127
7A Lithium–Carbon Alloys . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 127
7A.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 127
7A.2 Ideal Structure of Graphite Saturated with Lithium . . . . . . . . . . . . 129
7A.3 Variations in the Structure of Graphite . . . . . . . . . . . . . . . . . . . . . . 130
7A.4 Structural Aspects of Lithium Insertion
into Graphitic Carbons . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 131
7A.5 Electrochemical Behavior of Lithium in Graphite . . . . . . . . . . . . . 132
7A.6 Electrochemical Behavior of Lithium
in Amorphous Graphite . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 134
7A.7 Lithium in Hydrogen-Containing Carbons . . . . . . . . . . . . . . . . . . . 134
7B Metallic Lithium Alloys . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 136
7B.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 136
7B.2 Equilibrium Thermodynamic Properties of Binary
Lithium Alloys . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 136
7B.3 Experiments at Ambient Temperature . . . . . . . . . . . . . . . . . . . . . . 137
7B.4 Liquid Binary Alloys . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 138
7B.5 Mixed-Conductor Matrix Electrodes . . . . . . . . . . . . . . . . . . . . . . . 138
7B.6 Decrepitation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 143
7B.7 Modification of the Micro and Nanostructure
of the Electrode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 145
7B.8 Formation of Amorphous Products at Ambient Temperatures . . 147
References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 148
8 Convertible Reactant Electrodes. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 151
8.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 151
8.2 Electrochemical Formation of Metals and Alloys from Oxides . 152
8.3 Lithium–Tin Alloys at Ambient Temperature . . . . . . . . . . . . . . . . 152
8.4 The Lithium–Tin Oxide System . . . . . . . . . . . . . . . . . . . . . . . . . . . 153
8.5 Irreversible and Reversible Capacities . . . . . . . . . . . . . . . . . . . . . . 155
8.6 Other Possible Convertible Oxides . . . . . . . . . . . . . . . . . . . . . . . . 157
8.7 Final Comments . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 158
References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 158
9 Positive Electrodes in Lithium Systems . . . . . . . . . . . . . . . . . . . . . . . . . . . 159
9.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 159
9.2 Insertion Reaction, Instead of Reconstitution Reaction,
Electrodes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 160
9.3 More than One Type of Interstitial Site or More than
One Type of Redox Species . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 161
9.4 Cells Assembled in the Discharged State . . . . . . . . . . . . . . . . . . . 162
9A Solid Positive Electrodes in Lithium Systems. . . . . . . . . . . . . . . . . . . . . . 163
9A.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 163
9A.2 Influence of the Crystallographic Environment on the Potential . 166
9A.3 Oxides with Structures in Which the Oxygen Anions
Are in a Face-Centered Cubic Array . . . . . . . . . . . . . . . . . . . . . . . 167
9A.3.1 Materials with Layered Structures . . . . . . . . . . . . . . . . 167
9A.3.2 Materials with the Spinel Structure . . . . . . . . . . . . . . . . 169
9A.3.3 Lower Potential Spinel Materials with
Reconstitution Reactions . . . . . . . . . . . . . . . . . . . . . . . . 174
9A.4 Materials in Which the Oxide Ions Are
in a Close-Packed Hexagonal Array . . . . . . . . . . . . . . . . . . . . . . . 175
9A.4.1 The Nasicon Structure . . . . . . . . . . . . . . . . . . . . . . . . . . 175
9A.4.2 Materials with the Olivine Structure . . . . . . . . . . . . . . . 177
9A.5 Materials Containing Fluoride Ions . . . . . . . . . . . . . . . . . . . . . . . . 179
9A.6 Hybrid Ion Cells . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 180
9A.7 Amorphization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 180
9A.8 The Oxygen Evolution Problem . . . . . . . . . . . . . . . . . . . . . . . . . . . 180
9A.9 Closing Comments . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 186
9B Liquid Positive Electrode Reactants. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 186
9B.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 186
9B.2 The Li/SO2 System . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 186
9B.3 The Li/SOCl2 System . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 188
9C Hydrogen and Water in Positive Electrode Materials . . . . . . . . . . . . . . 188
9C.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 188
9C.2 Ion Exchange . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 189
9C.3 Simple Addition Methods . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 190
9C.4 Thermodynamics of the Lithium–Hydrogen–Oxygen System . . 190
9C.5 Examples of Phases Containing Lithium That are Stable
in Water . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 191
9C.6 Materials That Have Potentials Above the Stability
Window of Water . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 192
9C.7 Absorption of Protons from Water Vapor in the Atmosphere . . . 192
9C.8 Extraction of Lithium from Aqueous Solutions . . . . . . . . . . . . . . 193
References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 193
10 Negative Electrodes in Aqueous Systems . . . . . . . . . . . . . . . . . . . . . . . . . 197
10.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 197
10A The Zinc Electrode in Aqueous Systems . . . . . . . . . . . . . . . . . . . . . . . . . . 197
10A.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 197
10A.2 Thermodynamic Relationships in the H−Zn−O System . . . . . . 198
10A.3 Problems with the Zinc Electrode . . . . . . . . . . . . . . . . . . . . . . . . . 199
10B The “Cadmium” Electrode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 199
10B.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 199
10B.2 Thermodynamic Relationships in the H−Cd−O System . . . . . . 200
10B.3 Comments on the Mechanism of Operation
of the Cadmium Electrode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 201
10C Metal Hydride Electrodes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 202
10C.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 202
10C.2 Comments on the Development of Commercial Metal
Hydride Electrode Batteries . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 203
10C.3 Hydride Materials Currently Being Used . . . . . . . . . . . . . . . . . . . 203
10C.4 Disproportionation and Activation . . . . . . . . . . . . . . . . . . . . . . . . . 204
10C.5 Pressure–Composition Relation . . . . . . . . . . . . . . . . . . . . . . . . . . . 205
10C.6 The Influence of Temperature . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 206
10C.7 AB2 Alloys . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 208
10C.8 General Comparison of These Two Structural Types . . . . . . . . . . 209
10C.9 Other Alloys That Have Not Been Used in Commercial
Batteries . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 210
10C.10 Microencapsulation of Hydride Particles . . . . . . . . . . . . . . . . . . . 210
10C.11 Other Binders . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 211
10C.12 Inclusion of a Solid Electrolyte in the Negative Electrode
of Hydride Cells . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 211
10C.13 Maximum Theoretical Capacities of Various
Metal Hydrides . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 211
References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 212
11 Positive Electrodes in Aqueous Systems . . . . . . . . . . . . . . . . . . . . . . . . . . 213
11.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 213
11A Manganese Dioxide Electrodes in Aqueous Systems. . . . . . . . . . . . . . . . 214
11A.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 214
11A.2 The Open Circuit Potential . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 215
11A.3 Variation of the Potential During Discharge . . . . . . . . . . . . . . . . . 216
11B The “Nickel” Electrode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 216
11B.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 216
11B.2 Structural Aspects of the Ni(OH)2 and NiOOH Phases . . . . . . . 217
11B.3 Mechanism of Operation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 218
11B.4 Relations Between Electrochemical and Structural Features . . . 220
11B.5 Self-discharge . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 221
11B.6 Overcharge . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 223
11B.7 Relation to Thermodynamic Information . . . . . . . . . . . . . . . . . . . 223
11C Cause of the Memory Effect in “Nickel” Electrodes . . . . . . . . . . . . . . . . 226
11C.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 226
11C.2 Mechanistic Features of the Operation of the “Nickel”
Electrode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 228
11C.3 Overcharging Phenomena . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 230
11C.4 Conclusions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 232
References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 233
12 Other Topics Related to Electrodes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 235
12.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 235
12A Mixed-Conducting Host Structures into Which Either Cations
or Anions Can Be Inserted . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 235
12A.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 235
12A.2 Insertion of Species into Materials with Transition Metal
Oxide Bronze Structures . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 236
12A.3 Materials with Cubic Structures Related to Rhenium Trioxide . . 237
12A.4 Hexacyanometallates . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 237
12A.5 Electrochemical Behavior of Prussian Blue . . . . . . . . . . . . . . . . . 241
12A.6 Various Cations Can Occupy the A Sites in the Prussian
Blue Structure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 244
12A.7 The Substitution of Other Species for the Fe3+ and the Fe2+
in the P and R Positions in the Prussian Blue Structure . . . . . . . . 245
12A.8 Other Materials with x = 2 That Have the Perovskite
Structure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 246
12A.9 The Electronic Properties of Members of the Prussian
Blue Family . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 246
12A.10 Batteries with Members of the Prussian Blue Family
on Both Sides . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 247
12A.11 Catalytic Behavior . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 247
12A.12 Electrochromic Behavior . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 248
12A.13 Insertion of Species into Graphite . . . . . . . . . . . . . . . . . . . . . . . . . 249
12A.14 Insertion of Guest Species into Polymers . . . . . . . . . . . . . . . . . . . 251
12A.15 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 252
12B Cells with Liquid Electrodes: Flow Batteries . . . . . . . . . . . . . . . . . . . . . . 252
12B.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 252
12B.2 Redox Reactions in the Vanadium/Vanadium System . . . . . . . . . 255
12B.3 Resultant Electrical Output . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 255
12B.4 Further Comments on the Vanadium/Vanadium Redox System . 255
12C Reactions in Fine Particle Electrodes. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 257
12C.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 257
12C.2 Translation of Two-Phase Interface by Chemical Diffusion . . . . 257
12C.3 Alternative Mechanism for the Translation of Poly-Phase
Interfaces. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 258
12C.4 Reactions in Electrodes Containing Many Small Particles . . . . . 260
12C.5 Mechanism Involved in Changing the Composition
of Lithium–Carbons . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 260
References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 261
13 Potentials . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 263
13.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 263
13A Potentials in and Near Solids . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 264
13A.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 264
13A.2 Potential Scales . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 265
13A.3 Electrical, Chemical, and Electrochemical Potentials in Metals . 265
13A.4 Relation to the Band Model of Electrons in Solids . . . . . . . . . . . 271
13A.5 Potentials in Semiconductors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 272
13A.6 Interactions Between Different Materials . . . . . . . . . . . . . . . . . . . 273
13A.7 Junctions Between Two Metals . . . . . . . . . . . . . . . . . . . . . . . . . . . 273
13A.8 Junctions Between Metals and Semiconductors . . . . . . . . . . . . . . 275
13A.9 Selective Equilibrium . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 276
13B Reference Electrodes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 276
13B.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 276
13B.2 Reference Electrodes in Nonaqueous Lithium Systems . . . . . . . . 277
13B.2.1 Use of Elemental Lithium . . . . . . . . . . . . . . . . . . . . . . . 277
13B.2.2 Use of Two-phase Lithium Alloys . . . . . . . . . . . . . . . . 277
13B.3 Reference Electrodes in Elevated Temperature
Oxide-Based Systems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 278
13B.3.1 Gas Electrodes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 278
13B.3.2 Polyphase Solid Reference Electrodes . . . . . . . . . . . . . 279
13B.3.3 Metal Hydride Systems . . . . . . . . . . . . . . . . . . . . . . . . . 280
13B.4 Relations Between Binary Potential Scales. . . . . . . . . . . . . . . . . . 280
13B.5 Potentials in the Ternary Lithium–Hydrogen–Oxygen System . . 280
13B.5.1 Lithium Cells in Aqueous Electrolytes . . . . . . . . . . . . . 282
13B.6 Significance of Electrically Neutral Species . . . . . . . . . . . . . . . . . 282
13B.7 Reference Electrodes in Aqueous Electrochemical Systems. . . . 283
13B.8 Historical Classification of Different Types
of Electrodes in Aqueous Systems . . . . . . . . . . . . . . . . . . . . . . . . . 284
13B.8.1 Electrodes of the First Kind . . . . . . . . . . . . . . . . . . . . . . 284
13B.8.2 Electrodes of the Second Kind . . . . . . . . . . . . . . . . . . . 285
13B.9 The Gibbs Phase Rule . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 287
13B.10 Application of the Gibbs Phase Rule to Reference Electrodes . . 288
13B.10.1 Nonaqueous Systems . . . . . . . . . . . . . . . . . . . . . . . . . . . 288
13B.10.2 Aqueous Systems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 288
13B.11 Systems Used to Measure the pH of Aqueous
Electrolytes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 291
13B.12 Electrodes with Mixed-Conducting Matrices . . . . . . . . . . . . . . . . 292
13B.13 Closing Comments . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 293
13C Potentials of Chemical Reactions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 293
13C.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 293
13C.2 Relation Between Chemical Redox Equilibria
and the Potential and Composition of Insertion
Reaction Materials . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 294
13C.3 Other Examples . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 295
13C.4 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 297
13D Potential and Composition Distributions Within Components
of Electrochemical Cells . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 297
13D.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 297
13D.2 Relevant Energy Quantities . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 297
13D.3 What Is Different About the Interior of Solids? . . . . . . . . . . . . . . 298
13D.4 Relations Between Inside and Outside Quantities . . . . . . . . . . . . 299
13D.5 Basic Flux Relations Inside Phases . . . . . . . . . . . . . . . . . . . . . . . . 299
13D.6 Two Simple Limiting Cases . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 300
13D.7 Three Configurations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 300
13D.8 Variation of the Composition with Potential . . . . . . . . . . . . . . . . . 300
13D.9 Calculation of the Concentrations of the Relevant Defects
in a Binary Solid MX That Is Predominantly an Ionic
Conductor . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 301
13D.10 Defect Equilibrium Diagrams. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 303
13D.11 Approximations Relevant in Specific Ranges of Composition
or Activity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 304
13D.12 Situation in Which an Electrical Potential Difference
Is Applied Across a Solid Electrolyte Using Electrodes
That Block the Entry and Exit of Ionic Species . . . . . . . . . . . . . . 305
13D.13 The Use of External Sensors to Evaluate Internal
Quantities in Solids . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 307
13D.14 Another Case, a Mixed Conductor in Which
the Transport of Electronic Species Is Blocked . . . . . . . . . . . . . . 308
13D.15 Further Comments on Composite Electrochemical
Cells Containing a Mixed Conductor in Series
with a Solid Electrolyte . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 309
13D.16 Transference Numbers of Particular Species . . . . . . . . . . . . . . . . . 311
References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 312
14 Liquid Electrolytes. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 315
14.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 315
14.2 General Considerations Regarding the Stability
of Electrolytes Vs. Alkali Metals . . . . . . . . . . . . . . . . . . . . . . . . . . 315
14A Elevated Temperature Electrolytes for Alkali Metals. . . . . . . . . . . . . . . 317
14A.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 317
14A.2 Lithium-Conducting Inorganic Molten Salts . . . . . . . . . . . . . . . . . 318
14A.3 Lower Temperature Alkali Halide Molten Salts . . . . . . . . . . . . . . 318
14A.4 Other Modest Temperature Molten (and Solid) Salts. . . . . . . . . . 318
14A.5 Relation Between the Potential and the Oxygen Pressure
in Lithium Systems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 319
14A.6 Implications for the Safety of Lithium Cells . . . . . . . . . . . . . . . . . 320
14B Ambient Temperature Electrolytes for Lithium . . . . . . . . . . . . . . . . . . . 321
14B.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 321
14B.2 Organic Solvent Liquid Electrolytes . . . . . . . . . . . . . . . . . . . . . . . 321
14B.3 Lithium Salts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 322
14B.4 Ionic Liquids . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 323
14C Aqueous Electrolytes for Hydrogen . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 324
14C.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 324
14C.2 Nafion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 325
14C.3 Other Considerations Relating to Nafion . . . . . . . . . . . . . . . . . . . . 327
14C.4 Alternatives to Nafion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 328
14D Nonaqueous Electrolytes for Hydrogen . . . . . . . . . . . . . . . . . . . . . . . . . . . 328
14D.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 328
14D.2 Methods Typically Used to Study Materials
for Hydrogen Storage . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 329
14D.3 Potential Advantages of Electrochemical Methods . . . . . . . . . . . 330
14D.4 The Amphoteric Behavior of Hydrogen . . . . . . . . . . . . . . . . . . . . 330
14D.5 Relationships Between the Potential and the Stability
of Phases in Molten Salts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 331
14D.6 Alkali Halide Molten Salts Containing Hydride Ions . . . . . . . . . 332
14D.7 Solution of Hydrogen in Vanadium . . . . . . . . . . . . . . . . . . . . . . . . 334
14D.8 The Titanium–Hydrogen System . . . . . . . . . . . . . . . . . . . . . . . . . . 334
14D.9 Use of Low Temperature Organic-Anion Molten Salt to Study
Hydrogen in Binary Magnesium Alloys . . . . . . . . . . . . . . . . . . . . 335
14D.10 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 336
References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 337
15 Solid Electrolytes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 339
15.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 339
15A Solid Electrolytes: Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 340
15A.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 340
15A.2 Structural Defects in Nonmetallic Solids . . . . . . . . . . . . . . . . . . . 341
15A.3 Various Types of Notation That May Be Used
to Describe Imperfections . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 343
15A.4 Types of Disorder . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 345
15B Mechanism and Structural Dependence of Ionic Conduction
in Solid Electrolytes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 347
15B.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 347
15B.2 Characteristic Properties . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 347
15B.3 Simple Hopping Model of Defect Transport . . . . . . . . . . . . . . . . . 350
15B.4 Interstitial Motion in Body-Centered Cubic Structures . . . . . . . . 352
15B.5 Rapid Ionic Motion in Other Crystal Structures . . . . . . . . . . . . . . 354
15B.6 Simple Structure-Dependent Model for the Rapid Transport
of Mobile Ions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 356
15B.7 Interstitial Motion in the Rutile Structure . . . . . . . . . . . . . . . . . . . 358
15B.8 Other Materials with Unidirectional Tunnels . . . . . . . . . . . . . . . . 361
15B.9 Materials with the Fluorite and Antifluorite Structures . . . . . . . . 362
15B.10 Materials with Layer Structures . . . . . . . . . . . . . . . . . . . . . . . . . . . 364
15B.11 Materials with Three-Dimensional Arrays of Tunnels . . . . . . . . . 367
15B.12 Structures with Isolated Tetrahedra . . . . . . . . . . . . . . . . . . . . . . . . 367
15C Lithium Ion Conductors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 368
15C.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 368
15C.2 Materials with the Perovskite Structure . . . . . . . . . . . . . . . . . . . . . 368
15C.3 Materials with the Garnet Structure . . . . . . . . . . . . . . . . . . . . . . . . 370
References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 371
16 Electrolyte Stability Windows and Their Extension . . . . . . . . . . . . . . . . 375
16.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 375
16.2 Binary Electrolyte Phases . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 376
16.3 Ternary Electrolyte Phases . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 377
16.3.1 Stability Limits Relative to Lithium . . . . . . . . . . . . . . . 378
16.3.2 Stability Limits Relative to Oxygen . . . . . . . . . . . . . . . 379
16.4 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 380
16A Composite Structures That Combine Stability Regimes . . . . . . . . . . . . 380
16A.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 380
16A.2 Two Solid Electrolytes in Series . . . . . . . . . . . . . . . . . . . . . . . . . . . 381
16A.3 Solid Electrolyte in Series with Aqueous Electrolyte . . . . . . . . . 381
16A.4 Solid Electrolyte in Series with Molten Salt . . . . . . . . . . . . . . . . . 382
16A.5 Formation of a Second Electrolyte by Topotactic Reaction
Between a Liquid and a Solid Mixed Conductor Electrode . . . . . 382
16A.6 Formation of a Protective Reaction Product Layer Between
the Negative Electrode and the Organic Solvent Electrolyte
in Lithium Cells . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 382
16B The SEI in Organic Solvent Systems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 383
16B.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 383
16B.2 Interaction of Organic Solvent Electrolytes with Graphite . . . . . 383
16B.3 Electrolyte Additives . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 387
16C Combination of a Solid Electrolyte and a Molten Salt Electrolyte . . . . 388
16C.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 388
16C.2 The Lithium–Nitrogen–Oxygen System . . . . . . . . . . . . . . . . . . . . 388
16C.3 Extension of the Effective Potential Range by the Formation
of a Second Electrolyte In Situ . . . . . . . . . . . . . . . . . . . . . . . . . . . . 389
16C.4 A Primary Lithium/Carbon Cell . . . . . . . . . . . . . . . . . . . . . . . . . . . 390
16C.5 Problems with This Concept . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 391
References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 391
17 Experimental Methods to Evaluate the Critical Properties
of Electrodes and Electrolytes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 393
17.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 393
17A Use of DC Methods to Determine the Electronic and Ionic
Components of the Conductivity in Mixed Conductors . . . . . . . . . . . . . 393
17A.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 393
17A.2 Transference Numbers of Individual Species . . . . . . . . . . . . . . . . 394
17A.3 The Tubandt Method . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 395
17A.4 The DC Assymetric Polarization Method . . . . . . . . . . . . . . . . . . . 395
17A.5 Interpretation of Hebb–Wagner Asymmetric Polarization
Measurements in Terms of a General Defect Equilibrium
Diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 396
17A.6 DC Open Circuit Potential Method . . . . . . . . . . . . . . . . . . . . . . . . 405
17B Experimental Determination of the Critical Properties of Potential
Electrode Materials . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 406
17B.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 406
17B.2 The GITT Method . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 408
17B.3 The PITT Method . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 408
17B.4 The FITT Method . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 409
17B.5 The WITT Method . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 411
17C Use of AC Methods to Determine the Electronic and Ionic
Components of the Conductivity in Solid Electrolytes
and Mixed Conductors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 414
17C.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 414
17C.2 Representation of the Properties of Simple Circuit Elements
on the Complex Impedance Plane . . . . . . . . . . . . . . . . . . . . . . . . . 416
17C.3 The Influence of Electronic Leakage Through an Ionic
Conductor . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 422
17C.4 Case in Which Both Ionic and Electronic Transport
Are Significant . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 423
17C.5 Influence of an Additional Impedance Due to Transverse
Internal Interfaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 425
17C.6 Behavior When There Is Internal Transverse Interface
Impedance as well as Partial Electronic Conduction . . . . . . . . . . 426
17C.7 An Example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 429
17C.8 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 430
References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 430
18 Use of Polymeric Materials As Battery Components . . . . . . . . . . . . . . . 433
18.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 433
18A Polymer Electrolytes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 434
18A.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 434
18A.2 High Molecular Weight Polymers Containing Salts . . . . . . . . . . . 434
18A.3 Particle-Enhanced Conductivity . . . . . . . . . . . . . . . . . . . . . . . . . . . 436
18A.4 Ionic Rubbers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 437
18A.5 Hybrid Electrolytes Containing an Ionically Conducting
Plasticizer . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 437
18A.6 Gel Electrolytes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 437
References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 439
19 Transient Behavior of Electrochemical Systems . . . . . . . . . . . . . . . . . . . 441
19.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 441
19A Transient Behavior Under Pulse Demand Conditions . . . . . . . . . . . . . . 442
19A.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 442
19A.2 Electrochemical Charge Storage Mechanisms . . . . . . . . . . . . . . . 445
19A.2.1 Electrostatic Energy Storage in the
Electrical Double Layer in the Vicinity of
the Electrolyte/Electrode Interface . . . . . . . . . . . . . . . . 445
19A.2.2 Underpotential Faradaic Two-Dimensional
Adsorption on the Surface of a Solid Electrode. . . . . . 447
19A.2.3 Faradaic Deposition That Results in the
Three-Dimensional Absorption of the Electroactive
Species into the Bulk Solid Electrode Material
by an Insertion Reaction . . . . . . . . . . . . . . . . . . . . . . . . 447
19A.2.4 Faradaically Driven Reconstitution Reactions . . . . . . . 450
19A.3 Comparative Magnitudes of Energy Storage . . . . . . . . . . . . . . . . . 450
19A.4 Importance of the Quality of the Stored Energy . . . . . . . . . . . . . . 452
19B Modeling Transient Behavior of Electrochemical Systems
Using Laplace Transforms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 453
19B.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 453
19B.2 Use of Laplace Transform Techniques . . . . . . . . . . . . . . . . . . . . . 453
19B.3 Simple Examples . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 455
References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 456
20 Closing Comments . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 459
20.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 459
20.2 Terminology . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 459
20.3 Major Attention Is Given to the Driving Forces
and Mechanisms That Determine the Potentials,
Kinetic Properties, and Capacities of Electrodes . . . . . . . . . . . . . 460
20.4 Thinking Tools . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 461
20.5 Major Players in This Area . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 461
20.6 The Future . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 462
Index . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 463
""", "url":"https://link.springer.com/content/pdf/10.1007/978-0-387-76424-5.pdf", "page_buffer":29},
    "CHEM 1480": {
"content":"""
1 Fundamental Concepts of Thermodynamics 1
2 Heat, Work, Internal Energy, Enthalpy, and the
First Law of Thermodynamics 17
3 The Importance of State Functions: Internal
Energy and Enthalpy 45
4 Thermochemistry 67
5 Entropy and the Second and Third Laws of
Thermodynamics 85
6 Chemical Equilibrium 125
7 The Properties of Real Gases 165
8 Phase Diagrams and the Relative Stability of
Solids, Liquids, and Gases 181
9 Ideal and Real Solutions 209
10 Electrolyte Solutions 243
11 Electrochemical Cells, Batteries, and Fuel
Cells 259
12 From Classical to Quantum Mechanics 293
13 The Schrödinger Equation 309
14 The Quantum Mechanical Postulates 331
15 Using Quantum Mechanics on Simple
Systems 343
16 The Particle in the Box and the Real
World 361
17 Commuting and Noncommuting Operators
and the Surprising Consequences of
Entanglement 383
18 A Quantum Mechanical Model for the
Vibration and Rotation of Molecules 405
19 The Vibrational and Rotational Spectroscopy
of Diatomic Molecules 431
20 The Hydrogen Atom 465
21 Many-Electron Atoms 483
22 Quantum States for Many-Electron Atoms and
Atomic Spectroscopy 507
23 The Chemical Bond in Diatomic
Molecules 537
24 Molecular Structure and Energy Levels for
Polyatomic Molecules 567
25 Electronic Spectroscopy 601
26 Computational Chemistry 631
27 Molecular Symmetry 687
28 Nuclear Magnetic Resonance
Spectroscopy 715
29 Probability 747
30 The Boltzmann Distribution 771
31 Ensemble and Molecular Partition
Functions 793
32 Statistical Thermodynamics 825
33 Kinetic Theory of Gases 857
34 Transport Phenomena 877
35 Elementary Chemical Kinetics 909
36 Complex Reaction Mechanisms 955
APPENDIX A Math Supplement 1007
APPENDIX B Data Tables 1029
APPENDIX C Point Group Character
Tables 1047
APPENDIX D Answers to Selected End-of-Chapter
Problems 1055
CREDITS 1071
INDEX 1073
""", "url":"https://students.aiu.edu/submissions/profiles/resources/onlineBook/r8y5Z7_Physical_Chemistry-_3.pdf", "page_buffer":23
},
    "PHYS 1361": {
"content": """1 A Brief History 9
1.1 Prolegomenon 9
1.2 In the Beginning 9
1.3 From the Seventeenth Century 10
1.4 The Nineteenth Century 12
1.5 Twentieth-Century Optics 15
2 Wave Motion 18
2.1 One-Dimensional Waves 18
2.2 Harmonic Waves 22
2.3 Phase and Phase Velocity 26
2.4 The Superposition Principle 28
2.5 The Complex Representation 30
2.6 Phasors and the Addition of Waves 31
2.7 Plane Waves 32
2.8 The Three-Dimensional Differential
Wave Equation 36
2.9 Spherical Waves 37
2.10 Cylindrical Waves 39
2.11 Twisted Light 39
 Problems 41
3 Electromagnetic Theory, Photons, and Light 45
3.1 Basic Laws of Electromagnetic Theory 46
3.2 Electromagnetic Waves 54
3.3 Energy and Momentum 57
3.4 Radiation 69
3.5 Light in Bulk Matter 76
3.6 The Electromagnetic-Photon Spectrum 83
3.7 Quantum Field Theory 90
 Problems 92
4 The Propagation of Light 96
4.1 Introduction 96
4.2 Rayleigh Scattering 96
4.3 Reflection 104
4.4 Refraction 108
4.5 Fermat’s Principle 117
4.6 The Electromagnetic Approach 121
4.7 Total Internal Reflection 133
4.8 Optical Properties of Metals 139
4.9 Familiar Aspects of the Interaction of Light
and Matter 142
4.10 The Stokes Treatment of Reflection and
Refraction 147
4.11 Photons, Waves, and Probability 148
 Problems 151
5 Geometrical Optics 159
5.1 Introductory Remarks 159
5.2 Lenses 159
5.3 Stops 183
5.4 Mirrors 188
5.5 Prisms 199
5.6 Fiberoptics 204
5.7 Optical Systems 215
5.8 Wavefront Shaping 239
5.9 Gravitational Lensing 244
 Problems 246
6 More on Geometrical Optics 255
6.1 Thick Lenses and Lens Systems 255
6.2 Analytical Ray Tracing 259
6.3 Aberrations 266
6.4 Grin Systems 284
6.5 Concluding Remarks 286
 Problems 286
7 The Superposition of Waves 290
7.1 The Addition of Waves of the Same
Frequency 291
7.2 The Addition of Waves of
Different Frequency 302
7.3 Anharmonic Periodic Waves 308
7.4 Nonperiodic Waves 318
 Problems 332
s
8 Polarization 338
8.1 The Nature of Polarized Light 338
8.2 Polarizers 346
8.3 Dichroism 347
8.4 Birefringence 351
8.5 Scattering and Polarization 361
8.6 Polarization by Reflection 363
8.7 Retarders 366
8.8 Circular Polarizers 373
8.9 Polarization of Polychromatic Light 374
8.10 Optical Activity 375
8.11 Induced Optical Effects—Optical
Modulators 380
8.12 Liquid Crystals 384
8.13 A Mathematical Description of
Polarization 387
 Problems 392
9 Interference 398
9.1 General Considerations 398
9.2 Conditions for Interference 402
9.3 Wavefront-Splitting Interferometers 405
9.4 Amplitude-Splitting Interferometers 416
9.5 Types and Localization
of Interference Fringes 432
9.6 Multiple-Beam Interference 433
9.7 Applications of Single and Multilayer Films 441
9.8 Applications of Interferometry 446
 Problems 452
10 Diffraction 457
10.1 Preliminary Considerations 457
10.2 Fraunhofer Diffraction 465
10.3 Fresnel Diffraction 505
10.4 Kirchhoff’s Scalar Diffraction Theory 532
10.5 Boundary Diffraction Waves 535
 Problems 536
11 Fourier Optics 542
11.1 Introduction 542
11.2 Fourier Transforms 542
11.3 Optical Applications 552
 Problems 583
12 Basics of Coherence Theory 588
12.1 Introduction 588
12.2 Fringes and Coherence 590
12.3 Visibility 594
12.4 The Mutual Coherence Function and the
Degree of Coherence 597
12.5 Coherence and Stellar Interferometry 603
 Problems 609
13 Modern Optics: Lasers and
Other Topics 612
13.1 Lasers and Laserlight 612
13.2 Imagery—The Spatial Distribution of Optical
Information 638
13.3 Holography 652
13.4 Nonlinear Optics 667
 Problems 672
 Appendix 1 677
 Appendix 2 680
 Table 1 681
 Solutions to Selected Problems 685
 Bibliography 708
 Index 712
 List of Tables 722
""", "url":"https://emineter.wordpress.com/wp-content/uploads/2020/04/hecht-optics-5ed.pdf", "page_buffer": 1
},
    "CHE 1754": {
    "content": """
    Preface..................................................................................................................... xv
The Authors..........................................................................................................xvii
Chapter 1 Introduction .......................................................................................... 1
1.1 Birth of a Concept ......................................................................................... 1
1.2 Some Basic Definitions ................................................................................. 2
1.3 Synthesis of Polymers ................................................................................... 4
1.4 Nomenclature................................................................................................. 4
1.5 Average Molar Masses and Distributions ..................................................... 8
1.6 Size and Shape............................................................................................. 10
1.7 Configuration ............................................................................................... 12
1.8 The Glass Transition Temperature Tg and the Melting Temperature Tm .... 14
1.9 Elastomers, Fibers, and Plastics.................................................................. 16
1.10 Fiber-Forming Polymers.............................................................................. 18
1.11 Plastics ......................................................................................................... 18
1.12 Thermosetting Polymers.............................................................................. 21
1.13 Elastomers.................................................................................................... 21
Problems .................................................................................................................. 25
References................................................................................................................ 27
Bibliography ............................................................................................................ 27
Chapter 2 Step-Growth Polymerization.............................................................. 29
2.1 General Reactions........................................................................................ 29
2.2 Reactivity of Functional Groups ................................................................. 30
2.3 Carothers Equation ...................................................................................... 31
2.4 Control of the Molar Mass.......................................................................... 32
2.5 Stoichiometric Control of Mn ...................................................................... 34
2.6 Kinetics ........................................................................................................ 36
2.7 Molar Mass Distribution in Linear Systems............................................... 38
2.8 Average Molar Masses ................................................................................ 39
2.9 Characteristics of Step-Growth Polymerization.......................................... 40
2.10 Typical Step-Growth Reactions................................................................... 40
2.11 Ring Formation............................................................................................ 41
2.12 Nonlinear Step-Growth Reactions............................................................... 42
2.13 Statistical Derivation.................................................................................... 43
2.14 Comparison with Experiment...................................................................... 44
2.15 Polyurethanes............................................................................................... 46
2.16 Thermosetting Polymers.............................................................................. 49
Problems .................................................................................................................. 52
References................................................................................................................ 56
Bibliography ............................................................................................................ 56
Chapter 3 Free-Radical Addition Polymerization .............................................. 57
3.1 Addition Polymerization.............................................................................. 57
3.2 Choice of Initiators...................................................................................... 57
3.3 Free-Radical Polymerization ....................................................................... 58
3.4 Initiators ....................................................................................................... 59
3.4.1 Initiator Efficiency......................................................................... 60
3.5 Chain Growth............................................................................................... 62
3.6 Termination.................................................................................................. 62
3.7 Steady-State Kinetics................................................................................... 63
3.8 High-Conversion Bulk Polymerizations...................................................... 65
3.9 Chain Transfer ............................................................................................. 67
3.9.1 Consequences of Chain Transfer .................................................. 70
3.10 Inhibitors and Retarders .............................................................................. 70
3.11 Activation Energies and the Effect of Temperature.................................... 72
3.12 Thermodynamics of Radical Polymerization.............................................. 73
3.13 Heats of Polymerization .............................................................................. 76
3.14 Polymerization Processes ............................................................................ 76
3.15 Features of Free-Radical Polymerization.................................................... 79
3.16 Controlled Radical Polymerization ............................................................. 79
3.17 Nitroxide-Mediated Polymerizations .......................................................... 81
3.18 Atom Transfer Radical Polymerization (ATRP)......................................... 82
3.19 Reverse ATRP.............................................................................................. 83
3.20 Degenerative Chain Transfer Reaction (DT) .............................................. 84
3.21 Reversible Addition Fragmentation Chain Transfer (RAFT) ..................... 84
3.22 CRP of Vinyl Chloride ................................................................................ 87
3.23 The Kinetics of CRP Processes .................................................................. 87
3.24 Application to Experimental Data............................................................... 90
Problems .................................................................................................................. 92
References................................................................................................................ 96
Bibliography ............................................................................................................ 96
Chapter 4 Ionic Polymerization.......................................................................... 99
4.1 General Characteristics................................................................................ 99
4.2 Cationic Polymerization ............................................................................ 100
4.3 Propagation by Cationic Chain Carriers ................................................... 101
4.4 Termination................................................................................................ 102
4.5 General Kinetic Scheme............................................................................ 103
4.6 Energetics of Cationic Polymerization...................................................... 103
4.7 Telechelic Polymers via Cationic Polymerization .................................... 104
4.8 Cationic Ring Opening Polymerization .................................................... 105
4.9 Stable Carbocations ................................................................................... 107
4.10 Anionic Polymerization............................................................................. 108
4.11 Living Polymers......................................................................................... 109
4.12 Kinetics and Molar Mass Distribution in Living Anionic Systems ......... 110
4.13 Metal Alkyl Initiators ................................................................................ 114
4.14 Solvent and Gegen Ion Effects.................................................................. 114
4.15 Anionic Ring-Opening Polymerization..................................................... 114
Problems ................................................................................................................ 116
References.............................................................................................................. 118
Bibliography .......................................................................................................... 119
Chapter 5 Linear Copolymers and Other Architectures................................... 121
5.1 General Characteristics.............................................................................. 121
5.2 Composition Drift...................................................................................... 122
5.3 The Copolymer Equation .......................................................................... 122
5.4 Monomer Reactivity Ratios....................................................................... 123
5.5 Reactivity Ratios and Copolymer Structure ............................................. 124
5.6 Monomer Reactivities and Chain Initiation.............................................. 127
5.7 Influence of Structural Effects on Monomer Reactivity Ratios ............... 127
5.7.1 Resonance Effects ....................................................................... 127
5.7.2 Polar Effects ................................................................................ 129
5.8 The Q–e Scheme ....................................................................................... 129
5.9 Alternating Copolymers ............................................................................ 131
5.10 Block Copolymer Synthesis ...................................................................... 133
5.10.1 Transformation Reactions ........................................................... 135
5.10.1.1 Cationic to CRP......................................................... 137
5.10.1.2 Anionic to CRP ......................................................... 138
5.10.1.3 ROMP to ATRP......................................................... 139
5.10.1.4 Step-Growth ATRP.................................................... 139
5.10.2 Coupling Reactions ..................................................................... 140
5.10.3 Use of CRP Methods .................................................................. 142
5.11 Graft Copolymer Synthesis ....................................................................... 145
5.12 Statistical and Gradient Copolymers......................................................... 147
5.13 Complex Molecular Architectures............................................................. 148
5.14 Dendrimers................................................................................................. 149
5.14.1 Divergent Growth........................................................................ 150
5.14.2 Convergent Growth ..................................................................... 151
5.14.3 Dendrimer Molecular Weight ..................................................... 152
5.14.4 Properties of Dendrimers ............................................................ 153
5.14.5 Applications of Dendrimers........................................................ 154
Problems ................................................................................................................ 155
References.............................................................................................................. 156
Bibliography .......................................................................................................... 156
Chapter 6 Polymer Stereochemistry ................................................................. 157
6.1 Architecture ............................................................................................... 157
6.2 Orientation ................................................................................................. 157
6.3 Configuration ............................................................................................. 158
6.3.1 Monotactic Polymers .................................................................. 159
6.3.2 Ditactic Polymers ........................................................................ 160
6.3.3 Polyethers .................................................................................... 160
6.4 Geometric Isomerism ................................................................................ 162
6.5 Conformation of Stereoregular Polymers ................................................. 163
6.6 Factors Influencing Stereoregulation......................................................... 165
6.7 Homogeneous Stereospecific Cationic Polymerizations........................... 167
6.8 Homogeneous Stereoselective Anionic Polymerizations.......................... 168
6.9 Homogeneous Diene Polymerization........................................................ 170
6.10 Summary.................................................................................................... 172
Problems ................................................................................................................ 172
References.............................................................................................................. 173
Bibliography .......................................................................................................... 173
Chapter 7 Polymerization Reactions Initiated by Metal Catalysts
and Transfer Reactions .................................................................... 175
7.1 Polymerization Using Ziegler–Natta Catalysts......................................... 175
7.2 Nature of the Catalyst ............................................................................... 176
7.3 Nature of Active Centers........................................................................... 177
7.4 Bimetallic Mechanism............................................................................... 177
7.5 Monometallic Mechanism ......................................................................... 178
7.6 Stereoregulation ......................................................................................... 180
7.7 Ring-Opening Metathesis Polymerization (ROMP) ................................. 181
7.8 Monocyclic Monomers.............................................................................. 182
7.9 Bicyclo- and Tricyclomonomers ............................................................... 183
7.10 Copolyalkenamers ..................................................................................... 184
7.11 Living Systems .......................................................................................... 184
7.12 Group Transfer Polymerization (GTP) ..................................................... 186
7.13 Aldol Group Transfer Polymerization....................................................... 187
7.14 Metallocene Catalysts................................................................................ 188
7.14.1 Metallocene/Aluminoxane Catalysts .......................................... 189
7.14.2 Stereoregulation........................................................................... 189
7.14.3 Cationic Metallocenes................................................................. 192
7.14.4 Mechanism of Stereoregulation .................................................. 192
7.15 Concluding Remarks ................................................................................. 193
Problems ................................................................................................................ 194
References.............................................................................................................. 194
Bibliography .......................................................................................................... 194
Chapter 8 Polymers in Solution........................................................................ 197
8.1 Thermodynamics of Polymer Solutions.................................................... 197
8.2 Ideal Mixtures of Small Molecules........................................................... 197
8.3 Nonideal Solutions .................................................................................... 199
8.4 Flory–Huggins Theory: Entropy of Mixing.............................................. 199
8.5 Enthalpy Change on Mixing ..................................................................... 203
8.6 Free Energy of Mixing .............................................................................. 204
8.7 Limitations of the Flory–Huggins Theory ................................................ 205
8.8 Phase Equilibria......................................................................................... 206
8.9 Flory–Krigbaum Theory............................................................................ 208
8.10 Location of the Theta Temperature........................................................... 210
8.11 Lower Critical Solution Temperatures ...................................................... 213
8.12 Solubility and the Cohesive Energy Density ............................................ 216
8.13 Polymer–Polymer Mixtures....................................................................... 219
8.14 Kinetics of Phase Separation..................................................................... 223
Problems ................................................................................................................ 224
References.............................................................................................................. 227
Bibliography .......................................................................................................... 227
Chapter 9 Polymer Characterization — Molar Masses ................................... 229
9.1 Introduction................................................................................................ 229
9.2 Molar Masses, Molecular Weights, and SI Units ..................................... 229
9.3 Number-Average Molar Mass Mn ............................................................. 229
9.4 End-Group Assay....................................................................................... 230
9.5 Colligative Properties of Solutions ........................................................... 230
9.6 Osmotic Pressure ....................................................................................... 231
9.7 Light Scattering ......................................................................................... 234
9.7.1 Scattering from Large Particles .................................................. 236
9.8 Dynamic Light Scattering ......................................................................... 239
9.9 Viscosity..................................................................................................... 240
9.9.1 Viscosity-Average Molecular Weight ......................................... 242
9.10 Gel Permeation Chromatography.............................................................. 243
9.11 MALDI ...................................................................................................... 247
Problems ................................................................................................................ 248
References.............................................................................................................. 251
Bibliography .......................................................................................................... 252
Chapter 10 Polymer Characterization — Chain Dimensions, Structures,
and Morphology............................................................................... 253
10.1 Average Chain Dimensions ....................................................................... 253
10.2 Freely Jointed Chain Model...................................................................... 254
10.3 Short-Range Effects................................................................................... 255
10.4 Chain Stiffness........................................................................................... 255
10.5 Treatment of Dilute Solution Data............................................................ 256
10.5.1 The Second Virial Coefficient..................................................... 256
10.5.2 Expansion Factor α..................................................................... 257
10.5.3 Flory–Fox Theory ....................................................................... 258
10.5.4 Indirect Estimates of Unperturbed Chain Dimensions............... 259
10.5.5 Influence of Tacticity on Chain Dimensions .............................. 259
10.6 Nuclear Magnetic Resonance (NMR)....................................................... 260
10.7 Infrared Spectroscopy................................................................................ 262
10.8 Thermal Analysis....................................................................................... 264
10.9 Wide-Angle and Small-Angle Scattering.................................................. 265
10.9.1 Wide-Angle X-Ray Scattering .................................................... 266
10.9.2 Small-Angle X-Ray Scattering (SAXS) ..................................... 267
10.9.3 Small-Angle Neutron Scattering (SANS)................................... 268
10.10 Microscopy ................................................................................................ 271
10.10.1 Optical Microscopy..................................................................... 272
10.10.2 Scanning Electron Microscopy ................................................... 273
10.10.3 Transmission Electron Microscopy............................................. 274
10.10.4 Atomic Force Microscopy and Scanning Tunneling
Microscopy.................................................................................. 274
Problems ................................................................................................................ 276
References.............................................................................................................. 277
Bibliography .......................................................................................................... 277
Chapter 11 The Crystalline State and Partially Ordered Structures.................. 279
11.1 Introduction................................................................................................ 279
11.2 Mechanism of Crystallization ................................................................... 279
11.3 Temperature and Growth Rate .................................................................. 281
11.4 Melting....................................................................................................... 282
11.4.1 Effect of Crystallite Size on Melting.......................................... 282
11.5 Thermodynamic Parameters ...................................................................... 282
11.6 Crystalline Arrangement of Polymers....................................................... 285
11.6.1 Factors Affecting Crystallinity and Tm........................................ 285
11.6.1.1 Symmetry................................................................... 285
11.6.1.2 Intermolecular Bonding............................................. 286
11.6.1.3 Tacticity ..................................................................... 287
11.6.1.4 Branching and Molar Mass....................................... 287
11.7 Morphology and Kinetics.......................................................................... 287
11.8 Morphology ............................................................................................... 287
11.8.1 Crystallites................................................................................... 288
11.8.2 Single Crystals ............................................................................ 288
11.8.3 Hedrites ....................................................................................... 289
11.8.4 Crystallization from the Melt...................................................... 289
11.8.5 Spherulites ................................................................................... 291
11.9 Kinetics of Crystallization......................................................................... 292
11.9.1 Isothermal Crystallization ........................................................... 293
11.9.2 The Avrami Equation .................................................................. 293
11.9.3 Deviations from Avrami Equation .............................................. 294
11.10 Block Copolymers ..................................................................................... 294
11.11 Historical Development of Polymer Liquid Crystals ............................... 296
11.12 Liquid Crystalline Phases.......................................................................... 297
11.13 Identification of the Mesophases............................................................... 300
11.14 Lyotropic Main-Chain Liquid Crystal Polymers ...................................... 302
11.15 Thermotropic Main-Chain Liquid Crystal Polymers................................ 304
11.16 Side-Chain Liquid Crystal Polymers ........................................................ 309
11.17 Chiral Nematic Liquid Crystal Polymers.................................................. 311
Problems ................................................................................................................ 314
References.............................................................................................................. 318
Bibliography .......................................................................................................... 318
Chapter 12 The Glassy State and Glass Transition............................................ 321
12.1 The Amorphous State ................................................................................ 321
12.2 The Glassy State........................................................................................ 321
12.3 Relaxation Processes in the Glassy State ................................................. 321
12.4 Glass Transition Region ............................................................................ 323
12.4.1 The Glass Transition Temperature, Tg ........................................ 323
12.4.2 Experimental Demonstration of Tg ............................................. 324
12.4.2.1 Measurement of Tg from V–T Curves ...................... 325
12.4.2.2 Thermal Methods ...................................................... 326
12.4.3 Factors Affecting Tg .................................................................... 327
12.4.3.1 Chain Flexibility........................................................ 328
12.4.3.2 Steric Effects ............................................................. 328
12.4.3.3 Configurational Effects.............................................. 330
12.4.3.4 Effect of Cross-Links on Tg ...................................... 330
12.5 Theoretical Treatments .............................................................................. 330
12.5.1 The Free-Volume Theory ............................................................ 331
12.5.2 Gibbs–Di Marzio Thermodynamic Theory ................................ 335
12.5.3 Adam–Gibbs Theory................................................................... 336
12.6 Dependence of Tg on Molar Mass ............................................................ 337
12.7 Structural Relaxation and Physical Aging ................................................ 338
Problems ................................................................................................................ 339
References.............................................................................................................. 342
Bibliography .......................................................................................................... 343
Chapter 13 Rheology and Mechanical Properties.............................................. 345
13.1 Introduction to Rheology........................................................................... 345
13.2 The Five Regions of Viscoelastic Behavior.............................................. 346
13.3 The Viscous Region................................................................................... 347
13.3.1 Shear Dependence of Viscosity .................................................. 349
13.3.2 Kinetic Units in Polymer Chains................................................ 351
13.3.3 Effect of Chain Length ............................................................... 352
13.3.4 Temperature Dependence of η.................................................... 353
13.3.5 Concentration Dependence of Viscosity..................................... 353
13.3.6 Time-Dependent Behavior .......................................................... 354
13.4 Mechanical Properties ............................................................................... 355
13.4.1 Interrelation of Moduli................................................................ 357
13.5 Mechanical Models Describing Viscoelasticity ........................................ 357
13.6 Linear Viscoelastic Behavior of Amorphous Polymers............................ 360
13.6.1 Creep ........................................................................................... 360
13.6.2 Stress–Strain Measurements ....................................................... 363
13.6.3 Effect of Temperature on Stress–Strain Response ..................... 363
13.6.4 Boltzmann Superposition Principle ............................................ 364
13.6.5 Stress Relaxation......................................................................... 365
13.7 Dynamic Mechanical and Dielectric Thermal Analysis ........................... 366
13.7.1 Dynamic Mechanical Thermal Analysis (DMTA) ..................... 366
13.7.2 Dielectric Thermal Analysis (DETA) ......................................... 369
13.7.3 Comparison Between DMTA and DETA ................................... 371
13.8 Time–Temperature Superposition Principle.............................................. 373
13.9 Dynamic Viscosity..................................................................................... 377
13.10 A Molecular Theory for Viscoelasticity.................................................... 378
13.11 The Reptation Model................................................................................. 380
Problems ................................................................................................................ 382
References.............................................................................................................. 387
Bibliography .......................................................................................................... 388
Chapter 14 The Elastomeric State ...................................................................... 389
14.1 General Introduction.................................................................................. 389
14.1.1 Natural Rubber ............................................................................ 390
14.2 Experimental Vulcanization....................................................................... 391
14.3 Properties of Elastomers............................................................................ 391
14.4 Thermodynamic Aspects of Rubberlike Elasticity ................................... 392
14.5 Nonideal Elastomers.................................................................................. 394
14.6 Distribution Function for Polymer Conformation .................................... 395
14.7 Statistical Approach................................................................................... 398
14.7.1 Experimental Stress–Strain Results ............................................ 398
14.7.1.1 Simple Extension....................................................... 398
14.7.1.2 Simple Compression.................................................. 400
14.7.1.3 Pure Shear.................................................................. 400
14.7.1.4 Large Elastic Deformation ........................................ 400
14.8 Swelling of Elastomeric Networks............................................................ 400
14.9 Network Defects ........................................................................................ 401
14.10 Resilience of Elastomers ........................................................................... 403
Problems ................................................................................................................ 405
References.............................................................................................................. 408
Bibliography .......................................................................................................... 408
Chapter 15 Structure–Property Relations ........................................................... 409
15.1 General Considerations.............................................................................. 409
15.2 Control of Tm and Tg.................................................................................. 409
15.2.1 Chain Stiffness ............................................................................ 410
15.2.2 Intermolecular Bonding .............................................................. 411
15.3 Relation Between Tm and Tg...................................................................... 413
15.4 Random Copolymers ................................................................................. 413
15.5 Dependence of Tm and Tg on Copolymer Composition............................ 414
15.6 Block Copolymers ..................................................................................... 417
15.7 Plasticizers ................................................................................................. 419
15.8 Crystallinity and Mechanical Response.................................................... 420
15.9 Application to Fibers, Elastomers, and Plastics ....................................... 422
15.10 Fibers ......................................................................................................... 422
15.10.1 Chemical Requirements .............................................................. 423
15.10.1.1 Linear Polyesters ....................................................... 425
15.10.2 Mechanical Requirements for Fibers.......................................... 426
15.10.2.1 Spinning Techniques ................................................. 426
15.10.2.1.1 Melt Spinning ....................................... 426
15.10.2.1.2 Wet and Dry Spinning .......................... 426
15.10.2.2 Drawing, Orientation, and Crystallinity.................... 427
15.10.2.3 Modulus and Chain Stiffness .................................... 428
15.10.2.4 Other Factors ............................................................. 428
15.11 Aromatic Polyamides ................................................................................ 429
15.12 Polyethylene............................................................................................... 431
15.13 Elastomers and Cross-Linked Networks................................................... 434
15.13.1 Cross-Linking.............................................................................. 435
15.13.2 Creep in Cross-Linked Polymers................................................ 435
15.13.3 Additives...................................................................................... 435
15.14 Plastics ....................................................................................................... 435
15.14.1 Plastic Selection for Bottle Crate Manufacture.......................... 437
15.14.2 Medical Applications .................................................................. 438
15.15 High-Temperature Speciality Polymers .................................................... 439
15.16 Carbon Fibers ............................................................................................ 446
15.17 Concluding Remarks ................................................................................. 446
Problems ................................................................................................................ 448
References.............................................................................................................. 453
Bibliography .......................................................................................................... 454
Chapter 16 Polymers for the Electronics Industry............................................. 455
16.1 Introduction................................................................................................ 455
16.2 Polymer Resists for IC Fabrication........................................................... 455
16.3 The Lithographic Process.......................................................................... 456
16.4 Polymer Resists ......................................................................................... 457
16.4.1 Sensitivity .................................................................................... 458
16.4.2 Resolution.................................................................................... 459
16.5 Photolithography........................................................................................ 459
16.5.1 Positive Photoresists.................................................................... 459
16.5.2 Negative Photoresists .................................................................. 460
16.6 Electron Beam Sensitive Resists............................................................... 463
16.6.1 Positive Resists............................................................................ 463
16.6.2 Negative Resists .......................................................................... 464
16.7 X-ray and Ion Sensitive Resists ................................................................ 464
16.8 Electroactive Polymers .............................................................................. 465
16.9 Conduction Mechanisms ........................................................................... 466
16.10 Preparation of Conductive Polymers......................................................... 467
16.11 Polyacetylene ............................................................................................. 469
16.12 Poly(p-phenylene)...................................................................................... 472
16.13 Polyheterocyclic Systems .......................................................................... 474
16.13.1 Polypyrrole .................................................................................. 475
16.13.2 Sulfur Compounds ...................................................................... 475
16.14 Polyaniline ................................................................................................. 476
16.15 Poly(Phenylene Sulfide) ............................................................................ 476
16.16 Poly(1,6-heptadiyne).................................................................................. 476
16.17 Applications ............................................................................................... 476
16.18 Photonic Applications................................................................................ 477
16.19 Light-Emitting Polymers ........................................................................... 477
16.19.1 Applications................................................................................. 478
16.20 Nonlinear Optics........................................................................................ 478
16.21 Langmuir–Blodgett Films.......................................................................... 481
16.22 Optical Information Storage...................................................................... 483
16.23 Thermorecording on Liquid Crystalline Polymers ................................... 486
References.............................................................................................................. 487
Bibliography .......................................................................................................... 487
Index ................................................................................................................... 489
""",
"url":"https://www.eng.uc.edu/~beaucag/Classes/Properties/Books/Arrighi,%20Valeria_%20Cowie,%20J.M.G%20-%20Polymers%20_%20Chemistry%20and%20Physics%20of%20Modern%20Materials,%20Third%20Edition-CRC%20Press%20(2007).pdf",
"page_buffer": 19
}
}