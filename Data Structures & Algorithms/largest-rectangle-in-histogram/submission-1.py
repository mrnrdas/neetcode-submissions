class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Store the max area
        max_area = 0
        # Initialize the stack
        stack = [] # pair: (index, height)
        
        # Iterate through each bar in the histogram
        for i, h in enumerate(heights):
            # Initialize the start index of the rectangle
            start = i
            # While stack is not empty and the bar at the stacks top has a greater height than the current bar
            while stack and stack[-1][1] > h:
                # Pop the top of the stack
                index, height = stack.pop()
                # Calculate the area with the popped bar as the smallest (or limiting) height
                max_area = max(max_area, height * (i - index))
                # Update the start index to the popped index
                start = index
            
            # Push the current bar onto the stack
            stack.append((start, h))

        # After going through all bars, clear the stack and calculate area for remaining bars
        for i, h in stack:
            # Calculate the area with the height of the remaining bars and width until the end of the histogram
            max_area = max(max_area, h * (len(heights) - i))

        # Return the maximum area found
        return max_area
