from queue import PriorityQueue

class Process:
    def __init__(self, name, arrival_time, burst_time, priority):
        self.name = name
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.remaining_time = burst_time
    
    def __lt__(self, other):
        # Si tienen la misma prioridad, resolvemos el empate por SJF
        if self.priority == other.priority:
            return self.remaining_time < other.remaining_time
        else:
            return self.priority < other.priority

def priority_sjf(processes):
    ready_queue = PriorityQueue()
    waiting_queue = []
    turnaround_times = {}
    waiting_times = {}
    current_time = 0
    
    for process in processes:
        waiting_times[process.name] = 0
        turnaround_times[process.name] = 0
        ready_queue.put(process)
    
    while not ready_queue.empty() or len(waiting_queue) > 0:
        if len(waiting_queue) > 0:
            process = waiting_queue.pop(0)
            waiting_times[process.name] += current_time - process.wait_start_time
        else:
            process = ready_queue.get()
            waiting_times[process.name] += current_time - process.arrival_time
        
        current_time += process.remaining_time
        turnaround_times[process.name] += current_time - process.arrival_time
        process.remaining_time = 0
        
        for p in processes:
            if p.arrival_time > current_time or p.remaining_time == 0:
                continue
            
            if p.priority > process.priority or (p.priority == process.priority and p.remaining_time < process.remaining_time):
                p.wait_start_time = current_time
                waiting_queue.append(p)
            else:
                ready_queue.put(p)
        
    avg_waiting_time = sum(waiting_times.values()) / len(processes)
    avg_turnaround_time = sum(turnaround_times.values()) / len(processes)
    
    print(f"Average waiting time: {avg_waiting_time}")
    print(f"Average turnaround time: {avg_turnaround_time}")

# Ejemplo de uso
processes = [
    Process("P1", 0, 18, 2),
    Process("P2", 2, 16, 1),
    Process("P3", 5, 10, 2),
    Process("P4", 6, 5, 3),
    Process("P5", 7, 9, 1),
    Process("P6", 11, 7, 2),
    Process("P7", 28, 8, 1)
]

priority_sjf(processes)
