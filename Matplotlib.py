import matplotlib.pyplot as plt
import matplotlib.markers
import numpy as np

lst1 = [3,5,7,9,11]
lst2 = [10,20,20,10,50]

# 1. Plotting a line graph
x_axis = np.array(lst1)
y_axis = np.array(lst2)
"""
plt.plot(x_axis, y_axis)
plt.show()


# 2. Plotting just points in a graph - scatter plot
plt.plot(x_axis, y_axis, 'o')
plt.show()

# 3. Considering default values for x
plt.plot(y_axis)
plt.show()

# 4. Marking points on a line graph with marker. marker can 1 char. 'o' puts a dot. '+'/'*' shows a + or a *. Look at doc for more options 
plt.plot(x_axis, y_axis, marker='d')
plt.show()

# clear the plot area
plt.close()

# 5. Marking points on a line graph with marker. using colors. ms is the size, mec is the color used around the point, mfc is the color of the marker
# ls is the linestyle, c is for the color parameter, lw is line width
plt.plot(x_axis, y_axis, marker='o', ms=16, mec='r', mfc='g', c='r', ls=':',lw=6)
plt.show()

# 6. Showing multiple lines in the chart
plt.close()
fline = np.array([3,5,2,7])
sline = np.array((4,2,6,8))
plt.plot(fline, c='r')
plt.plot(sline, c='g')
plt.show()

# 7. Adding labels and titles to the chart
plt.close()
x_axis = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
y_axis = np.array([20, 25, 35, 50, 65, 60, 60, 55, 50, 45])
plt.plot(x_axis, y_axis)
plt.title('Age vs Weight')
plt.xlabel('Age')
plt.ylabel('Weight')
plt.show()

# 8. Adding font styles labels and titles to the chart
plt.close()
x_axis = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
y_axis = np.array([20, 25, 35, 50, 65, 60, 60, 55, 50, 45])
font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}
plt.plot(x_axis, y_axis)
plt.title('Age vs Weight', fontdict=font1, loc='right')
plt.xlabel('Age', fontdict=font2)
plt.ylabel('Weight', fontdict=font2)
plt.show()

# 9. Adding grid lines. Default, grid on both x and y axis. Use parameter axis='x/y' for specifics
plt.close()
x_axis = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
y_axis = np.array([20, 25, 35, 50, 65, 60, 60, 55, 50, 45])
font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}
plt.plot(x_axis, y_axis)
plt.title('Age vs Weight', fontdict=font1, loc='right')
plt.xlabel('Age', fontdict=font2)
plt.ylabel('Weight', fontdict=font2)
plt.grid(c='r',lw=0.5, ls=':')
plt.show()

#10. Using subplot to have more graphs. 3 params - 1 no. of rows, 2 no. of cols, 3 the index starting from 1
plt.close()
font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}
plt.subplot(2,2,1)
plt.plot(x_axis, y_axis)
plt.subplot(2,2,2)
plt.plot(x_axis, y_axis)
plt.subplot(2,2,3)
plt.plot(x_axis, y_axis)
plt.subplot(2,2,4)
plt.plot(x_axis, y_axis)
plt.suptitle('Multiple Charts', fontdict=font1)
plt.show()

#11. Scatter charts
plt.close()
plt.subplot(2,2,1)
plt.plot(x_axis, y_axis)
plt.subplot(2,2,2)
plt.plot(x_axis, y_axis)
plt.subplot(2,2,3)
plt.plot(x_axis, y_axis)
plt.subplot(2,2,4)
plt.scatter(x_axis, y_axis)
plt.suptitle('Multiple Charts')
plt.show()


#12. Colorful scatter charts
plt.close()
colors = np.array(["red","green","blue","yellow","pink"])
plt.scatter(x_axis, y_axis, c=colors)
plt.show()

#13. Colorful scatter charts using colormaps, with size and transparency
plt.close()
colors = np.array([10,20,30,40,50])
sizes = np.array([5,10,5,45,10])
plt.scatter(x_axis, y_axis, c=colors, cmap='viridis', s=sizes, alpha=0.75)
plt.colorbar()
plt.show()

"""
#14. Bar graphs vertical
plt.close()
dept = np.array(('Admin', 'HR', 'Finance', 'IT', 'Transport', 'Travel'))
memcount = np.array([18, 23, 14, 32, 21, 7])
colors = ['red','blue','green','black','grey','yellow']
plt.bar(dept, memcount, color=colors)
plt.title("Member Count")
plt.xlabel("Departments")
plt.ylabel("Counts")
plt.show()

"""
#15. Bar graphs (horizontal)
plt.close()
plt.barh(dept, memcount)
# plt.show()

#16. Bar graphs with more styles
plt.close()
hatches=['/','+','-','*','|','o']
colors =["red","green","blue","yellow","pink","orange"]
plt.bar(dept, memcount, width=0.75, color=colors, fill=True, hatch=hatches)
plt.title("Member Count",fontdict=font1)
plt.xlabel("Departments",fontdict=font2)
plt.ylabel("Counts",fontdict=font2)
# plt.show()

#17. Histograms
plt.close()
x = np.random.normal(50, 10, 500)
plt.hist(x)
#plt.show()

#18. Pie charts
x = np.array((30,20,40,10,50))
mylabels = ['apples', 'oranges', 'bananas', 'kiwis', 'mangos']
plt.pie(x, labels=mylabels)
# plt.show()

#19. Exploded Pie charts
x = np.array((30,20,40,10,50))
mylabels = ['apples', 'oranges', 'bananas', 'kiwis', 'mangos']
myexplode = [0, 0.2, 0, 0.2, 0]
plt.pie(x, labels=mylabels, explode=myexplode)
#plt.show()

"""