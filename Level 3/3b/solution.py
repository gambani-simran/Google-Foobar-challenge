from fractions import Fraction

# def​ ​solution(m):
# ​ ​​ ​​ ​​ ​#​ ​Your​ ​code​ ​here

def gcd(x, y):
    def gcdTwo(x, y):
        if y == 0:
            return x
        return gcdTwo(y, x%y)
    return gcdTwo(abs(x), abs(y))

def lcm(x, y):
    return int(x*y/gcd(x,y))

def simplify(x, y):
    g = gcd(x, y)
    return Fraction(int(x/g), int(y/g))

def transform(m):
    sum_list = list(map(sum, m))
    bool_indices = list(map(lambda x: x == 0, sum_list))
    indices = set([i for i, x in enumerate(bool_indices) if x])
    new_mat = []
    for i in range(len(m)):
        new_mat.append(list(map(lambda x: Fraction(0, 1) if(sum_list[i] == 0) else simplify(x, sum_list[i]), m[i])))
    transform_mat = []
    zeros_mat = []
    for i in range(len(new_mat)):
        if i not in indices:
            transform_mat.append(new_mat[i])
        else:
            zeros_mat.append(new_mat[i])
    transform_mat.extend(zeros_mat)
    tmat = []
    for i in range(len(transform_mat)):
        tmat.append([])
        extend_mat = []
        for j in range(len(transform_mat)):
            if j not in indices:
                tmat[i].append(transform_mat[i][j])
            else:
                extend_mat.append(transform_mat[i][j])
        tmat[i].extend(extend_mat)
    return [tmat, len(zeros_mat)]

def copy_mat(m):
    cmat = []
    for i in range(len(m)):
        cmat.append([])
        for j in range(len(m[i])):
            cmat[i].append(Fraction(m[i][j].numerator, m[i][j].denominator))
    return cmat

def gaussElmination(m, values):
    matrix = copy_mat(m)
    for i in range(len(matrix)):
        index = -1
        for j in range(i, len(matrix)):
            if matrix[j][i].numerator != 0:
                index = j
                break
        if index == -1:
            raise ValueError('Gauss elimination failed!')
        matrix[i], matrix[index] = matrix[index], matrix[j]
        values[i], values[index] = values[index], values[i]
        for j in range(i+1, len(matrix)):
            if matrix[j][i].numerator == 0:
                continue
            ratio = -matrix[j][i]/matrix[i][i]
            for k in range(i, len(matrix)):
                matrix[j][k] += ratio * matrix[i][k]
            values[j] += ratio * values[i]
    res = [0 for i in range(len(matrix))]
    for i in range(len(matrix)):
        index = len(matrix) -1 -i
        end = len(matrix) - 1
        while end > index:
            values[index] -= matrix[index][end] * res[end]
            end -= 1
        res[index] = values[index]/matrix[index][index]
    return res

def transpose(m):
    transpose = []
    for i in range(len(m)):
        for j in range(len(m)):
            if i == 0:
                transpose.append([])
            transpose[j].append(m[i][j])    
    return transpose

def inverseOfMatrixQ(m):
    transposeOfMatrixQ = transpose(m)
    matrixInverse = []
    for i in range(len(transposeOfMatrixQ)):
        values = [Fraction(int(i==j), 1) for j in range(len(m))]
        matrixInverse.append(gaussElmination(transposeOfMatrixQ, values))
    return matrixInverse

def matrixMultiply(mat1, mat2):
    res = []
    for i in range(len(mat1)):
        res.append([])
        for j in range(len(mat2[0])):
            res[i].append(Fraction(0, 1))
            for k in range(len(mat1[0])):
                res[i][j] += mat1[i][k] * mat2[k][j]
    return res

def splitQRmatrices(m, lengthOfR):
    lengthOfQ = len(m) - lengthOfR
    Q = []
    R = []
    for i in range(lengthOfQ):
        Q.append([int(i==j)-m[i][j] for j in range(lengthOfQ)])
        R.append(m[i][lengthOfQ:])
    return [Q, R]

def solution(m):
    res = transform(m)
    if res[1] == len(m):
        return [1, 1]
    Q, R = splitQRmatrices(*res)
    inverse = inverseOfMatrixQ(Q)
    res = matrixMultiply(inverse, R)
    row = res[0]
    l = 1
    for item in row:
        l = lcm(l, item.denominator)
    res = list(map(lambda x: int(x.numerator*l/x.denominator), row))
    res.append(l)
    return res


w, h = 6, 6
Matrix = [[0 for x in range(w)] for y in range(h)]

Matrix[0][1] = 1
Matrix[0][5] = 1

Matrix[1][0] = 4
Matrix[1][3] = 3
Matrix[1][4] = 2

a, b = 5,5
Matrix1 = [[0 for x in range(a)] for y in range(b)]
Matrix1[0][1] = 2
Matrix1[0][2] = 1

Matrix1[1][3] = 3
Matrix1[1][4] = 4

arr = solution(Matrix1)
print(arr)