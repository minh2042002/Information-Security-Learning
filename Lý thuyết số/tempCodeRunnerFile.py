def find_primitive_root(N):
#     Z = []
#     for i in range(1, N):
#         if euclid(1, N) == 1:
#             Z.append(i)
#     S = []
#     for i in Z:
#         for j in Z:
#             if modular_exponent(i, j, N) == 1:
#                 if j == len(Z):
#                     S.append(i)
#                 break
    
#     return S, len(S)