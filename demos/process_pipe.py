"""
use pipe to exchange data between parent process and child process
"""
import pickle
import multiprocessing


def send_data(pipe):
    data = {'key': 'value'}
    pipe.send(pickle.dumps(data))

if __name__ == "__main__":
    parent_pipe, child_pipe = multiprocessing.Pipe()

    p = multiprocessing.Process(target = send_data, args = (child_pipe,))
    p.start()
    p.join()

    received_data = pickle.loads(parent_pipe.recv())
    print(received_data)