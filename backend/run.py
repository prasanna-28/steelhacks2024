from app import create_app
from app import gemini

app = create_app()

if __name__ == '__main__':
    # app.run(debug=True)
    example_latex = r"\n \documentclass[12pt,a4paper]{article} \usepackage[margin=1in]{geometry} \usepackage{amsmath} \begin{document} \section{Inverse Matrices} An $n\times n$ matrix $A$ is invertible if there is a matrix $A^{-1}$ such that $AA^{-1} = A^{-1}A = I$. \subsection{Examples} \begin{itemize} \item $A = \begin{bmatrix} 2 & 3 \\ 1 & 2 \end{bmatrix}$, $B = \begin{bmatrix} 2 & -3 \\ -1 & 2 \end{bmatrix}$ are inverses \item Since $AB = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$, we can write $B = A^{-1}$ \item Not all matrices have inverses: $A = \begin{bmatrix} 0 & 0 \\ 2 & 3 \end{bmatrix}$ has no inverse \item Singular matrices $\begin{bmatrix} 2 & 3 \\ 2 & 3 \end{bmatrix} = B$ also have no inverse \end{itemize} \subsection{Connection to Linear Transformations} $A$ : $\mathbb{R}^n \to \mathbb{R}^n$ is a linear transformation with associated matrix $A$ (in standard basis). The inverse transformation exists if and only if $A^{-1}$ exists. \section{2x2 Inverse Formula} Let $A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$, then if $ad-bc \neq 0$: $A^{-1} = \frac{1}{ad-bc} \begin{bmatrix} d & -b \\ -c & a \end{bmatrix}$ Note: $ad-bc$ is called the determinant of $A$. There is a general $n\times n$ inverse formula (involving the determinant and cofactors) but it's complicated to compute (and we won't use it). For now, we'll focus on the 2x2 case. \subsection{Using Gauss-Jordan to Find the Inverse} Suppose $A$ has inverse $A^{-1}$ Then $AA^{-1} = I$ So $A[A^{-1}] = [I]$ To find $A^{-1}$, we must solve the system $Ax = e_i$ for each $i$. Instead of solving $[A][x_1] = [e_1]$, $[A][x_2] = [e_2]$, ..., $[A][x_n] = [e_n]$ individually, we can combine these systems into one matrix equation: $[A][x_1, x_2, ..., x_n] = [e_1, e_2, ..., e_n] = [I]$ If $A$ doesn't have $n$ pivots (one in each row), then $A^{-1}$ doesn't exist. If $A$ has $n$ pivots, then the algorithm produces $A^{-1}$. \subsection{Summary: Algorithm to Find $A^{-1}$ (if it exists)} \begin{itemize} \item If $A$ doesn't have $n$ pivots, then $A^{-1}$ doesn't exist \item If $A$ has $n$ pivots, write $[A|I]$ and use row operations to get $[I|A^{-1}]$ \end{itemize} \section{Example: Finding $A^{-1}$} Find $A^{-1}$ if it exists: $A = \begin{bmatrix} 2 & 4 & -2 \\ 4 & 9 & -3 \\ -2 & -3 & 7 \end{bmatrix}$ We write $[A|I]$ and perform row operations: $\begin{bmatrix} 2 & 4 & -2 & | & 1 & 0 & 0 \\ 4 & 9 & -3 & | & 0 & 1 & 0 \\ -2 & -3 & 7 & | & 0 & 0 & 1 \end{bmatrix}$ (Row operations omitted for brevity) $\begin{bmatrix} 1 & 0 & 0 & | & -\frac{9}{2} & 2 & \frac{1}{2} \\ 0 & 1 & 0 & | & 2 & -1 & 0 \\ 0 & 0 & 1 & | & \frac{1}{2} & 0 & \frac{1}{2} \end{bmatrix}$ Therefore, $A^{-1} = \begin{bmatrix} -\frac{9}{2} & 2 & \frac{1}{2} \\ 2 & -1 & 0 \\ \frac{1}{2} & 0 & \frac{1}{2} \end{bmatrix}$ (Check: $AA^{-1} = I$) \section{Using Inverses to Solve Systems} If $A$ exists, we can solve $Ax = b$ by multiplying both sides by $A^{-1}$: $A^{-1}Ax = A^{-1}b$ $Ix = A^{-1}b$ $x = A^{-1}b$ Note: $A^{-1}$ has a solution if (and only if) $A$ has $n$ pivots (i.e., $A$ is invertible). This solution is unique. \end{document}\n"
    # gemini.make_summary(example_latex)
    gemini.make_quiz(example_latex)
    file = '''{
  "definitions": [
    {
      "question": "What is the definition of an invertible matrix?",
      "answer": "An n x n matrix A is invertible if there exists a matrix, denoted A<sup>-1</sup>, such that AA<sup>-1</sup> = A<sup>-1</sup>A = I, where I is the identity matrix."
    },
    {
      "question": "What is a singular matrix?",
      "answer": "A singular matrix is a square matrix that does not have an inverse. This is because its determinant is zero."
    },
    {
      "question": "What is the determinant of a 2x2 matrix?",
      "answer": "The determinant of a 2x2 matrix  A = [[a, b], [c, d]] is given by ad-bc."
    },
    {
      "question": "How does the invertibility of a matrix relate to linear transformations?",
      "answer": "A linear transformation represented by a matrix A is invertible if and only if the matrix A is invertible. The inverse of the transformation is then represented by the inverse matrix A<sup>-1</sup>."
    },
    {
      "question": "Describe the Gauss-Jordan method for finding the inverse of a matrix.",
      "answer": "1. Form the augmented matrix [A|I], where I is the identity matrix of the same size as A. 2. Use row operations to transform the left side of the augmented matrix into the identity matrix. 3. The right side of the augmented matrix will then be the inverse of the original matrix, A<sup>-1</sup>."
    }
  ],
  "problems": [
    {
      "question": "Calculate the inverse of the matrix A = [[3, 1], [2, 1]] using the 2x2 inverse formula.",
      "answer": "A<sup>-1</sup> = [[1, -1], [-2, 3]]"
    },
    {
      "question": "Determine if the matrix B = [[1, 2], [2, 4]] is invertible. If so, find its inverse. If not, explain why.",
      "answer": "The matrix B is not invertible because its determinant is 0 (ad - bc = 1*4 - 2*2 = 0)."
    },
    {
      "question": "Use the Gauss-Jordan method to find the inverse of the matrix C = [[1, 1, 1], [0, 1, 1], [0, 0, 1]]",
      "answer": "C<sup>-1</sup> = [[1, -1, 0], [0, 1, -1], [0, 0, 1]]"
    },
    {
      "question": "Given the system of equations: x + y = 5 2x - y = 1 a) Write the system of equations in matrix form. b) Find the inverse of the coefficient matrix. c) Use the inverse matrix to solve the system of equations.",
      "answer": "a) [[1, 1], [2, -1]] [[x], [y]] = [[5], [1]] b)  [[1/3, 1/3], [2/3, -1/3]] c) x = 2, y = 3"
    }
  ]
}'''
'''
{
"definitions": [
    {
      "question": "What is the definition of an invertible matrix?",
      "answer": "An n x n matrix A is invertible if there exists a matrix A<sup>-1</sup> such that AA<sup>-1</sup> = A<sup>-1</sup>A = I, where I is the identity matrix."
    },
    {
      "question": "What is a singular matrix?",
      "answer": "A singular matrix is a square matrix that does not have an inverse. This means its determinant is zero."
    },
    {
      "question": "How is the concept of an invertible matrix related to linear transformations?",
      "answer": "A linear transformation represented by a matrix A has an inverse transformation if and only if the matrix A is invertible."
    },
    {
      "question": "What is the determinant of a 2x2 matrix?",
      "answer": "For a 2x2 matrix A = [[a, b], [c, d]], the determinant is calculated as ad - bc."
    },
    {
      "question": "Describe the Gauss-Jordan method for finding the inverse of a matrix.",
      "answer": "1. Form an augmented matrix [A|I], where I is the identity matrix. 2. Apply row operations to transform the left side (A) into the identity matrix. 3. The resulting right side of the augmented matrix will be the inverse of the original matrix, A<sup>-1</sup>."
    }
  ],
  "problems": [
    {
      "question": "Calculate the inverse of the following matrix: A = [[3, 1], [4, 2]]",
      "answer": "A<sup>-1</sup> = [[1, -0.5], [-2, 1.5]]"
    },
    {
      "question": "Determine if the following matrix is invertible. If so, find its inverse: B = [[1, 2], [2, 4]]",
      "answer": "The matrix B is not invertible because its determinant is 0."
    },
    {
      "question": "Solve the system of equations using the matrix inverse method:\n 2x + 3y = 8\n  x  + 2y = 5",
      "answer": "x = 1, y = 2"
    }
  ]
}
'''
    # gemini.make_json(file)
