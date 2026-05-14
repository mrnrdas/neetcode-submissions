class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Initialize result array
        res = []

        # Iterate through existing intervals
        for i in range(len(intervals)):
            
            # Case 1: No overlap, newInterval ends before the current interval starts
            if newInterval[1] < intervals[i][0]:
                # Append the newInterval to the result as it doesn't overlap
                res.append(newInterval)

                # Return the result list combined with the remaining intervals
                return res + intervals[i:]

            # Case 2: No overlap, newInterval starts after the current interval ends
            elif newInterval[0] > intervals[i][1]:
                # Add the current interval to the result as it doesn't overlap
                res.append(intervals[i])
            
            # Case 3: Overlap exists between newInterval and current interval
            else:
                # Merge the overlapping intervals by updating newInterval
                # Start of the merged interval is the minimum start time
                # End of the merged interval is the maximum end time
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1])
                ]

        # After processing all intervals, add the remaining newInterval
        # If it wasn't added in Case 1, it needs to be added here
        res.append(newInterval)

        # Return the result list
        return res