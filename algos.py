import time
from time import sleep

def bubble_sort(data, draw, speed):
    for _ in range(len(data)-1):
        for j in range(len(data)-1):
            # Colours elements which currently are being compared
            draw(data, ['yellow' if x==j or x==j+1 else 'red' for x in range(len(data))])
            time.sleep(0.4)
            if data[j] > data[j+1]:
                data[j+1],data[j]=data[j],data[j+1]
                # Colours elements which were swapped after being compared based on the logic
                draw(data, ['yellow' if x==j or x==j+1 else 'red' for x in range(len(data))])
                time.sleep(speed)
    # Colours entire yellow on success sorting of the list
    draw(data, ['yellow' for _ in range(len(data))])


def insertion_sort(data, draw, speed): 
    for i in range(1, len(data)): 
  
        key = data[i]
        j = i-1
        draw(data, ['yellow' if x==i else 'red' for x in range(len(data))])
        while j >=0 and key < data[j] :
                data[j+1] = data[j]
                j -= 1
                draw(data,['yellow' if x==i or x==j else 'red' for x in range(len(data))])
                time.sleep(speed)
        #draw(data,['yellow' if x==i or x==j+1 or x==data.index(key) else 'red' for x in range(len(data))])
        data[j+1] = key
        draw(data, ['yellow' if x==data.index(key) or x==j else 'red' for x in range(len(data))])
        time.sleep(speed)
    draw(data, ['yellow' for x in data])


def selection_sort(data, draw, speed):
    for i in range(len(data)): 
        min_idx = i
        draw(data, ['yellow' if x==min_idx else 'red' for x in range(len(data))])
        for j in range(i+1, len(data)):
            draw(data, ['yellow' if x==min_idx or x==j else 'red' for x in range(len(data))])
            if data[min_idx] > data[j]: 
                min_idx = j
                draw(data, ['yellow' if x==min_idx or x==j else 'red' for x in range(len(data))])
                time.sleep(speed)
            time.sleep(speed)
                
        data[i], data[min_idx] = data[min_idx], data[i]
        draw(data, ['yellow' if x==min_idx or x==i else 'red' for x in range(len(data))])
        time.sleep(speed)
    draw(data,['yellow' for x in range(len(data))])
  