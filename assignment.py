# area of square 
#Area of a square = Side × Side = S2

# area of circle
# A = π r²

# are of cylinder
#A = 2 π r h + 2 π r 2

#percentage


def area_of_square(side):
    return side*side

results = area_of_square(10)
print(results)

def area_of_circle(radius):
    return 3.14 * radius*radius

result = round(area_of_circle(10))
print(result)

def area_of_cylinder(radiuss, height):
    return 2 * 3.14 * radiuss * height + 2 * 3.14 * radiuss * radiuss

a = round(area_of_cylinder(5,7))
print(a)

def calculating_percentage(obtained_marks, total_marks):
    percentage = (obtained_marks/total_marks) * 100
    return percentage

b = calculating_percentage(250,500)
print(b,"%")