import os,time
from flask import Flask, render_template,request
from flask_jsonpify import jsonify
from timeit import default_timer as timer


app = Flask(__name__)

def bubble_sort(nums):
	start= timer()
	for i in range(len(nums)):
		for j in range(0,len(nums)-i-1):
				if(nums[j]>nums[j+1]):
					nums[j],nums[j+1]=nums[j+1],nums[j]
	end = timer()
	print("The time taken for bubble_sort is {}".format(end-start))
	return nums
def insertion_sort(arr):
	start = timer()
	for i in range(1, len(arr)):
		key = arr[i]
		# Move elements of arr[0..i-1], that are
		# greater than key, to one position ahead
		# of their current position
		j = i-1
		while j >=0 and key < arr[j] :
			arr[j+1] = arr[j]
			j -= 1
		arr[j+1] = key
	end = timer()
	print("The time taken for insertion_sort is {}".format(end-start))
	return arr

@app.route('/')
def index():
	return render_template('hello.html')
@app.route('/chart')
def chart():
	return render_template("chart.html")


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)
@app.route('/api',methods=['POST','GET'])
def sort():
	lis = request.get_json(force=True)
	#app.logger.info("The lis is a list {} ".format(lis))
	if(lis):
		lis = [int(x) for x in lis.split(',')]
		start = time.time()
		nums = bubble_sort(lis)
		num1 = insertion_sort(lis)
		performance = round((time.time()-start),3)
		#nums.append(performance)
		#app.logger.info("The sorted list is {}".format(insertion_sort(lis)))
		#app.logger.info("The performance is {}".format(performance))
		#app.logger.info("The lis is {} and type is {}".format(nums,type(nums)))
		
		return jsonify(nums)
	else:
		return jsonify("List is empty ")


if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.debug = True
    port = int(os.environ.get('PORT', 5002))
    app.run(host='0.0.0.0', port=port)
