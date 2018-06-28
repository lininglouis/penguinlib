import os

def list_full_path(dirPath):
	file_paths = []
	for f in os.listdir(dirPath):
		file_paths.append(os.path.join(dirPath,f))
	return file_paths

def list_all_files_recursively(dirPath):
	file_paths = []
	for root, dirs, files in os.walk(dirPath, topdown=False):
		for name in files:
			file_paths.append(os.path.join(root, name))
	return file_paths


def mkdir_if_not_exists(dirPath):
	if not os.path.exists(dirPath):
		os.makedirs(dirPath)
