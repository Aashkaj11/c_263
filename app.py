from flask import Flask,render_template,request
app=Flask(__name__)

#Define visitor function to check how many visitor are there
@app.route('/')
def visitors():

    counter_read_file = open("count.txt", "r")
    visitors_count = int(counter_read_file.read())
    counter_read_file.close()

    visitors_count = visitors_count + 1

    counter_write_file = open("count.txt", "w")
    counter_write_file.write(str(visitors_count))
    counter_write_file.close()
    return render_template('index.html',count=visitors_count)
@app.route('/',methods=['POST'])
def weather_stats():
    # Load current count
    counter_read_file = open("count.txt", "r")
    visitors_count = int(counter_read_file.read())
    counter_read_file.close()
    text=request.form['text']
    formula_data='https://covidstats-sdbd.onrender.com/?country='+text
    print(formula_data)
    return render_template('index.html',image=formula_data,count=visitors_count)


#add code for executing flask
if __name__ == "__main__":
    app.run()
