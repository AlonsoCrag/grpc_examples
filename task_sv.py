import grpc
import guide_pb2_grpc
import guide_pb2
from concurrent import futures
import time

class DoTaskServicer(guide_pb2_grpc.TaskMenuServicer):

    def DoTask(self, request, context):
        print("request", request)
        print("context", context)
        # time.sleep(10)
        return guide_pb2.TaskReply(task_name=request.task_name, task_number="999")


    # Response-streaming RPC where the client sends a request to the server and gets a stream to read a sequence of messages back
    def DeleteTask(self, request, context):
        print("request", request)
        print("context", context)
        # data = ["99", "2", "3", "4", "5", "6"]
        data = [
            {"task_name": "clean", "task_number": "99"},
            {"task_name": "play", "task_number": "12"},
            {"task_name": "edit", "task_number": "55"},
        ]
        for i in data:
            # print("Data", i)
            yield guide_pb2.TaskReply(task_name=i["task_name"], task_number=i["task_number"])
            time.sleep(1)

    # A bidirectionally-streaming RPC where both sides send a sequence of messages using a read-write stream
    def OvewriteTask(self, request_iterator, context):
        # Request iterator refers to the method used as parameter to call this method in the client side
        # Functions that use yield are iterable
        # The request parameter defined in the proto file can be accessed with dot notation even to the response
        print("New request", request_iterator)
        for element in request_iterator:
            print("Element", element)
            print("Element", element.task_name)
            if element.task_name == "DO":
                yield guide_pb2.TaskReply(task_name="Done", task_number="8888")
                time.sleep(1)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    guide_pb2_grpc.add_TaskMenuServicer_to_server(DoTaskServicer(), server)
    server.add_insecure_port("localhost:50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    print("Server started...")
    serve()


# The file with termination pb2_grpc.py 
# Main purpose is to create the server
# It also includes a "Stub" which will help us access and know what methods were defined for the server


# The file with termination pb2.py
# Its to get the different Requests and Replys for each method
# So co un pass the attributes with the right types


# command to create python code based in the proto file:
# python -m grpc_tools.protoc -I./protos --python_out=. --pyi_out=. --grpc_python_out=. .\protos\guide.proto