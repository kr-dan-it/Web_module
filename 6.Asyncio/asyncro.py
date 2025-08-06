import asyncio
import time
import datetime
import random
import aiohttp

# # executor
# async def say_hello():
#     print("Hello")
#
# # main process
# async def main():
#     await say_hello()
#
# if __name__ == "__main__":
#     asyncio.run(main())
#
# # time.sleep() #sync
# # await asyncio.sleep()
# asyncio.create_task()

# async def perform_io_task(task_id, duration):
#     print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] Task id: {task_id}: Start execution on {duration} sec.")
#     await asyncio.sleep(duration)
#     print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] Task id: {task_id}: End performance.")
#     return f"Task_id: {task_id}"
#
# async def main_process():
#     print("-" * 30)
#     print("With gather")
#     start_time = time.perf_counter()
#
#     result = await asyncio.gather(
#         perform_io_task(1, 2),
#         perform_io_task(2, 10),
#         perform_io_task(3, 4)
#     )
#
#     end_time = time.perf_counter()
#     print(f"Total time spent: {end_time - start_time:.3f}")
#
#     print(f"Result: {result}")

# async def main_process_split():
#     print("-" * 30)
#     print("Without gather")
#     start_time = time.perf_counter()
#
#     result=[]
#
#     result.append(await perform_io_task(1, 2)),
#     result.append(await perform_io_task(2, 1)),
#     result.append(await perform_io_task(3, 4))
#
#     end_time = time.perf_counter()
#     print(f"Total time spent: {end_time - start_time:.3f}")
#
#     print(f"Result: {result}")

# if __name__ == "__main__":
#     asyncio.run(main_process())
#     # asyncio.run(main_process_split())

# async def mock_api_request(request_data):
#     print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] API Service: Get request on {request_data["type"]}")
#     await asyncio.sleep(random.uniform(0.5, 1.5))
#     response_data = {"status": random.choice(["success", "failed"]), "message": f"API Service get request_data: {request_data["payload"]} "}
#     print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] API Service: Request processed.")
#     return response_data
#
# async def send_api_request(request_data, payload):
#     print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] Start request: Send request {request_data}")
#     response = await mock_api_request({"type": request_data, "payload": payload})
#     print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] Get response from API: Response{response}")
#     return response
#
# async def main():
#     request_to_send = [
#         ("login", {"username":"user1"}),
#         ("get_profile", {"user_id":122}),
#         ("logout", {"data": None})
#
#     ]
#
#     start_time = time.perf_counter()
#
#     tasks = [send_api_request(req_type, payload) for req_type, payload in request_to_send]
#     try:
#         response = await asyncio.gather(*tasks)
#     except TypeError as e:
#         print(e)
#         print("fail to get response")
#     else:
#         end_time = time.perf_counter()
#
#         print(f"Spent time: {end_time - start_time}")
#
#         [print(resp) for resp in response]
#
#
# asyncio.run(main())

base_url = "https://jsonplaceholder.typicode.com"

async def send_api_request(session, request_type, resource_id):
    url = f"{base_url}/{request_type}/{resource_id}"

    try:
        async with session.get(url) as response:
            response.raise_for_status()
            data = await response.json()
            return {"type": request_type, "id": resource_id, "data": data}
    except aiohttp.ClientError as e:
        print(e)
        return {"type": request_type, "id": resource_id, "data": "error"}

async def main():
    request_data = [
        ("posts", 1),
        ("comments", 5),
        ("todos", 10),
        ("users", 2),
        ("posts", 9999)
    ]

    async with aiohttp.ClientSession() as session:
        tasks = [send_api_request(session, request_type, resource_id) for request_type, resource_id in request_data]
        response = await asyncio.gather(*tasks)

    for resp in response:
        print(resp)

asyncio.run(main())