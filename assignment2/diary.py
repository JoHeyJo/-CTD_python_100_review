import traceback
def log_response():
    response = input("What happened today? ")
    try:
        while response:
            with open('diary.txt', 'a') as file:
                if response == "done for now":
                    file.write(f"{response}")
                    return
                else:
                    file.write(f'{response} \n')
                    response = input("What else? ")
    except Exception as e:
            trace_back = traceback.extract_tb(e.__traceback__)
            stack_trace = list()
            for trace in trace_back:
               stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
            print(f"Exception type: {type(e).__name__}")
            message = str(e)
            if message:
               print(f"Exception message: {message}")
            print(f"Stack trace: {stack_trace}")

log_response()