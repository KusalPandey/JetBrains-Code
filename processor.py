class Matrix:
    def __init__(self):
        self.matrices = []
        self.matrices_dim = []
        self.matrix_dim = "self.matrices_dim[0]"
        self.i = "self.matrix_dim[0]"
        self.j = "self.matrix_dim[1]"
        self.total = "self.i * self.j"

    def matrix_plot(self, dim_data):
        maps = []
        i = dim_data[0]
        j = dim_data[1]
        count_i = 1
        count_j = 1
        for iteration in range(int(i)):
            for loops in range(int(j)):
                position = str(count_i) + str(count_j)    # count = count_i + count_j just in case
                maps.append(position)                      # map.append(count)
                count_j += 1
            count_i += 1
            count_j = 1
        # map = self.output(map)
        return maps

    def matrix_dimension(self, data):
        matrix = data.split(' ')
        self.matrices_dim.append(matrix)
        if 0 < len(matrix) < 3:
            row = int(matrix[0])
            column = int(matrix[1])
            return row, column
        else:
            print("The operation cannot be performed.")  # only 2d model
            exit(0)

    def matrix_structure(self, i=1, j=1):
        matrix = []
        for times in range(i):
            row_input = input()
            b = row_input.split(' ')
            if len(b) == j:
                matrix.extend(b)
            else:
                print("The operation cannot be performed.")  # input out of range
                exit(0)
        self.matrices.append(matrix)
        return matrix

    def output(self, data):
        self.matrix_dim = self.matrices_dim[-1]
        self.i = self.matrix_dim[0]
        self.j = self.matrix_dim[1]
        self.total = int(self.i) * int(self.j)
        output_list = data
        output_str = ''
        count = 0
        for iterations in range(self.total):
            output_str = output_str + str(output_list[iterations]) + " "
            count += 1
            if count == int(self.j):
                output_str = output_str + "\n"
                count = 0
        print("The result is: ")
        return output_str

    def constant_multiple(self, data):
        self.matrix_dim = self.matrices_dim[0]
        self.i = self.matrix_dim[0]
        self.j = self.matrix_dim[1]
        self.total = int(self.i) * int(self.j)
        data = data.split(" ")
        matrix = self.matrices[0]
        output_list = []
        for i in range(self.total):
            temp = float(matrix[i]) * float(data[0])
            output_list.append(temp)
        out = self.output(output_list)
        return out

    def add(self):
        self.matrix_dim = self.matrices_dim[-1]
        self.i = self.matrix_dim[0]
        self.j = self.matrix_dim[1]
        self.total = int(self.i) * int(self.j)
        matrix = self.matrices
        matrix_1 = matrix[0]
        matrix_2 = matrix[1]
        output_list = []
        if self.i == self.j:
            for i in range(self.total):
                temp = float(matrix_1[i]) + float(matrix_2[i])
                output_list.append(temp)
            return self.output(output_list)
        else:
            return "The operation cannot be performed."  # two matrices dimension are not same

    def multiply(self):
        self.matrix_dim = self.matrices_dim[0]
        self.i = self.matrix_dim[0]
        self.j = self.matrix_dim[1]
        self.total = int(self.i) * int(self.j)
        matrix = self.matrices
        matrix_1 = matrix[0]
        matrix_2 = matrix[1]
        matrix_dim = self.matrices_dim[1]
        i = matrix_dim[0]
        j = matrix_dim[1]
        output_list = []
        if self.j != i:
            return "The operation cannot be performed."
        else:
            multiple_total = int(self.i) * int(j)
            count_x = 0
            count_y = 0
            pos_val = 0
            reference_count_y = 0
            reference_count_x = 0
            for location in range(multiple_total):
                for individual in range(int(i)):
                    spi = float(matrix_1[count_x])
                    spj = float(matrix_2[count_y])
                    pos_val = pos_val + spi * spj
                    count_x += 1
                    count_y += int(j)
                reference_count_y += 1
                count_y = reference_count_y
                output_list.append(pos_val)
                pos_val = 0
                if reference_count_y == int(j):
                    count_x = count_x
                    count_y = 0
                    reference_count_y = 0
                    reference_count_x = count_x
                else:
                    count_x = reference_count_x
            output_str = ''
            count_x = 0
            for iterations in range(multiple_total):
                output_str = output_str + str(output_list[iterations]) + " "
                count_x += 1
                if count_x == int(j):
                    output_str = output_str + "\n"
                    count_x = 0
            print("The result is: ")
            return output_str

    def main(self):
        while True:
            self.matrices_dim = []
            self.matrices = []
            print("1. Add matrices")
            print("2. Multiply matrix by a constant")
            print("3. Multiply matrices")
            print("4. Transpose matrix")
            print("5. Calculate a determinant")
            print("6. Inverse matrix")
            print("0. Exit")
            choice = int(input("Your choice: "))

            if choice == 1 or choice == 3:
                matrix_dim = input("Enter the size of first matrix: ")
                row, column = self.matrix_dimension(matrix_dim)
                print("Enter first matrix: ")
                self.matrix_structure(row, column)
                matrix_dim = input("Enter the size of second matrix: ")
                row, column = self.matrix_dimension(matrix_dim)
                print("Enter second matrix: ")
                self.matrix_structure(row, column)
                if choice == 1:
                    print(self.add())
                elif choice == 3:
                    print(self.multiply())

            elif choice == 2:
                matrix_dim = input("Enter the size of matrix: ")
                row, column = self.matrix_dimension(matrix_dim)
                print("Enter matrix: ")
                self.matrix_structure(row, column)
                constant = input("Enter constant: ")
                print(self.constant_multiple(constant))

            elif choice == 4:
                print("1. Main diagonal")
                print("2. Side diagonal")
                print("3. Vertical line")
                print("4. Horizontal line")
                choice_2 = int(input("Your choice: "))
                matrix_dim = input("Enter the size of matrix: ")
                row, column = self.matrix_dimension(matrix_dim)
                print("Enter matrix: ")
                self.matrix_structure(row, column)
                transpose = Transpose(self.matrices, self.matrices_dim)
                if choice_2 == 1:
                    print(self.output(transpose.main_diagonal(self.matrices[0])))
                elif choice_2 == 2:
                    print(self.output(transpose.side_diagonal(self.matrices[0])))
                elif choice_2 == 3:
                    print(transpose.vertical_line(self.matrices[0]))
                elif choice_2 == 4:
                    print(transpose.horizontal_line(self.matrices[0]))

            elif choice == 5:
                matrix_dim = input("Enter matrix size: ")
                row, column = self.matrix_dimension(matrix_dim)
                print("Enter matrix: ")
                self.matrix_structure(row, column)
                determinant = Determinant()
                print(determinant.deter(self.matrices[0], self.matrices_dim[0]))

            elif choice == 6:
                matrix_dim = input("Enter matrix size: ")
                row, column = self.matrix_dimension(matrix_dim)
                print("Enter matrix: ")
                self.matrix_structure(row, column)
                determinant = Determinant()
                deter = determinant.deter(self.matrices[0], self.matrices_dim[0])
                transpose = Transpose(self.matrices, self.matrices_dim)
                trans = transpose.main_diagonal(self.matrices[0])
                if deter == 0:
                    print("This matrix doesn't have an inverse.\n")
                else:
                    inverse = Inverse(self.matrices, self.matrices_dim)
                    inversed = inverse.inversed(self.matrices[0], self.matrices_dim[0],trans, deter)
                    print(self.output(inversed))
            elif choice == 0:
                exit(0)


