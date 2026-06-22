def hanoi_solver(n):
    source = list(range(n, 0, -1))
    auxiliary = []
    target = []

    states = [f"{source} {auxiliary} {target}"]

    def move(disks, start, end, temp):
        if disks == 1:
            end.append(start.pop())
            states.append(f"{source} {auxiliary} {target}")
        else:
            move(disks - 1, start, temp, end)
            end.append(start.pop())
            states.append(f"{source} {auxiliary} {target}")
            move(disks - 1, temp, end, start)

    move(n, source, target, auxiliary)

    return "\n".join(states)
