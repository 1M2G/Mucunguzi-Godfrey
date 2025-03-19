from bisect import bisect_right

class Job:
    def __init__(self, start, end, profit):
        self.start = start
        self.end = end
        self.profit = profit

def job_scheduling(start_times, end_times, profits):
    n = len(start_times)
    jobs = [Job(start_times[i], end_times[i], profits[i]) for i in range(n)]
    
    # Sort jobs by ending time
    jobs.sort(key=lambda job: job.end)
    
    # Extract job details
    ends = [job.end for job in jobs]
    
    # DP array: max profit up to job[i]
    dp = [0] * n
    
    # Base case: first job profit
    dp[0] = jobs[0].profit
    
    for i in range(1, n):
        # Profit including the current job
        include_profit = jobs[i].profit
        
        # Find the last non-overlapping job using binary search
        last_non_overlap = bisect_right(ends, jobs[i].start) - 1
        if last_non_overlap != -1:
            include_profit += dp[last_non_overlap]
        
        # Maximum profit excluding or including current job
        dp[i] = max(dp[i - 1], include_profit)

    return dp[-1]

# Example usage
start_times = [1, 2, 3, 3]
end_times = [3, 4, 5, 6]
profits = [50, 10, 40, 70]

print("Maximum Profit:", job_scheduling(start_times, end_times, profits))