import requests
import asyncio
import json
import os
import dotenv
dotenv.load_dotenv()

rhyms = []
async def rhyme_finder(word): 
    global rhyms
    api_key = os.getenv("API_KEY_RHYME")
    url = f"https://rhyming.ir/api/rhyme-finder?api={api_key}&w={word}&sb=1&mfe=2&eq=1"
    response = requests.request("GET", url)
    result = json.loads(response.text)
    for word in result['data_items']:
        rhyms.append(word['word'])
    return rhyms

async def get_states(): 
    url = f"https://iran-locations-api.vercel.app/api/v1/fa/states"
    response = requests.request("GET", url)

    return response

async def get_cities(state_id): 
    url = f"https://iran-locations-api.vercel.app/api/v1/fa/cities?state_id={state_id}"
    response = requests.request("GET", url)
    result = json.loads(response.text)

    return result

async def get_coordinates(list_of_states):
    list_of_states = json.loads(list_of_states)
    for state in list_of_states:
        if state['name'] == "خراسان رضوی":
            cities_list = await get_cities(state['id'])
            break
    for city in cities_list:
        if city['name'] == "مشهد":
            return city['latitude'],city['longitude']



async def main():
    await asyncio.create_task(rhyme_finder("جانان"))
    print(f"rhyms of جانان are {rhyms}")
    try:
        states_list = await get_states()
        await asyncio.sleep(1)
        latitude, longitude = await get_coordinates(states_list.text)
        print(latitude, longitude)
    except Exception as e:
        print(e)


if __name__=="__main__":
    asyncio.run(main())
