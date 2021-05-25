def func1(input, func = None):
  func = func or func1
  print(f'func1 called with {input}')

  if input == 1:
    return

  func(input - 1)

def func2(input):
  print(f'func2 called with {input}')
  func1(input, func2)

func1(3)
print('------')
func2(3)

