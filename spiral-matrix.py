class Solution:
    # Directions
#     def spiralOrder(self, matrix):
#         def rfe(array):
#             return array[1:]
#         height = len(matrix)
#         width = len(matrix[0])
#         directions = {'right': 0, 'left': len(matrix)-1, 'down': len(matrix[0])-1, 'up': 0}
#         current_direction = 'right'
#         result = []
#         while directions['left'] > directions['right']:
#             if current_direction == 'right':
#                 result.extend(rfe([matrix[directions['right']][j] 
#                                for j in 
#                                range(directions['right'],width - directions['right'] )
#                               ]))
#                 directions['right'] += 1
#                 current_direction = 'down'
#             elif current_direction == 'down':
#                 result.extend(rfe([matrix[row][directions['down']] 
#                                for row in 
#                                range(height-(directions['down']+1),directions['down']+1)
#                               ]))
#                 directions['down'] -= 1
#                 current_direction = 'left'
#                 break
#             elif current_direction == 'left':
#                 result.extend(rfe([matrix[directions['left']][j] 
#                                for j in 
#                                range(width-)
#                               ]))
#                 directions['right'] += 1
#                 current_direction = 'down'
# #             elif current_direction == 'up':
                  
#         return result
    def spiralOrder(self, matrix):
        height = len(matrix)
        if not height:
            return []
        width = len(matrix[0])
        borders = {'up': 0, 'left': 0, 'down': height-1, 'right': width-1}
        current_direction = 'right'
        result = []
        while borders['down'] >= borders['up'] and borders['right'] >= borders['left']:
            if current_direction == 'right':
                result.extend([matrix[borders['up']][j] 
                               for j in 
                               range(borders['left'], borders['right']+1)
                              ])
                borders['up'] += 1
                current_direction = 'down'
            elif current_direction == 'down':
                result.extend([matrix[i][borders['right']] 
                               for i in 
                               range(borders['up'], borders['down']+1)
                              ])
                borders['right'] -= 1
                current_direction = 'left'
            elif current_direction == 'left':
                result.extend([matrix[borders['down']][j] 
                              for j in
                              range(borders['right'], borders['left']-1,-1)
                              ])
                borders['down'] -= 1
                current_direction = 'up'
            elif current_direction == 'up':
                result.extend([matrix[i][borders['left']] for i in range(borders['down'], borders['up']-1,-1)])
                borders['left'] += 1
                current_direction = 'right'
        return result

sol = Solution()
print(sol.spiralOrder([[7],[9],[6]]))
