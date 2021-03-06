import numpy as np
import random

def front_anti_clockwise(front_face, right_face, back_face, left_face, up_face, down_face):
	anti_rotated_front_face = np.rot90(front_face)

	temp_face = np.zeros([3, 3], dtype = str)
	temp_face[:] = down_face[:]
	temp_face[0,0], temp_face[0,2] = temp_face[0,2], temp_face[0,0]
	down_face[0, :], left_face[:, 2], up_face[2, :], right_face[:, 0]  =  left_face[:, 2], up_face[2, :], right_face[:, 0], temp_face[0, :]
	return(anti_rotated_front_face, right_face, back_face, left_face, up_face, down_face)

def front_clockwise(front_face, right_face, back_face, left_face, up_face, down_face):
	rotated_front_face = np.rot90(front_face, -1)

	temp_face = np.zeros([3,3], dtype = str)
	temp_face[:] = right_face[:]
	temp_face[0,0], temp_face[2,0] = temp_face[2,0], temp_face[0,0]
	right_face[:, 0], up_face[2, :], left_face[:, 2], down_face[0, :] =  up_face[2, :], left_face[:, 2], down_face[0, :], temp_face[:, 0]
	return(rotated_front_face, right_face, back_face, left_face, up_face, down_face)

def right_clockwise(front_face, right_face, back_face, left_face, up_face, down_face):
	rotated_right_face = np.rot90(right_face, -1)

	temp_face = np.zeros([3,3], dtype = str)
	temp_face[:] = up_face[:]
	temp_face[0,2], temp_face[2,2] = temp_face[2,2], temp_face[0,2]
	back_face[0,0], back_face[2,0] = back_face[2,0], back_face[0,0]
	up_face[:,2], front_face[:,2], down_face[:,2], back_face[:,0] = front_face[:,2], down_face[:,2], back_face[:,0], temp_face[:,2]
	return(front_face, rotated_right_face, back_face, left_face, up_face, down_face)

def right_anti_clockwise(front_face, right_face, back_face, left_face, up_face, down_face):
	rotated_right_face = np.rot90(right_face, 1)

	temp_face = np.zeros([3,3], dtype = str)
	temp_face[:] = up_face[:]
	back_face[0,0], back_face[2,0] = back_face[2,0], back_face[0,0]
	down_face[0,2], down_face[2,2] = down_face[2,2], down_face[0,2]
	up_face[:,2], back_face[:,0], down_face[:,2], front_face[:,2] = back_face[:,0], down_face[:,2], front_face[:,2], temp_face[:,2]
	return(front_face, rotated_right_face, back_face, left_face, up_face, down_face)

def left_clockwise(front_face, right_face, back_face, left_face, up_face, down_face):
	rotated_left_face = np.rot90(left_face, -1)
	temp_face = np.zeros([3,3], dtype = str)
	temp_face[:] = back_face[:]
	temp_face[0,2], temp_face[2,2] = temp_face[2,2], temp_face[0,2]
	down_face[0,0], down_face[2,0] = down_face[2,0], down_face[0,0]
	back_face[:,2], down_face[:,0], front_face[:, 0],up_face[:,0] = down_face[:,0], front_face[:, 0], up_face[:,0],temp_face[:,2]
	return(front_face, right_face, back_face, rotated_left_face, up_face, down_face)

def left_anti_clockwise(front_face, right_face, back_face, left_face, up_face, down_face):
	rotated_left_face = np.rot90(left_face, 1)
	temp_face = np.zeros([3,3], dtype = str)
	temp_face[:] = back_face[:]
	temp_face[0,2], temp_face[2,2] = temp_face[2,2], temp_face[0,2]
	up_face[0,0], up_face[2,0] = up_face[2,0], up_face[0,0]
	back_face[:,2], up_face[:,0], front_face[:, 0],down_face[:,0] = up_face[:,0], front_face[:, 0], down_face[:,0],temp_face[:,2]
	return(front_face, right_face, back_face, rotated_left_face, up_face, down_face)

def back_clockwise(front_face, right_face, back_face, left_face, up_face, down_face):
	rotated_back_face = np.rot90(back_face, -1)
	temp_face = np.zeros([3,3], dtype = str)
	temp_face[:] = up_face[:]
	temp_face[0,0], temp_face[0,2] = temp_face[0,2], temp_face[0,0]
	down_face[2,0], down_face[2,2] = down_face[2,2], down_face[2,0]
	up_face[0,:], right_face[:,2],down_face[2,:],left_face[:,0] = right_face[:,2], down_face[2, :], left_face[:,0],temp_face[0,:]
	return(front_face, right_face, rotated_back_face, left_face, up_face, down_face)

def back_anti_clockwise(front_face, right_face, back_face, left_face, up_face, down_face):
	rotated_back_face = np.rot90(back_face, 1)
	temp_face = np.zeros([3,3], dtype = str)
	temp_face[:] = up_face[:]
	left_face[0,0], left_face[2,0] = left_face[2,0], left_face[0,0]
	right_face[0,2], right_face[2,2] = right_face[2,2], right_face[0,2]
	up_face[0,:], left_face[:,0], down_face[2,:],right_face[:,2] = left_face[:,0], down_face[2,:], right_face[:,2],temp_face[0,:]
	return(front_face, right_face, rotated_back_face, left_face, up_face, down_face)

