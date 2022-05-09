if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    if query_name in student_marks:
        display = list(student_marks[query_name]) 
        p=sum(display)/len(display);
        print("%.2f" % p);

        