class Transpose(Matrix):
    def __init__(self, structure, dim):
        super().__init__()
        self.matrices = structure
        self.matrices_dim = dim
        self.matrix_dim = self.matrices_dim[0]
        self.i = self.matrix_dim[0]
        self.j = self.matrix_dim[1]
        self.total = int(self.i) * int(self.j)
        self.matrix = self.matrices[0]

    def main_diagonal(self, matrix):
        output_list = []
        for instance in range(int(self.i)):
            count = instance
            for individual in range(int(self.j)):
                output_list.append(matrix[count])
                count += int(self.j)
        return output_list # REMAINDER

    def side_diagonal(self, matrix):
        output_list = []
        count = self.total
        for position in range(self.total):
            count -= 1
            output_list.append(matrix[count])
        return self.main_diagonal(output_list)

    def vertical_line(self, matrix):
        output_list = []
        mat = []
        count = self.total
        for position in range(self.total):
            count -= 1
            mat.append(matrix[count])
        count = self.total - int(self.j)
        for instances in range(int(self.i)):
            for times in range(int(self.j)):
                output_list.append(mat[count])
                count += 1
            count -= 2 * int(self.j)
        return self.output(output_list)

    def horizontal_line(self, matrix):
        output_list = []
        count = self.total - int(self.j)
        for instances in range(int(self.i)):
            for times in range(int(self.j)):
                output_list.append(matrix[count])
                count += 1
            count -= 2 * int(self.j)
        return self.output(output_list)


