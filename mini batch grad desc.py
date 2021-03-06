import random ##

inp = open('data', 'r')
data = inp.readlines()
data[:] = (value for value in data if value != '\n')

#no need to change this 
def compute_errors_for_line_given_points(b,m,points):
    totalError = 0
    for i in range(0,len(points)):   #points => data
        x = float(points[i][0].strip('\t'))
        y = float(points[i][1].strip('\n'))
        totalError += (y - (m*x + b))**2

    return totalError/float(len(points))

#CHANGE MAYBE
def step_gradient(b_current, m_current, points, learningRate):
    b_gradient = 0
    m_gradient = 0
    N = float(len(points))
    for i in range(0, len(points)):
        x = float(points[i][0].strip('\t'))
        y = float(points[i][1].strip('|n'))
        
        b_gradient += -(2/N)*(y-((m_current*x)+b_current))
        m_gradient += -(2/N)*x*(y-((m_current*x)+b_current))
    new_b = b_current - (learningRate * b_gradient)
    new_m = m_current - (learningRate * m_gradient)
    '''print new_b
    print new_m'''
    return [new_b, new_m]
#CHANGE SURELY 
def gradient_descent_runner(points, starting_b, starting_m, learning_rate, num_iterations):
    b = starting_b
    m = starting_m
    num_iterations = 1000#num_iterations = [DEFINE IT FOR MINI BATCH GD]#
    
    for i in range(num_iterations):
        array_batch = []
        
        '''A randomizer to get mini batches in each step
        Here we need to pick from 'points' 
    '''
        points_len = len(points)
        for x in range(10): #creating a batch 
            ran_no = random.randint(0,points_len)
            temp_point = points[ran_no-1]
            array_batch.append(temp_point)
            
        b,m = step_gradient(b,m, array_batch, learning_rate)
        var = compute_errors_for_line_given_points(b,m,points)
        print var

    return [b,m]
#change min 
def run():
    points = data
    learning_rate = 0.0001
    initial_b = 0
    initial_m = 0
    num_iterations = 1000
    [b,m] = gradient_descent_runner(points, initial_b, initial_m, learning_rate, num_iterations)
    print [b,m]
    var = compute_errors_for_line_given_points(b,m,points)
    
if __name__ == '__main__':
    run()

