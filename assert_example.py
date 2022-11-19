def start_program(data: dict):
    assert isinstance(data, dict), 'invalid JSON'
    assert data, 'No data foud'

    print('Loaded successfully')

if __name__ == '__main__':
    json = {'user': 123}
    start_program(data=json)
    print(__debug__)