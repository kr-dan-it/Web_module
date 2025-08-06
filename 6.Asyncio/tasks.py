import asyncio
import time
import datetime
import random
import aiohttp

# Імітуйте 3 асинхронні "API-виклики", кожен з яких має випадкову
# затримку від 0.5 до 2.0 секунд. Використайте `asyncio.gather()`
# для їх конкурентного виконання. Виведіть загальний час виконання.

# async def perform_api_call(api_id):
#     print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] API id: {api_id}: Start API call.")
#     await asyncio.sleep(random.uniform(0.5, 2))
#     print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] API id: {api_id}: End API call.")
#     return f"API_id: {api_id}"
#
# async def main_process():
#     print("-" * 30)
#     print("With gather")
#     start_time = time.perf_counter()
#
#     result = await asyncio.gather(
#         perform_api_call(1),
#         perform_api_call(2),
#         perform_api_call(3)
#     )
#
#     end_time = time.perf_counter()
#     print(f"Total time spent: {end_time - start_time:.3f}")
#
#     print(f"Result: {result}")
#
# if __name__ == "__main__":
#     asyncio.run(main_process())

# Створіть асинхронну функцію `get_post_and_comments(session, post_id)`,
# яка одночасно (конкурентно) отримує дані про пост та всі його коментарі з JSONPlaceholder.
# URL для поста: `https://jsonplaceholder.typicode.com/posts/{post_id}`
# URL для коментарів: `https://jsonplaceholder.typicode.com/posts/{post_id}/comments`
# Виведіть заголовок поста та кількість коментарів.

base_url = "https://jsonplaceholder.typicode.com"

async def get_post_and_comments(session, post_id):
    post_url = f"{base_url}/posts/{post_id}"
    comment_url = f"{base_url}/posts/{post_id}/comments"

    try:
        async with session.get(post_url) as response:
            response.raise_for_status()
            data_post = await response.json()

        async with session.get(comment_url) as response:
            response.raise_for_status()
            data_comment_post = await response.json()

        return {"title": data_post['title'], "num_post_comments": len(data_comment_post)}
    except aiohttp.ClientError as e:
        print(e)
        return {"title": "", "num_comments": 0}

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [get_post_and_comments(session, id_) for id_ in range(1, 11)]
        response = await asyncio.gather(*tasks)

        for resp in response:
            print(resp, "\n")

if __name__ == "__main__":
    asyncio.run(main())