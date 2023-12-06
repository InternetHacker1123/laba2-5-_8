#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    A = tuple(map(int, input().split()))
    if len(A) < 3:
        print("Слишком маленькая длина кортежа", file=sys.stderr)
        exit(1)

    for i in range(len(A) - 2):
        if A[i+1] > A[i] and A[i+1] > A[i+2]:
            print(i, i+1, i+2)
            break
    else:
        print("Ничего не нашлось")