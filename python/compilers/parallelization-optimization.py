import multiprocessing as mp
import timeit

# timeit.template = """
# def inner(_it, _timer{init}):
#     from tqdm import tqdm
#     {setup}
#     _t0 = _timer()
#     for _i in tqdm(_it, total=_it.__length_hint__()):
#         {stmt}
#     _t1 = _timer()
#     return _t1 - _t0
# """

def sum_of_squares(numbers):
    return sum([num * num for num in numbers])

def sum_of_squares_parallel(numbers):
    # use all available cores
    num_processes = mp.cpu_count()
    chunk_size = len(numbers) // num_processes
    # create pool of processes
    pool = mp.Pool(processes=num_processes)
    # divide work into chunks
    chunks = [numbers[i:i + chunk_size] for i in range(0, len(numbers), chunk_size)]
    results = pool.map(sum_of_squares, chunks)
    # close
    pool.close()
    # combine results
    pool.join()

    return sum(results)

if __name__ == '__main__':
    assert sum_of_squares(list(range(1, 10000))) == sum_of_squares_parallel(list(range(1, 10000)))
    # timeit
    n = list(range(1, 10000000))
    print(f"sum_of_squares: {timeit.timeit(lambda: sum_of_squares(n), number=10)}")
    # sum_of_squares: 7.48474136996083
    print(f"sum_of_squares_parallel: {timeit.timeit(lambda: sum_of_squares_parallel(n), number=10)}")
    # sum_of_squares_parallel: 6.641842097043991
