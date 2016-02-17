import time
#Store Program Execution time in a variable
start_time = time.time()

#run the main function in the trial1.py module
import trial1
for i in range(0,50):
    trial1.main()
end_time = time.time()
print "Time = %s" %(end_time-start_time)
print "Average = %s" %((end_time-start_time)/50)