class Determinant(Matrix):
    def __init__(self):
        self.plot = []
        self.matrix = []

    def minor(self, ij):
        plot = self.plot   # These codes can surly be optimized and even I can do it but it works
        mij = ij           # So I won't be breaking it :)
        output_list = []
        output_pos = []
        for pos in plot:
            if mij[0] not in pos[0] and mij[1] not in pos[1]:
                b = plot.index(pos)
                a = self.matrix[b]
                output_pos.append(pos)
                output_list.append(a)
        c = output_list
        output = (float(c[0]) * float(c[3])) - (float(c[1]) * float(c[2]))
        return output

    def factor(self, data, dim_data):
        self.plot = self.matrix_plot(dim_data)
        position = self.plot
        matrix = data
        self.matrix = matrix
        cij = 0
        for index in range(3):
            mij = position[index]
            i = mij[0]
            j = mij[1]
            c = ((-1) ** (int(i)+int(j))) * self.minor(mij)
            c1 = float(matrix[index]) * c
            cij = cij + c1
        return cij

    def deter(self, data, dim_data):
        matrix = data
        i = dim_data[0]
        j = dim_data[1]
        position = self.matrix_plot(dim_data)
        determinant = 0
        if i != j:
            return "ERROR"
        if int(i) == 1 and int(j) == 1:
            return matrix[0]
        if int(i) == 2 and int(j) == 2:
            output = (float(matrix[0]) * float(matrix[3])) - (float(matrix[1]) * float(matrix[2]))
            return output
        if int(i) == 3 and int(j) == 3:
            output = self.factor(matrix, dim_data)
            return output
        else:
            for ind in range(int(j)):
                mij = position[ind]
                temp_list = []
                for pos in position:
                    if mij[0] not in pos[0] and mij[1] not in pos[1]:
                        b = position.index(pos)
                        a = matrix[b]
                        temp_list.append(a)
                dim = [int(i)-1, int(j)-1]
                c = self.deter(temp_list, dim)
                d = ((-1) ** (int(mij[0])+int(mij[1])))
                e = c * d
                determinant += float(matrix[ind]) * e
            return determinant


class Inverse(Matrix):
    def __init__(self, structure, dim):
        self.plot = []
        self.matrix = []

    def minor_inverse(self, ij):
        plot = self.plot   # These codes can surly be optimized and even I can do it but it works
        mij = ij           # So I won't be breaking it :)
        output_list = []
        output_pos = []
        for pos in plot:
            if mij[0] not in pos[0] and mij[1] not in pos[1]:
                b = plot.index(pos)
                a = self.matrix[b]
                output_pos.append(pos)
                output_list.append(a)
        c = output_list
        output = (float(c[0]) * float(c[3])) - (float(c[1]) * float(c[2]))
        return output

    def factor_inverse(self, data, dim_data):
        self.plot = self.matrix_plot(dim_data)
        position = self.plot
        matrix = data
        self.matrix = matrix
        cij = 0
        for index in range(3):
            mij = position[index]
            i = mij[0]
            j = mij[1]
            c = ((-1) ** (int(i)+int(j))) * self.minor_inverse(mij)
            c1 = float(matrix[index]) * c
            cij = cij + c1
        return cij

    def invert(self, data, dim_data):
        matrix = data
        i = dim_data[0]
        j = dim_data[1]
        total = int(i) * int(j)
        output_list = []
        position = self.matrix_plot(dim_data)
        if i != j:
            return "ERROR"
        if int(i) == 3 and int(j) == 3:
            output = self.factor_inverse(matrix, dim_data)
            return output
        else:
            for index in range(int(total)):
                mij = position[index]
                temp_list = []
                for pos in position:
                    if mij[0] not in pos[0] and mij[1] not in pos[1]:
                        b = position.index(pos)
                        a = matrix[b]
                        temp_list.append(a)
                dim = [int(i)-1, int(j)-1]
                c = self.invert(temp_list, dim)
                out = ((-1) ** (int(mij[0])+int(mij[1]))) * c
                output_list.append(out)
            return output_list

    def inversed(self, data, dim, trans, deter):
        position = self.matrix_plot(dim)
        i = dim[0]
        j = dim[1]
        output_list = []
        if i == "2" and j == "2":
            out_list = [float(data[3]),  -float(data[1]), -float(data[2]), float(data[3])]
        elif i == "3" and j == "3":
            out_list = []
            self.matrix = trans
            self.plot = position
            for index in range(9):
                mij = position[index]
                output = self.minor_inverse(mij)
                d = ((-1) ** (int(mij[0])+int(mij[1]))) * output
                out_list.append(d)
        else:
            out_list = self.invert(trans, dim)
        for items in out_list:
            inverse_item = items / deter
            if inverse_item == 0:
                inverse_item = abs(inverse_item)
            output_list.append(inverse_item)
        return output_list


if __name__ == "__main__":
    run = Matrix()
    run.main()
