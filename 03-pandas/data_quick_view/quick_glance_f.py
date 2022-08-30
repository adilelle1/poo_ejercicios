from tabulate import tabulate


def file_quick_glance(data):
    print(f'SHAPE:\n\n{data.shape}')
    print(f'------------------\n')
    print(f'COLUMNS:\n\n{data.columns}')
    print(f'------------------\n')
    print(f'COLUMNS DATA TYPE:\n\n{data.dtypes}')
    print(f'------------------\n')
    print(f'DESCRIBE:\n\n{data.describe()}')
    print(f'------------------\n')
    print(f'COUNT:\n\n{data.count()}')
    print(f'------------------\n')
    print(f'2 ROW SAMPLE:\n\n{data.sample(2)}')
    print(f'------------------\n')

