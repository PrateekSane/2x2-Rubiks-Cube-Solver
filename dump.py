def second_bfs(self):
    cur_root = self.moveQueue.get()

    if cur_root == self.cube.solved_array:
        print('solution found')
        return self.cube.current
    elif cur_root:
        temp = cur_root[:]

        for i in range(len(self.actions)):
            res = self.actions[i](temp)
            res_string = ''.join(res)
            self.visited[res_string] = 1
            if self.visited[res_string] >= 2:
                continue
            else:
                self.moveQueue.put(res)
                self.visited[res_string] += 1
        self.total_moves += 1
        self.start_bfs()

    else:
        print('solution not found and queue is empty')




    self.cube.current = self.cube.front(self.cube.current)
    self.cube.current = self.cube.right(self.cube.current)
    self.cube.current = self.cube.back(self.cube.current)
    self.cube.current = self.cube.front_prime(self.cube.current)

python solver.py