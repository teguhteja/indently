import sample_module

def get_sample_world() -> dict:
    return 'The World'

if __name__ == '__main__':
    print('Before:',sample_module.get_hello())
    sample_module.get_hello = get_sample_world
    print('After: ',sample_module.get_hello())
