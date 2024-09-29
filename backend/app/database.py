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
    "MATH 0001": {
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
    }
}