def up_clockwise(front_face, right_face, back_face, left_face, up_face, down_face):
	rotated_up_face = np.rot90(up_face, -1)
	temp_face = np.zeros([3,3], dtype = str)
	temp_face[:] = front_face[:]
	front_face[0,:], right_face[0,:], back_face[0,:],left_face[0,:] = right_face[0,:], back_face[0,:], left_face[0,:],temp_face[0,:]
	return(front_face, right_face, back_face, left_face, rotated_up_face, down_face)

def up_anti_clockwise(front_face, right_face, back_face, left_face, up_face, down_face):
	rotated_up_face = np.rot90(up_face, 1)
	temp_face = np.zeros([3,3], dtype = str)
	temp_face[:] = front_face[:]
	front_face[0,:], left_face[0,:], back_face[0,:],right_face[0,:] = left_face[0,:], back_face[0,:], right_face[0,:],temp_face[0,:]
	return(front_face, right_face, back_face, left_face, rotated_up_face, down_face)

def down_clockwise(front_face, right_face, back_face, left_face, up_face, down_face):
	rotated_down_face = np.rot90(down_face, -1)
	temp_face = np.zeros([3,3], dtype = str)
	temp_face[:] = front_face[:]
	front_face[2,:], left_face[2,:], back_face[2,:],right_face[2,:]= left_face[2,:], back_face[2,:], right_face[2,:],temp_face[2,:]
	return(front_face, right_face, back_face, left_face, up_face, rotated_down_face)

def down_anti_clockwise(front_face, right_face, back_face, left_face, up_face, down_face):
	rotated_down_face = np.rot90(down_face, 1)
	temp_face = np.zeros([3,3], dtype = str)
	temp_face[:] = front_face[:]
	front_face[2,:], right_face[2,:], back_face[2,:],left_face[2,:]  = right_face[2,:], back_face[2,:], left_face[2,:],temp_face[2,:]
	return(front_face, right_face, back_face, left_face, up_face, rotated_down_face)

if __name__ == '__main__':
	rubix_array = np.zeros([6,9], dtype = str)
	# color_array = ['W','G','Y','R','B','O']
	# for faces in range(0,6):
	# 	for pieces in range(0,9):
	# 		rubix_array[faces][pieces] = color_array[random.randrange(1,6)]
	rubix_array = [
		['G','Y','W','B','W','Y','B','R','W'],
		['B','G','W','R','R','B','R','R','R'],
		['R','G','O','W','Y','Y','B','O','Y'],
		['G','R','Y','G','O','Y','G','W','Y'],
		['W','O','B','G','B','W','O','O','O'],
		['O','B','G','O','G','W','R','B','Y']
	]
	print("Orgial Scrambled Cube")
	print(np.reshape(rubix_array, (6,9)))
	front_face = np.reshape(rubix_array[0], (3, 3))
	right_face = np.reshape(rubix_array[1], (3, 3))
	back_face = np.reshape(rubix_array[2], (3, 3))
	left_face = np.reshape(rubix_array[3], (3, 3))
	up_face = np.reshape(rubix_array[4], (3, 3))
	down_face = np.reshape(rubix_array[5], (3, 3))
	# print("Face rotate anti-clockwise F'")
	# print(np.reshape(front_anti_clockwise(front_face, right_face, back_face, left_face, up_face, down_face), (6, 9)))
	# print("Face rotate clockwise F")
	# print(np.reshape(front_clockwise(front_face, right_face, back_face, left_face, up_face, down_face),(6, 9)))
	# print("Right rotate clockwise R")
	# print(np.reshape(right_clockwise(front_face, right_face, back_face, left_face, up_face, down_face),(6, 9)))
	# print("Right rotate anti clockwise R'")
	# print(np.reshape(right_anti_clockwise(front_face, right_face, back_face, left_face, up_face, down_face),(6, 9)))
	# print("Left rotate clockwise L")
	# print(np.reshape(left_clockwise(front_face, right_face, back_face, left_face, up_face, down_face),(6, 9)))
	# print("Left rotate anti clockwise L'")
	# print(np.reshape(left_anti_clockwise(front_face, right_face, back_face, left_face, up_face, down_face),(6, 9)))
	# print("Back rotate clockwise B")
	# print(np.reshape(back_clockwise(front_face, right_face, back_face, left_face, up_face, down_face),(6, 9)))
	# print("Back rotate anti clockwise B'")
	# print(np.reshape(back_anti_clockwise(front_face, right_face, back_face, left_face, up_face, down_face),(6, 9)))
	# print("Up rotate clockwise U")
	# print(np.reshape(up_clockwise(front_face, right_face, back_face, left_face, up_face, down_face),(6, 9)))
	# print("Up rotate anti clockwise U'")
	# print(np.reshape(up_anti_clockwise(front_face, right_face, back_face, left_face, up_face, down_face),(6, 9)))
	# print("Down rotate clockwise D")
	# print(np.reshape(down_clockwise(front_face, right_face, back_face, left_face, up_face, down_face),(6, 9)))
	# print("Down rotate anti clockwise D'")
	# print(np.reshape(down_anti_clockwise(front_face, right_face, back_face, left_face, up_face, down_face),(6, 9)))