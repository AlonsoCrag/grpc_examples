import grpc
import guide_pb2_grpc
import guide_pb2
import time

def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = guide_pb2_grpc.TaskMenuStub(channel)

        # response = stub.DoTask(guide_pb2.TaskRequest(task_name="Wash the dishes"))


        # for element in stub.DeleteTask(guide_pb2.TaskRequest(task_name="Please delete all tasks...")):
        #     print("Response...", element)


        def sendStreamData():
            data = [
            {"task_name": "DO"},
            {"task_name": "play"},
            {"task_name": "DO"},
            ]
            for i in data:
                yield guide_pb2.TaskRequest(task_name=i["task_name"])
                time.sleep(1)

        for element in stub.OvewriteTask(sendStreamData()):
            print("Response...", element)

        # Remember that what is being streamed is the request parameter
        # Remember that what is being streamed is the response
        # Not the rpc method

        # The request parameter defined in the proto file can be accessed with dot notation even to the response


        # How do you stream data? by collecting it using yield

if __name__ == "__main__":
    run()