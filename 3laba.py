import copy
class Matrix:

	def __init__(self, mat):
		self.mat = mat

	@staticmethod
	def print(A): 
		for j in A:
			for i in j:
				print(i, end=" ")
			print()
		return ''

	@staticmethod
	def getminor(mas,q): 
		result=[]
		for r in mas[1:]:
			row=[]
			for j in range(len(r)):
				if j != q:
					row.append(r[j])
			result.append(row)
		return result

	@staticmethod
	def getdet(mas):
		n=len(mas)
		if n==2:
			return mas[0][0]*mas[1][1]-mas[0][1]*mas[1][0]
		det = 0
		sign = 1
		for i in range(n):
			det=det+sign*mas[0][i]*Matrix.getdet(Matrix.getminor(mas,i))
		sign=-sign
		return det  

	def __gt__(self, other): 
		return (Matrix.getdet(self.mat) > Matrix.getdet(other.mat))

	def __lt__(self, other):
		return (Matrix.getdet(self.mat) < Matrix.getdet(other.mat))

	def __eq__(self, other):
		return (Matrix.getdet(self.mat) == Matrix.getdet(other.mat))

	def __add__(self, other):
		A = copy.deepcopy(self.mat)
		for i in range(len(A)):
			for i2 in range(len(other.mat[i])):
				A[i][i2] = self.mat[i][i2] + other.mat[i][i2]
		return Matrix.print(A)

	def __mul__(self, other): 
		s = 0
		A = copy.deepcopy(self.mat)
		for i in range(len(A)):
			for i2 in range(len(other.mat[i])):
				for z in range(len(A[i2])):
					s = s + self.mat[i][z] * other.mat[z][i2]
					A[i][i2] = s
					s = 0
		return Matrix.print(A)

a = Matrix([[1,2],[2,1]])
b = Matrix([[2,1],[1,2]])
if a > b:
	print('a > b')

if a < b:
	print('a < b')

if a == b:
	print('a == b')

print('\nСумма матриц: ')
print(a + b)
print('Произведение матриц: ')
print(a * b)
