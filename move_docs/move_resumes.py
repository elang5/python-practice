import os 

dir = '/Users/elangreen/Downloads'
list = os.listdir(dir)

def main(): 
  for filename in list:
    if 'Resume' in filename:
      dst = '/Users/elangreen/Documents/Resume/'
      curr_file = dir + '/' + filename
      print(curr_file)
      os.rename(curr_file, dst + '/' + filename) 

main()